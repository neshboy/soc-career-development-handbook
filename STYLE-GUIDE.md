# The SOC Career Development Handbook — STYLE-GUIDE.md

**Status:** Adopted for the NESHBOY SOC Professional Library, adapted from the SOC Manager's Operating Handbook `STYLE-GUIDE.md` (itself adapted from the Detection Engineering Handbook V2's) for series consistency.
**Applies to:** every part, appendix, template, and figure in this book.
**Audience:** every writer, technical reviewer, and editor working on this book.

## Why this document exists

This is a cross-series brand standard, not a from-scratch style guide. The voice rules, the banned-filler list, and the general mechanic of "six content tags, one fixed callout-box system, four figure-evidence classes" are carried over near-verbatim from the SOC Manager's Operating Handbook's style guide, which itself carried them over from the Detection Engineering Handbook V2's. Only the *content* of the tags, callouts, and evidence classes is redesigned for this book's audience — the individual analyst planning and building their own career, not the manager who evaluates them or the engineer who builds the detection logic. The *mechanic* (bold bracketed tag, fixed blockquote template, no invented variants) is not redesigned; a reader moving between all four NESHBOY volumes should recognize the same skeleton every time, even though this book's subject — one person's own growth, not an organizational program — is the most personal in the series.

**"Must"** means a PR gets rejected if it doesn't comply. **"Should"** means deviate only with a reason recorded in the PR description. **"Avoid"** is a strong default a reviewer can override with justification, and a documented override is a guide change, not silent drift.

This guide governs prose voice, Markdown conventions, the eight recurring callout boxes, content-level tags, cross-book citation format, and the evidence-classification system for figures. It does not cover technical review standards (accuracy of a cited certification's exam objectives, correctness of a home-lab build's network diagram) — that is a separate concern with a separate reviewer, per the production model in `BOOK-INDEX.md`.

---

## 1. Voice and Tone

### 1.1 The core rule

Write like a sharp senior analyst leveling with a newer one over coffee, not a manager briefing a peer and not a certification vendor selling a bootcamp. The reader is not being sold on a career; they've already decided to have one, or are seriously weighing it, and they need a straight answer about what the next 12 months of study and practice actually require. Every sentence should survive the question: **what does this actually tell me to study, build, practice, or ask myself?** If it doesn't, cut it.

Concretely:

- **State the claim, then the evidence.** Don't build up to it with scene-setting.
- **Name the failure mode; don't gesture at it.** "This gets you a 'ready, but not yet demonstrated' verdict at your next review" beats "this can present challenges to your advancement."
- **Prefer the concrete number over the vague qualifier.** "Two structured hunts, one resolving to a real negative finding" beats "meaningful hunting experience."
- **Name the skill, the certification, the home-lab project, the specific evidence a reviewer will look for** — not the adjective. Say what to build and what it proves, not that it's important.
- **Prefer active voice with a named actor** ("you," "the reviewer," "the committee," "the hiring panel") over passive constructions that hide who does what.
- **Commit to a claim.** If evidence is thin, say so explicitly ("this certification-value ranking reflects hiring-manager anecdote and this book's own judgment, not a controlled study — treat it as a starting heuristic, not gospel") rather than hedging with vague qualifiers.
- Second person ("you") is the default register in this book — more than in any of its companion volumes, because the subject is the reader's own career, not an abstracted "the analyst." First person plural ("we") is fine for the book's own reasoning. Neither should be used to manufacture urgency or motivational-poster energy.
- It is okay to say a certification is overrated, a home-lab project is optional, or a career step is boring and mostly about time-in-seat. Not every study plan needs to sound like a transformation.

### 1.2 Banned filler — and the actual rule behind the ban

The patterns below are banned **only in their AI-marketing-filler usage** — as a load-bearing transition, hedge, or intensifier that could be deleted with no loss of meaning, or that signals "content" rather than a claim. Mechanically grepping-and-blocking normal English is explicitly wrong: several of these words have legitimate, specific uses that are fine to keep. **The reviewer's test: does this phrase carry information, or does it just sound like it does?** If a reviewer can delete the phrase and the sentence loses nothing, it's filler — cut it.

