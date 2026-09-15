"""
Mermaid diagram renderer for The SOC Career Development Handbook.

Adapted from detection-engineering-handbook/release-v2/build/render_mermaid.py
and soc-manager-handbook/build/mmdc_render.py, with one change this book's
draft required that neither sibling did: chapters/*.md arrived in a MIXED
state after review — some fences already have a reviewer-inserted
`![Figure N.N ...](../assets/diagrams/fig-....svg)` tag right after them
(pointing at a file that doesn't exist on disk yet), and some have only the
fenced Mermaid source plus a caption paragraph naming a `FIG-####` ID with no
tag at all yet.

This script therefore runs in two passes per file:
  1. INSERT — for a fence with no image tag yet, find the caption's
     `FIG-####` id, look up the committed filename for that id in
     VISUAL-INVENTORY.md, and insert the tag right after the caption
     paragraph (same convention already used by the reviewer-tagged chapters).
  2. RENDER — for every fence (now all have a tag, one way or another),
     resolve the tag's relative path and render the fenced Mermaid source to
     that exact path via @mermaid-js/mermaid-cli.

Never invents a new filename when one is already committed (in an existing
tag or in VISUAL-INVENTORY.md) — that would silently orphan the figure ID's
recorded path.
"""

import os
import re
import subprocess
import glob

ROOT = r"C:\Users\User\projects\soc-career-development-handbook"
CHAPTER_GLOBS = [
    os.path.join(ROOT, "chapters", "*.md"),
    os.path.join(ROOT, "appendices", "*.md"),
]
DIAGRAM_DIR = os.path.join(ROOT, "assets", "diagrams")
VISUAL_INVENTORY = os.path.join(ROOT, "VISUAL-INVENTORY.md")
os.makedirs(DIAGRAM_DIR, exist_ok=True)

MMDC_CMD = ["npx", "-y", "@mermaid-js/mermaid-cli"]

MERMAID_RE = re.compile(r"```mermaid\r?\n(.*?)```", re.DOTALL)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.svg)\)")
FIGCAP_RE = re.compile(r"\*\*(Figure [\d.]+ — [^*]+?)\*\*")
FIGID_RE = re.compile(r"FIG-(\d{4})")
INVENTORY_ROW_RE = re.compile(r"`FIG-(\d{4})`.*?assets\\diagrams\\([\w.\-]+\.svg)")

SEARCH_WINDOW = 2500  # chars after a fence's closing ``` to look for a caption/tag
LOOKBEHIND_WINDOW = 2500  # chars before a fence's opening ``` to look for a caption that precedes it


def load_inventory_filenames():
    with open(VISUAL_INVENTORY, "r", encoding="utf-8") as f:
        text = f.read()
    mapping = {}
    for m in INVENTORY_ROW_RE.finditer(text):
        mapping[m.group(1)] = m.group(2)
    return mapping


def render_one(mmd_text, out_svg):
    tmp_mmd = out_svg + ".mmd"
    with open(tmp_mmd, "w", encoding="utf-8") as f:
        f.write(mmd_text)
    cmd = MMDC_CMD + ["-i", tmp_mmd, "-o", out_svg, "-b", "white"]
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=90)
    ok = os.path.exists(out_svg) and os.path.getsize(out_svg) > 0
    try:
        os.remove(tmp_mmd)
    except OSError:
        pass
    return ok, result.stdout, result.stderr


