# The SOC Career Development Handbook

**Study Plans, Home-Lab Projects, Portfolios, and Interview Prep — The Analyst's Own Climb From L1 to SOC Architect**

📄 **[Download the full PDF](./SOC_Career_Development_Handbook.pdf)** — 326 pages, ~139,000 words across 24 parts.

Part of the **NESHBOY SOC Professional Library**, alongside [SIGNAL TO ACTION: The Complete SOC Playbook Handbook](https://github.com/neshboy/soc-playbook-handbook), [The Detection Engineering Handbook V2](https://github.com/neshboy/detection-engineering-handbook), and [The SOC Manager's Operating Handbook](https://github.com/neshboy/soc-manager-handbook).

This is a handbook for the person doing the climbing, not the person designing the ladder. **The SOC Manager's Operating Handbook is this book's direct counterpart from the other side of the desk** — it already owns, in real depth, how a manager builds a competency matrix (Part 10), runs a promotion committee and fights leveling drift (Part 13), and designs a defensible hiring bar and interview loop (Parts 7–8). This book does not re-derive any of that organizational machinery. It answers a different question, asked from the analyst's own chair: if you are the person being evaluated, not the person building the evaluation, what do you actually need to know, build, practice, and demonstrate to move from where you are to where you want to be — L1 to L2, L2 to L3, L3 into a specialist branch (detection engineer, threat hunter, incident responder) or into leadership, and from team lead through SOC manager to SOC architect. The test applied throughout drafting: if a paragraph describes what an organization does to evaluate or develop people, it belongs in the SOC Manager's Operating Handbook and gets cited, not rewritten; if it describes what you personally do to get ready, it belongs here.

## Reading the book

- **[SOC_Career_Development_Handbook.pdf](./SOC_Career_Development_Handbook.pdf)** — the assembled, print-ready book. Start here.
- **[BOOK-INDEX.md](./BOOK-INDEX.md)** — the full part table with per-unit scope, the series map against the other three NESHBOY volumes, and the multi-level content model.
- **[STYLE-GUIDE.md](./STYLE-GUIDE.md)** — the voice, formatting, and figure-evidence-classification contract every part follows: seven content tags (`[CONCEPT]`, `[L1/L2]`, `[SENIOR/SPECIALIST]`, `[LEAD/MANAGEMENT TRACK]`, `[STUDY PLAN]`, `[INTERVIEW PREP]`, `[MINDSET]`) and eight recurring callouts (Career Autopsy, Analyst's Note, Ground Truth, Blind Spot, Career Trap, Cross-Book Pointer, Field Test, What Would Change My Mind), adapted from the SOC Manager's Operating Handbook's style contract — itself adapted from the Detection Engineering Handbook V2's — for series-wide consistency.

## What's synthetic vs. real

Every case study, timeline, and worked example in this book is a **CONCEPTUAL** illustration or a **COMPOSITE CASE EXAMPLE** (a plausible scenario built from patterns, not one real person's identifiable career) — never a claim that a specific, identifiable analyst's career is being described. Diagrams are original Mermaid flowcharts and decision trees, mostly self-assessment routing logic rather than org-process diagrams. This book contains no fabricated screenshots or invented "real" company data.

## The planned SOC Home Lab Handbook

Several parts — most visibly Part 5 (The Home-Lab Foundation) and Part 10, 12, 14, 16, and 17's lab projects — flag home-lab build instructions inline as `[HOME LAB — companion volume not yet written]`, per a deliberate, tracked structural decision recorded in `BOOK-INDEX.md`: a dedicated *SOC Home Lab Handbook* was planned to eventually own step-by-step build instructions (VM sizing, ingestion-pipeline configuration, hardware/cloud-cost tradeoffs) that this book's parts currently carry in enough detail to attempt stand-alone, but don't go deeper on.

That gap is now partially closed on the drafting side: a `soc-home-lab-handbook` project exists locally (22 chapters, all status `reviewed`) but has not yet been published to GitHub — `neshboy/soc-home-lab-handbook` does not resolve as of this release. Once it publishes, every `[HOME LAB — companion volume not yet written]` flag in this book's chapters becomes a stale reference that should be updated to cite the real part number directly, the same way this book already cites the SOC Manager's Operating Handbook, SOC Playbook Handbook, and Detection Engineering Handbook V2 by name and part. That rewrite is out of scope for this release — it touches chapter prose, not build tooling — and is tracked here as a known follow-up rather than actioned.

## How it was built

- `build/build_book.js` — parses `BOOK-INDEX.md`'s Part Table, assembles all 24 chapter files into one HTML document, and prints it to PDF via headless Chrome. Deliberately stops before `## Appendix Table`: this book's 7 appendices (A1–A7) are indexed but not drafted yet, so the current release covers Parts 1–24 only.
- `build/render_mermaid.py` — renders Mermaid diagram source to SVG via `@mermaid-js/mermaid-cli`. Chapters arrived from review in a mixed state — some fences already had a reviewer-inserted image tag pointing at an SVG that didn't exist on disk yet, some had only a captioned `FIG-####` reference with no tag at all — so this script inserts the missing tags (resolving each `FIG-####` against `VISUAL-INVENTORY.md`) before rendering every fence to its tagged path.
- `build/add_watermark.py` — applies the diagonal `neshboy` watermark to every page.
- `CASE-INVENTORY.md`, `TEMPLATE-INVENTORY.md`, `VISUAL-INVENTORY.md` — permanent IDs for every named case study, reusable template, and figure, tracked independently of position in the book so cross-references never break on reorganization.

## Rebuilding it yourself

```
cd build
npm install
python render_mermaid.py
node build_book.js
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer ^
  --print-to-pdf="..\_build\SOC_Career_Development_Handbook.pdf" "..\_build\book.html"
python add_watermark.py
```

## Repository layout

- `chapters/` — the 24 parts, Markdown source of record. `appendices/` is reserved for the 7 planned appendices (A1–A7, indexed in `BOOK-INDEX.md`) but is empty as of this release — not yet drafted.
- `assets/diagrams/` — rendered Mermaid SVGs.
- `build/` — the build/render/watermark tooling above.
- `BOOK-INDEX.md`, `STYLE-GUIDE.md`, `CASE-INVENTORY.md`, `TEMPLATE-INVENTORY.md`, `VISUAL-INVENTORY.md` — cross-cutting project documentation.