| Banned pattern (as filler) | Why it's banned | Legitimate exception |
|---|---|---|
| "in today's rapidly evolving threat landscape" | Says nothing; every landscape is always evolving | None — always cut, replace with the specific change you mean |
| "it is crucial / critical / important / paramount that..." | Asserts importance instead of demonstrating it | Rewrite as the concrete consequence of skipping the thing |
| "passion for security" / "passionate about cybersecurity" | Unfalsifiable, and the exact phrase a job-description defect this book warns readers to see past — using it here would be self-undermining | None in this book's own voice; fine when quoted as an example of what *not* to write in a resume |
| "leveraging" | Nearly always means "using" | Keep only if something is literally used as leverage in a specific mechanical sense (rare) |
| "holistic" | Vague scope-inflation word | Cut; say what specific things are actually being combined |
| "unlock your potential" / "level up" / "10x" as vague self-improvement verbs | Motivational-content filler that names no mechanism | Use the literal verb and the literal mechanism: "closes the judgment gap," "clears the L2 tool-proficiency bar" |
| "delve into" | AI-pattern verb-of-choice for "discuss/examine" | Use "look at," "cover," "walk through" |
| "in conclusion" / "to summarize" as a section opener | Signposting the reader doesn't need — headings already do this | None in body prose |
| "it is important to note that..." | Hedge that adds no information; if worth saying, say it directly | None — cut the phrase, keep the note only if something remains |
| "grind" / "hustle" as a standalone virtue ("just grind it out") | Names no specific practice, study hour count, or project — praises effort in the abstract | Fine describing a specific, bounded activity: "a two-week grind through the ATT&CK matrix, one technique a day" |
| "unlock / empower / elevate" as verbs for a skill or credential | Marketing verbs, not operational verbs | Use the literal verb: "clears the bar," "gives you a defensible answer in the interview," "cuts your triage time by..." |
| "at the end of the day" | Filler transition | Cut |
| "game-changer / game-changing / cutting-edge / best-in-class" | Unfalsifiable superlative | Cut, or state the measurable change |

A phrase is **not** banned just because it contains one of these words. Two tests:

- "Getting comfortable with ambiguity is important because the judgment axis is exactly where a stalled L2 nomination usually hides, per the failure mode SOC Manager's Operating Handbook Part 10 §2 names from the reviewer's side" — `important` is load-bearing and explained. Keep it.
- "The hiring landscape for mid-level analysts got noticeably tighter after two regional MSSPs opened local offices and started offering a 15% pay premium to poach" — a specific, falsifiable claim, not the stock phrase. Keep it.

### 1.3 Worked GOOD vs. BAD examples

**Example 1 — opening a section**

> BAD: "In today's competitive cybersecurity job market, it is crucial for aspiring analysts to build a robust, holistic skill set that will empower their career growth."

> GOOD: "An L1 req on a mainstream job board typically fills inside 30 to 45 days, which means the L1 market is not actually as tight as certification-bootcamp marketing implies — the bottleneck is L2. If you're choosing where to spend your next three months of study time, spending it on depth that clears an L1 bar you'll pass anyway is a weaker bet than spending it on the judgment-under-ambiguity evidence Part 11 covers, because that's the gap that actually stalls people a year in."

**Example 2 — describing a limitation**

> BAD: "It is important to note that this study plan may present certain challenges depending on individual circumstances."

> GOOD: "This study plan assumes roughly five hours a week outside your shift. If you're working a fixed night rotation with one weekend in six, that number is optimistic — cut the plan's pace in half rather than skipping the home-lab projects, because the projects are what actually produce interview-ready evidence, not the reading."

**Example 3 — closing a section**

> BAD: "In conclusion, a holistic, passionate approach to home labs will empower your journey toward SOC career success."

> GOOD: "None of this works if the lab gets built once, screenshotted for a portfolio, and never touched again. A detection you wrote eight months ago and haven't looked at since doesn't prove ongoing judgment — it proves you could do the exercise once. Keep at least one lab project actively changing."

**Example 4 — a hedge that should just be a claim**

> BAD: "It is crucial to note that choosing between threat hunting and detection engineering is paramount to consider carefully."

> GOOD: "Detection engineering and threat hunting reward almost opposite tolerances for a hypothesis resolving to nothing. If a hunt that finds no adversary and no finding feels like wasted time rather than a real, useful negative result, that's a signal worth taking seriously before you spend six months building a hunt portfolio for a branch that will grind on you — see Part 3's self-assessment framework before Part 16's hunt-specific study plan, not after."

**Example 5 — false confidence vs. honest uncertainty**

> BAD: "This certification provides a robust, comprehensive path to a six-figure security career."

> GOOD: "This certification is a reasonable signal at the L1 sourcing stage and close to irrelevant once you have two years of real triage on your resume — see Part 6 for the sequencing table and the specific point past which it stops paying for itself in study time versus a home-lab project instead."

### 1.4 Sentence and paragraph mechanics

- Default to active voice; passive only when the actor genuinely doesn't matter.
- One claim per sentence where possible. Prefer sentences under ~30 words; if a sentence has more than one comma-joined independent clause carrying real content, split it.
- One idea per paragraph. A paragraph that introduces a study-plan item, then its home-lab pairing, then a certification note, then a cross-reference should be four short paragraphs or a callout box, not one block.
- Numbers: use digits for headcount, percentages, dollar amounts, time budgets (hours/weeks), and any count ≥ 10; spell out one through nine in prose ("three hunts," not "3 hunts") — except inside tables, where digits are always used for scanability, and except for counts paired with an identifier or unit (Tier 2, a 90-day plan, Part 11, a 1:6 study-to-lab time ratio), which always use digits regardless of size.
- Contractions ("doesn't," "isn't," "won't") are fine and preferred — this book has a spoken-voice register, not a legal-document register.
- Address the reader directly when giving instructions ("build this," "practice this," "ask yourself"). Do not switch to a hypothetical third-person "the analyst" mid-book just to sound more formal — the whole point of this volume's voice is that the reader is the subject, not a case study.