def insert_missing_tags(content, inventory):
    """Pass 1: insert an image tag for any fence that doesn't have one yet.

    This book's chapters use two different reviewer conventions for where the
    caption sits relative to the fence (confirmed by manual inspection of the
    10 already-tagged chapters before writing this): most put the caption
    right after the fence and the tag right after the caption (fence ->
    caption -> tag); a few put the caption *before* the fence and the tag
    immediately after the fence's closing ``` (caption -> fence -> tag). One
    chapter (Part 5) has a caption before the fence with nothing after it at
    all. Both conventions are handled; a fence matching neither is skipped
    and reported rather than guessed at.
    """
    matches = list(MERMAID_RE.finditer(content))
    new_content = content
    offset = 0
    inserted = 0
    skipped = []

    for m in matches:
        fence_start = m.start() + offset
        fence_end = m.end() + offset
        tail = new_content[fence_end:fence_end + SEARCH_WINDOW]

        existing = IMG_RE.search(tail)
        if existing and existing.start() < 600:
            continue  # already tagged, pass 2 will render it

        cap = FIGCAP_RE.search(tail)
        if cap:
            # Convention: fence -> caption -> tag. Insert after the caption's paragraph.
            id_m = FIGID_RE.search(tail[cap.end():cap.end() + 1000])
            if not id_m:
                skipped.append(f"caption '{cap.group(1)[:40]}...' has no FIG-#### id nearby")
                continue
            fig_id = id_m.group(1)
            filename = inventory.get(fig_id)
            if not filename:
                skipped.append(f"FIG-{fig_id} not found in VISUAL-INVENTORY.md")
                continue
            para_end_rel = tail.find("\n\n", cap.end())
            if para_end_rel == -1:
                para_end_rel = len(tail)
            insert_at = fence_end + para_end_rel
            rel_path = f"../assets/diagrams/{filename}"
            img_line = f"\n\n![{cap.group(1)}]({rel_path})\n"
            new_content = new_content[:insert_at] + img_line + new_content[insert_at:]
            offset += len(img_line)
            inserted += 1
            continue

        # No caption after the fence — check whether it precedes the fence instead
        # (convention: caption -> fence -> tag).
        head = new_content[max(0, fence_start - LOOKBEHIND_WINDOW):fence_start]
        cap_before_matches = list(FIGCAP_RE.finditer(head))
        if not cap_before_matches:
            skipped.append("no caption found before or after fence")
            continue
        cap_before = cap_before_matches[-1]  # closest one to the fence
        id_m = FIGID_RE.search(head[cap_before.end():cap_before.end() + 1000])
        if not id_m:
            skipped.append(f"caption '{cap_before.group(1)[:40]}...' (before fence) has no FIG-#### id nearby")
            continue
        fig_id = id_m.group(1)
        filename = inventory.get(fig_id)
        if not filename:
            skipped.append(f"FIG-{fig_id} not found in VISUAL-INVENTORY.md")
            continue
        rel_path = f"../assets/diagrams/{filename}"
        img_line = f"\n\n![{cap_before.group(1)}]({rel_path})\n"
        new_content = new_content[:fence_end] + img_line + new_content[fence_end:]
        offset += len(img_line)
        inserted += 1

    return new_content, inserted, skipped


def render_all_tagged(content, chapter_dir):
    """Pass 2: every fence should now be followed by a tag; render each to its target path."""
    matches = list(MERMAID_RE.finditer(content))
    rendered = 0
    failed = 0
    errors = []

    for m in matches:
        mmd_text = m.group(1)
        tail = content[m.end():m.end() + SEARCH_WINDOW]
        existing = IMG_RE.search(tail)
        if not existing:
            errors.append("fence still has no resolvable image tag after insert pass")
            failed += 1
            continue

        rel_path = existing.group(1)
        out_svg = os.path.normpath(os.path.join(chapter_dir, rel_path))
        ok, out, err = render_one(mmd_text, out_svg)
        if ok:
            rendered += 1
        else:
            failed += 1
            errors.append(f"{out_svg}: {err.strip()[:300]}")

    return rendered, failed, errors


def process_file(path, inventory):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "```mermaid" not in content:
        return None

    new_content, inserted, skipped = insert_missing_tags(content, inventory)
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        content = new_content

    rendered, failed, errors = render_all_tagged(content, os.path.dirname(path))
    return inserted, skipped, rendered, failed, errors


def main():
    inventory = load_inventory_filenames()
    files = []
    for g in CHAPTER_GLOBS:
        files.extend(sorted(glob.glob(g)))

    total_inserted = total_rendered = total_failed = 0
    for path in files:
        result = process_file(path, inventory)
        if result is None:
            continue
        inserted, skipped, rendered, failed, errors = result
        total_inserted += inserted
        total_rendered += rendered
        total_failed += failed
        print(f"{os.path.basename(path)}: inserted_tags={inserted} rendered={rendered} failed={failed}", flush=True)
        for s in skipped:
            print(f"  SKIP: {s}")
        for e in errors:
            print(f"  ERROR: {e}")

    print(f"\n=== TOTAL: inserted_tags={total_inserted} rendered={total_rendered} failed={total_failed} ===")


if __name__ == "__main__":
    main()