---

## 2. Heading Level Conventions

Locked down for series consistency:

| Level | Use for | Example |
|---|---|---|
| `#` (H1) | Part title only. One per file, first line of the file. | `# Part 11 — Making the Jump to L2: Closing the Judgment Gap` |
| `##` (H2) | Major numbered sections within a part (the part's own table-of-contents entries). Number sequentially: `## 1. Title`, `## 2. Title`. | `## 3. Building a personal ambiguous-call log` |
| `###` (H3) | Subsections within a major section — a specific exercise, a specific template, a specific sub-topic. Number as `### 3.2 Title` under `## 3`, never restarted as an independent `### 1`. | `### 3.2 What to write down before you know the resolution` |
| `####` (H4) | Rare; only for structured sub-breakdowns inside a long H3 that need their own anchor (e.g., "What to build," "Worked example," "Common mistakes" inside one exercise writeup, when those aren't rendered as callout boxes). Do not nest deeper than H4. | `#### Common mistakes` |

Rules:

- **Callout boxes are never headings** (see §6) — they are blockquotes opened with a bold label, at the same nesting level as the paragraph they annotate.
- Never skip a level (no H2 directly to H4).
- Every part must open with an unnumbered `## Why this part exists` section before numbering starts at `## 1.` — mandatory for all 24 parts.
- Every H2 and H3 must be unique within its file — needed for stable anchor links from the index and cross-references.
- Section titles are sentence case, not Title Case ("Closing the judgment gap," not "Closing The Judgment Gap"). Part titles use title case with an em dash, per the series convention (`# Part 11 — Making the Jump to L2: Closing the Judgment Gap`).
- When a named exercise or template gets a dedicated `###` walkthrough, format the heading as a plain descriptive label, not a restated sentence: `### The ambiguous-call reasoning log`, not `### This is how you keep track of ambiguous calls you've made`.

---

## 3. Template, Worksheet & Study-Plan Block Conventions

This book's structured artifacts are self-assessment worksheets, study-plan calendars, home-lab build checklists, resume/portfolio templates, and interview-practice scripts — not source code or organizational policy documents. Fenced blocks are still used, adapted from the SOC Manager's Operating Handbook's convention:

| Content type | Fence tag | Notes |
|---|---|---|
| Reusable template body (resume skeleton, study-plan calendar, self-assessment worksheet, home-lab checklist) | `` ```text `` or `` ```markdown `` (whichever the template is authored in) | Precede with a one-line label: `TEMPLATE — <name>, permanent ID TMPL-####`. The template's permanent ID and its home appendix (per §5) go in that label line, not buried in prose. |
| Worked example calendar or numeric estimate (study hours per week, a lab-build time budget, a certification cost/time tradeoff) | `` ```text `` | Every invented number carries the label `CONCEPTUAL SAMPLE — illustrative numbers, not a validated benchmark`. Reserve this for teaching examples; never label a real, sourced case this way (use the §9 evidence-class caption instead). |
| Home-lab architecture sketch, career-path decision tree, promotion-evidence flow | `` ```mermaid `` | See §10 — the fenced source stays in the file as the editable source of truth alongside its rendered image reference, never deleted once rendered. |
| Quoted job-posting language, real (anonymized) interview-scorecard excerpt, or certification exam-objective text | `` ```text `` | Must carry an evidence-class caption per §9 (typically `ANONYMIZED CASE EXAMPLE` or `OFFICIAL REFERENCE`), not just the fence. |

Additional rules:

- Every template block must be preceded by one sentence stating who uses it and when, and followed by one sentence stating its main limitation or the judgment call it doesn't automate — a bare template with no framing is grounds for reviewer rejection.
- Inline code (single backtick) is for field-like tokens inside prose — a template ID (`` `TMPL-1101` ``), a certification acronym on first definition, a home-lab tool name — never a substitute for a fenced block when showing more than one line of structured content.
- Annotations inside a template explain *why* a field exists or *what the reader should write there*, not restate the obvious: `<!-- name the specific enrichment you'd request and why, not "explain your reasoning" -->`, not `<!-- this is a text field -->`.

---

## 4. Citing the Other Three Books — Cross-Reference Format

Because this book's entire value proposition rests on not re-explaining what the SOC Manager's Operating Handbook, SOC Playbook Handbook, and Detection Engineering Handbook V2 already own, a sloppy or bare citation is a structural defect, not a style nit. This is doubly true for the SOC Manager's Operating Handbook specifically, since this book and that one cover the *same subject matter* from opposite chairs — the citation is the only thing keeping the two books from silently duplicating each other.

- **First cross-reference to a given part within a section:** full form — book title, comma, "Part NN," em dash, part title. `SOC Manager's Operating Handbook, Part 10 — Competency Models & Skills Matrices`. `Detection Engineering Handbook V2, Part 22 — Detection as Code`.
- **Subsequent references to the same part within the same section:** short form is fine — `SOC Manager's Handbook Part 10` or `DEH Part 22`. Never invent other abbreviations.
- **Never cite bare.** A cross-reference must state, in the same sentence, what the reader will find there and *why they'd go* — "for how a reviewer scores the judgment axis," "for the exact evidence-packet checklist a committee expects," "for the query-language mechanics behind this hunt." "See Part 13" with no reason is a lint failure.
- **When citing the SOC Manager's Operating Handbook specifically, state which side of the desk the citation is for.** Because this book constantly discusses the same artifacts (the competency matrix, the promotion committee, the hiring loop) that book owns organizationally, every citation must make clear that the reader is being pointed to *how the organization evaluates*, and that this book's own surrounding prose is about *what the reader does in response* — never blur the two into one undifferentiated paragraph.
- A single-clause pointer belongs inline. A pointer that needs more than one sentence of setup belongs in a **Cross-Book Pointer** callout (§6.6) instead of being stretched across surrounding prose.
- Every cross-reference added anywhere in the book must also be reflected in Appendix A7's lookup table — a build-check requirement, not a nice-to-have.
- Never cite a part number from memory without checking the current `BOOK-INDEX.md` of the target book — part numbers in any companion volume can shift on a future revision, and a stale citation is worse than no citation.
- Do not re-explain the cited material "just enough to be self-contained." If a paragraph needs more than the one-clause reason to make sense, that's a sign the paragraph is drifting into the other book's territory — cut it back to the pointer.
- **For the planned SOC Home Lab Handbook**, which does not exist yet: never cite a part number. Use the inline flag `[HOME LAB — companion volume not yet written]` immediately after the reference, per the convention set in `BOOK-INDEX.md`, and ensure the surrounding paragraph carries enough stand-alone detail that the reader isn't left with only a promise.

---

## 5. Referencing Templates, Cases & Figures

Permanent, position-independent IDs, tracked the same way the rest of the series tracks templates, cases, and figures:

- **`TMPL-####`** — every reusable template in the appendices (a study-plan calendar, a self-assessment worksheet, a resume skeleton, a hunt-record log). First reference in a chapter: full name plus ID, `the ambiguous-call reasoning log (TMPL-1101)`. Subsequent references in the same section: bare ID, `TMPL-1101`. Tracked in `TEMPLATE-INVENTORY.md`.
- **`CASE-####`** — every named case example used in a Career Autopsy box or a worked example (real, anonymized, or explicitly composite per §9). Same first-use/subsequent-use pattern. Tracked in `CASE-INVENTORY.md`.
- **`FIG-####`** — every rendered diagram or captured figure. Same pattern as the companion volumes. Tracked in `VISUAL-INVENTORY.md`.
- IDs are assigned once, at creation, and never reused or renumbered when the book's part order changes.
- Never invent a placeholder ID "to be assigned later" in body text — request the next ID from the relevant inventory file before the unit is marked `reviewed`.

---

## 6. Callout Boxes — Exact Templates

All eight use the same base shape: a **blockquote** (`>`) opened with a bold label line, visually and structurally consistent with each other and distinguished only by label text and (for some) internal sub-structure. They sit inline in the flow of a section — never a jump-target the table of contents would list separately, and never nested one inside another.

**General template:**

```
> **[Label — optional short qualifier]**
> Body text, 1–5 sentences. Can include inline code and a short template excerpt if needed.
```

If a box needs more than ~5 sentences, it isn't a callout — promote it to a real `###`/`####` subsection with prose.

### 6.1 Career Autopsy

Dissects a real or realistic individual career decision that went wrong: the decision, why it seemed reasonable, how it failed, what replaced it. This book's equivalent of the SOC Manager's Operating Handbook's Management Autopsy, reoriented to the person living the decision rather than the manager making one about someone else. The highest-frequency callout in the book.

```
> **Career Autopsy — "<the decision in one clause>"**
>
> **The decision:** <what was actually decided, plain description>.
>
> **Why it seemed reasonable:** <the logic that made this decision look right at the time>.
>
> **How it failed:** <the specific mechanism, with a concrete scenario>.
>
> **The fix:** <what the corrected approach adds or changes>.
```

Worked example:

```
> **Career Autopsy — "collect five certifications before applying anywhere"**
>
> **The decision:** A career-changer spends 14 months earning Security+, Network+, CySA+, a
> vendor SIEM cert, and a cloud-security cert before submitting a single application, reasoning
> that a thicker credential stack means a stronger candidacy.
>
> **Why it seemed reasonable:** Every certification felt like forward progress, each one was
> individually well-regarded, and job postings kept listing certifications in their preferred
> section, which read as evidence that more certifications equal a stronger application.
>
> **How it failed:** At the first real interview, the log-triage exercise exposed that none of the
> 14 months had included a single hands-on triage rep against ambiguous, multi-source data — the
> candidate could define terms fluently and disposition nothing under time pressure. Two rounds of
> rejection later, the feedback converged: certifications proved knowledge, not skill, and the
> exercises test skill.
>
> **The fix:** Cap certification study at one credential matched to the very next move (Part 6),
> and spend the freed months on the home-lab projects in Part 5 instead — the evidence an interview
> loop actually scores.
```

### 6.2 Analyst's Note

A tactical, practitioner-voice aside — a tip or "this is what actually works" observation. Shorter and more informal than the other boxes, but still no filler.

```
> **Analyst's Note**
> The tip or observation, stated as something you'd actually say out loud to a newer analyst over
> coffee.
```

Worked example:

```
> **Analyst's Note**
> Keep a running note of every ticket where you almost escalated but didn't, and why. Six months
> later, that file is the single best interview-prep and self-review resource you own — it's a
> record of judgment calls with your own real reasoning attached, not a reconstruction you're
> trying to remember under pressure in the room.
```

### 6.3 Ground Truth

A grounded statement about what a career step actually requires or feels like in practice, as opposed to how it's advertised, assumed, or described in a job posting, a bootcamp pitch, or a well-meaning senior's outdated memory of their own path.

```
> **Ground Truth**
> The gap between how this is advertised or assumed to work and what it actually takes, stated as
> a fact, plus the practical consequence for the reader's own planning.
```

Worked example:

```
> **Ground Truth**
> "Learn to code and you'll get hired faster" is repeated constantly in career-changer forums and
> is mostly wrong for an L1 SOC role specifically — the log-triage exercise almost never asks a
> candidate to write software, and hours spent on a general programming course compete directly
> with hours that could go into the home-lab projects in Part 5, which map far more directly onto
> what a real assessment tests. Scripting literacy pays off later, at the detection-engineer branch
> (Part 15) — it's a real skill, just not the one that gets you through the door first.
```

### 6.4 Blind Spot

A specific, named gap in what your own self-assessment, study plan, or portfolio can actually reveal about you — a limitation of self-evaluation, not an organizational or technical telemetry gap (that's the other books' Blind Spot usage).

```
> **Blind Spot**
> What your own self-assessment, practice, or portfolio cannot show you, stated specifically — the
> failure mode or population of gaps it misses.
```

Worked example:

```
> **Blind Spot**
> A self-run mock interview with a friend who isn't an analyst can validate that you can narrate a
> triage decision clearly. It cannot validate that your disposition itself is correct, because your
> friend has no way to check it either — you'll both walk away confident in an answer that might be
> wrong. Get at least one practice session reviewed by someone who's actually triaged real alerts,
> even if it's a single paid hour with a working analyst rather than a formal mentor relationship.
```

### 6.5 Career Trap

Names a specific, common individual-career mistake that will cost the reader time, money, or a missed opportunity, and what to do about it.

```
> **Career Trap**
> The specific common mistake or risk. The fix: the concrete action that resolves it — or an
> explicit statement that this is a real tradeoff with no clean fix.
```

Worked example:

```
> **Career Trap**
> Accepting an off-cycle "Lead" or "Senior" title bump from a manager trying to retain you with no
> corresponding change in scope, evidence packet, or pay band feels like a win in the moment, but
> per SOC Manager's Operating Handbook Part 13 §5, it's the exact mechanism behind leveling drift —
> and the person most exposed when a leveling audit eventually corrects it isn't the manager who
> offered the shortcut, it's you, holding a title the org's own audit may later flag as unsupported
> by evidence. Ask, in writing, what evidence and scope will back the new title before accepting it.
```

### 6.6 Cross-Book Pointer

An explicit "go here for the mechanics" reference into the SOC Manager's Operating Handbook, SOC Playbook Handbook, or Detection Engineering Handbook V2, used when a single inline citation (§4) isn't enough context to orient the reader.

```
> **Cross-Book Pointer**
> What this book does not cover here, which companion-book part covers it, and the one-clause
> reason a reader would actually go read it.
```

Worked example:

```
> **Cross-Book Pointer**
> This part does not explain how a promotion committee is composed, how it calibrates across
> teams, or what leveling drift is. See SOC Manager's Operating Handbook, Part 13 — Career Ladders
> & Promotion Criteria for the full organizational mechanics; come back here once you understand
> what the committee will be looking at, so the evidence-building advice in this part lands against
> a real target instead of a guess.
```

### 6.7 Field Test

A concrete, reproducible exercise or drill the reader can run on themselves to validate that a skill, a piece of evidence, or a self-assessment is real, plus the expected result.

```
> **Field Test**
> **Setup:** what needs to be in place first, one line.
> **Action:** the exercise or drill, stated concretely.
> **Expected result:** what should be observably true afterward.
```

Worked example:

```
> **Field Test**
> **Setup:** You believe you've closed the judgment gap between L1 and L2 triage.
> **Action:** Pull three already-resolved tickets from your own queue that were genuinely
> ambiguous at the time. Without looking at the resolution, write out your reasoning and disposition
> for each, timed at 10 minutes per ticket, then compare against what actually happened.
> **Expected result:** You should reach the same disposition, or a defensible "unable to determine
> without X," on at least two of the three, and be able to state clearly what evidence would have
> changed your answer on any you missed. If you can't reconstruct defensible reasoning under a time
> limit, the judgment gap isn't closed yet — no matter how confident it feels day to day on shift.
```

### 6.8 What Would Change My Mind

An explicit falsifiability statement — what evidence, if observed, would change the stated conclusion or confidence level. Carried over from the series' epistemic-honesty standard.

```
> **What Would Change My Mind**
> The specific observation, data point, or result that would overturn or materially revise the
> claim just made — a concrete, checkable condition, not a vague "more research needed."
```

Worked example:

```
> **What Would Change My Mind**
> This part treats a completed home-lab detection-engineering project as a stronger interview signal
> than an additional certification, based on the pattern of hiring-manager feedback cited in Part
> 15. If structured data from a real hiring pipeline showed candidates with an extra certification
> and no home-lab portfolio clearing technical interviews at a comparable rate to candidates with a
> home-lab portfolio and no extra certification, that would undercut this book's central bet on
> project-based evidence over credential stacking, and this part's guidance should shift toward
> "the two are closer to interchangeable signal than this book currently claims."
```

### 6.9 Callout usage density

A single part typically carries one or two Career Autopsy boxes, zero-to-one Career Trap, and one Cross-Book Pointer where the topic genuinely borders another book; the rest are used opportunistically. A section stacking all eight callouts is over-boxed — if every paragraph needs an annotation, the prose isn't doing its job.

---

## 7. Content-Level Tags

Format locked to `**[TAG]**` — bold, brackets, all caps, placed at the start of the paragraph or subsection it governs. Never a heading, never a footer note, never two tags on one paragraph (a sign the paragraph is doing two jobs — split it).

| Tag | Use for | Do not use for |
|---|---|---|
| `[CONCEPT]` | Foundational explanation of a career mechanic, a skill category, or a decision point, with no assumption the reader acts on it directly this week — the "what and why" a reader needs before anything else in the section makes sense. | Anything that specifies a concrete study item, project, or number — that's a lower tag even if conceptually simple. |
| `[L1/L2]` | Content for someone breaking in or working the first two rungs: foundational triage skill, first tool fluency, early study and lab priorities, first-year survival habits. | Judgment-under-ambiguity content aimed at someone already past L2 — that's `[SENIOR/SPECIALIST]`. |
| `[SENIOR/SPECIALIST]` | Content for someone at or approaching L3 and the specialist branches: judgment under ambiguity, branch-specific skill-building (detection engineering, threat hunting, IR), portfolio work proving branch readiness. | Day-to-day L1 triage mechanics — that's `[L1/L2]`. |
| `[LEAD/MANAGEMENT TRACK]` | Content for someone testing or pursuing team lead, SOC manager, or SOC architect — the individual's own preparation and self-testing for that transition. | The organizational program that evaluates or trains someone for that transition — that belongs in the SOC Manager's Operating Handbook, cited, not written here. |
| `[STUDY PLAN]` | A concrete, sequenced curriculum item: what to read or practice, in what order, and how to check it actually landed. | A one-off recommendation with no sequencing or verification step — that's likely `[CONCEPT]` or a bare Analyst's Note instead. |
| `[INTERVIEW PREP]` | Candidate-side interview preparation: practicing exercise types, building a story bank, questions to ask, negotiating from self-knowledge. | Describing how a hiring panel scores or designs the loop — that's the SOC Manager's Operating Handbook's territory, cited via Cross-Book Pointer. |
| `[MINDSET]` | Habits, self-assessment discipline, and psychological patterns — confidence calibration, documentation discipline, handling being wrong — independent of tier. | A tier-specific skill or study item that happens to also require discipline — tag it by tier/stage instead; `[MINDSET]` is for the cross-cutting habit itself, not everything that requires one. |

Tagging guidance:

- Most `##` sections carry more than one tag across their subsections — a single section on choosing a specialization plausibly has a `[CONCEPT]` opening, a `[SENIOR/SPECIALIST]` subsection on branch-specific bars, and a `[MINDSET]` subsection on the aptitude self-check. That's expected and good.
- `[CONCEPT]` is the only tag allowed to open a section before any other tag appears — every section needs grounding before it gets stage-specific.
- The two pairs authors most often confuse: `[L1/L2]` (day-to-day triage skill and early study priorities) vs. `[SENIOR/SPECIALIST]` (judgment under ambiguity and branch-specific portfolio work); `[STUDY PLAN]` (what to learn and in what order) vs. `[INTERVIEW PREP]` (how to demonstrate what you've learned under a scored, timed, adversarial condition). When in doubt, ask "is this paragraph telling the reader what to build/learn, or how to perform under evaluation" and match to the tag whose column that falls under above.
- `[LEAD/MANAGEMENT TRACK]` content must never restate the SOC Manager's Operating Handbook's organizational mechanics as if this book owns them — every `[LEAD/MANAGEMENT TRACK]` paragraph should pass the same test Part 2 sets up explicitly: is this the individual's own preparation, or the organization's evaluation program wearing this book's tag by accident?

---

## 8. Table Conventions

- Every data table gets a one-line lead-in sentence stating what decision it supports, not just "the following table shows..." — e.g., "The table below sequences which certification pays off at which career stage."
- Header row uses short noun phrases, capitalized like a title ("Typical Time Investment," not "typical time investment" or a full sentence).
- Left-align text columns; skip explicit `:---:` alignment markers unless a column is genuinely numeric and benefits from right-alignment.
- Cell content: fragments, not full sentences with terminal periods, unless a cell genuinely needs more than one sentence (rare — if so, reconsider whether it belongs in a table at all).
- Template IDs, case IDs, and field-like tokens inside cells use inline code ticks, same as in prose: `` `TMPL-1101` ``, `` `CASE-1501` ``.
- Never leave a cell blank — use an em dash "—" for "not applicable" so the omission is visibly deliberate.
- Cross-references to the other three books get their own greppable column where a table compares topics across the series, and must follow the §4 citation rules inside the cell too (full form on the row's first appearance in the table, short form after).
- Tables built from invented/illustrative data are marked `(CONCEPTUAL SAMPLE)` in the caption, same standard as template blocks in §3.

---

## 9. Figures: Evidence Classification

This book leans on career-progression narratives, self-assessment worksheets, study-plan calendars, and (occasionally) anonymized real artifacts — a redacted resume, a real home-lab architecture diagram, an actual promotion-evidence packet built from the reader's-eye view. The same discipline the rest of the series applies to screenshots and diagrams applies here, adapted to what this book actually has evidence of.

### 9.1 Evidence classes (exactly four, always tagged)

| Tag | Meaning | Allowed for |
|---|---|---|
| `ANONYMIZED CASE EXAMPLE` | Drawn from a real individual's real career decision, with identifying details scrubbed or rounded (name, employer, exact dates, exact compensation). Must be scrubbed of anything that could re-identify the person before inclusion. | Redacted resumes, real home-lab architecture diagrams, real study-plan calendars, direct quotes from a real (anonymized) interview debrief. |
| `COMPOSITE CASE EXAMPLE` | Constructed by merging patterns from multiple real career paths into one illustrative narrative — used when a single traceable real case would be too identifiable or too thin to generalize from. Must state in the caption that it is composite. | Career Autopsy narratives, worked self-assessment case studies. |
| `OFFICIAL REFERENCE` | Sourced from a published salary survey, workforce study (e.g., (ISC)², SANS, BLS), certification body's exam-objectives document, or standards body, reproduced or closely adapted with attribution. | Salary-band charts, published certification pass-rate or salary-lift data, cited industry workforce surveys. |
| `CONCEPTUAL` | An illustrative diagram or template with no claim of representing a captured real case. | Career-path decision trees, home-lab architecture sketches (as a design, not a build log), study-plan calendars, blank templates. |

A figure with no real captured evidence behind it yet is `CONCEPTUAL` if it's a diagram or template, or an explicit **pending placeholder** (§9.3) if it's meant to eventually be a real captured artifact. Never label an uncaptured, aspirational artifact `ANONYMIZED CASE EXAMPLE` "because a real one will be sourced later."

### 9.2 Caption format — rendered figure

```
**Figure N.M — [Short descriptive title].** *[Evidence class tag].* One to two sentences: what the
figure shows and what it's evidence of, or — for CONCEPTUAL figures — what it illustrates rather
than proves. If OFFICIAL REFERENCE: source citation. If ANONYMIZED/COMPOSITE CASE EXAMPLE: enough
context to be useful (career stage, rough date, industry) without being identifying.
```

Worked examples:

```
**Figure 3.1 — The specialization decision tree: detection engineer, threat hunter, IR, or
staying IC.** *CONCEPTUAL.* Illustrates the self-assessment questions this part uses to route a
reader toward a branch, not a capture of any individual's actual decision path — see Figure 3.2 for
an anonymized real example of one analyst's path through this same tree.
```

```
**Figure 10.2 — A first-year study-plan calendar with home-lab milestones.** *ANONYMIZED CASE
EXAMPLE.* Study calendar from a real L1 analyst's first 12 months (career-changer background,
mid-market SOC, ~2025), with employer name and exact dates removed. The sequencing and time
allocation are real; specific tool version numbers have been generalized to reduce
re-identification risk.
```

```
**Figure 6.1 — Median salary lift by certification, entry-level SOC roles.** *OFFICIAL REFERENCE.*
Reproduced from [industry workforce-survey source noted in REFERENCES.md], year and respondent-pool
size as published. See Part 6 for the caveats on self-selected survey populations before treating
this as a guarantee for any individual case.
```

### 9.3 Pending placeholder format

```
> **[FIGURE PENDING — target evidence class: <ANONYMIZED CASE EXAMPLE | COMPOSITE CASE EXAMPLE |
> OFFICIAL REFERENCE | CONCEPTUAL>]** What the figure will show, one sentence. Why it isn't
> sourced/rendered yet, one sentence. What claim in the surrounding text it would support.
```

A reviewer finding this block logs it in the tracked-placeholder list in `VISUAL-INVENTORY.md`; it must be resolved before the unit ships — never left as permanent content.

---

## 10. Diagram Rendering Requirement

Career-path decision trees, home-lab architecture sketches, and promotion-evidence flow diagrams are drafted as Mermaid source and treated the same way the rest of the series treats every diagram — as a draft, not a deliverable:

- Every `` ```mermaid `` block must be rendered to a static image (SVG preferred, PNG acceptable) and committed alongside the source, referenced via the §9.2 caption format with a real evidence-class tag (almost always `CONCEPTUAL`, unless it's a literal reproduction of an `OFFICIAL REFERENCE` diagram).
- The Mermaid source stays in the file, directly above or below the rendered image reference — it is the editable source of truth, not dead weight to delete once rendered.
- A unit is not review-complete if it contains a `mermaid` fence with no paired rendered figure reference. This is enforced as a build check, not a manual convention (see `BOOK-INDEX.md` production model).

---

## 11. Review Checklist (for the independent reviewer, per unit)

Work from this list, not from vibes:

1. **Voice:** any banned filler pattern present without being rewritten? Any sentence that doesn't survive the "what does this tell me to study/build/practice/ask myself" test? Any drift into third-person "the analyst" instead of second-person "you"?
2. **Headings:** correct level nesting, no heading used as a bold-line substitute, `## Why this part exists` present?
3. **Templates/blocks:** every template block labeled with its name and `TMPL-####`, every invented worked number marked `CONCEPTUAL SAMPLE`, framing sentences present?
4. **Cross-book citations:** full form on true first use per section, short form after, never bare (§4 test: does the sentence state *why* the reader would go there), reflected in Appendix A7? Every SOC Manager's Operating Handbook citation clearly marked as "how the org evaluates," distinct from this book's own "what you do about it"?
5. **IDs:** `TMPL-####`/`CASE-####`/`FIG-####` used correctly, no placeholder IDs left unassigned, inventories updated?
6. **Callouts:** correct label string, correct blockquote structure, body length in range, no box type nested in another, density not excessive (§6.9)?
7. **Tags:** every `##`/`###` subsection carries at least one `[TAG]`, no paragraph carries two, no `[LEAD/MANAGEMENT TRACK]` paragraph secretly re-deriving organizational evaluation mechanics?
8. **Tables:** lead-in sentence present, no blank cells, code-tick usage consistent with prose, cross-reference formatting followed inside cells?
9. **Figures:** every figure has a caption with an evidence-class tag; every pending figure uses the `[FIGURE PENDING]` blockquote and is logged in `VISUAL-INVENTORY.md`; every Mermaid block has (or is tracked toward) a paired rendered image?
10. **Home-lab flag check:** every reference to a project the planned SOC Home Lab Handbook would eventually own uses the `[HOME LAB — companion volume not yet written]` flag and carries enough stand-alone detail to attempt now, per §4's rule?
11. **Scope-boundary check (this book's own version of the depth check):** does this unit re-derive the SOC Manager's Operating Handbook's competency-matrix mechanics, promotion-committee process, or hiring-loop design instead of citing them and pivoting to the individual's own preparation? This is the single most important item on this list, given the book's entire reason for existing.

Match this guide over inventing local precedent. Any deviation a reviewer approves gets recorded as a documented change to this file, not silent local drift.
