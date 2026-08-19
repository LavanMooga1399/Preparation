# Note Generation Workflow

This file is the step-by-step process for turning one syllabus concept into a finished note file. It exists so that every note — regardless of which topic or which session produced it — goes through the same discipline. The two files in `UPSC-CSE/PROMPTS/` are contracts, not inspiration: follow them section-by-section rather than approximating their spirit.

## Which prompt governs which deliverable

- **`CLAUDE_SYLLABUS_ANALYSIS_GENERATOR_PROMPT.md`** — used once per GS paper (or per major sub-paper) to produce the paper-level syllabus-and-strategy file (see `UPSC_GS2_Syllabus.html` for the reference output). Produces the cluster breakdown, weightage, two-track routine, and priority ladder that everything else in that paper hangs off.
- **`CLAUDE_NOTES_GENERATOR_PROMPT.txt`** — used for every individual concept note (the level this workflow is mainly about). Produces one self-contained, print-friendly HTML file per concept.

## Step-by-step process for a concept note

1. **Locate the concept inside the syllabus tree.** Confirm which cluster and which numbered topic (per the paper's syllabus-analysis file) the concept belongs to, and which comma-separated element of that topic's official syllabus line it corresponds to. Quote the syllabus line verbatim in the note's Section 01 — never paraphrase it.
2. **Decide merge vs. separate file.** Apply the test in `FOLDER_AND_FILE_STRUCTURE.md`: one continuous narrative arc stays in one file; genuinely distinct examinable units get their own file, even if the syllabus lists them on the same line.
3. **Research before writing — against all six sources, not one.** Run the source-coverage contract in `TEST_INTELLIGENCE.md` Part 3B: (i) the weekly plan's "Important Topics" column *plus its adjacent surface*; (ii) the corresponding **Laxmikanth chapter, sub-heading by sub-heading, targeting 100% representation**; (iii) the **Bare Act** at clause level (Art 75(1A) ≠ 75(5)); (iv) **judgments from the last ~18 months**, searched at write-time — never assume the textbook position still holds; (v) **schemes, statutes and Bills in the news**, with their Article mappings; (vi) **genuine verified PYQs**. For dynamic topics verify figures, missions, reports and office-holders by search; for heavy-static topics prioritise foundational accuracy and standard framing; flag explicitly anything that could not be independently verified.
   - **The four explanatory layers.** Beyond facts, every note carries: a **recent-judgment layer**; a **concept-behind-the-article layer** (Art 14 is not its text — it is reasonable classification, arbitrariness and substantive equality); **Constituent Assembly debate ammunition** for any "do we need this institution?" question; and **pros/cons/way-forward** framing for any law or reform in the news.
   - **Story + flowchart for anything sequential.** A case saga, amendment battle or institutional evolution gets BOTH a narrative telling in the `📖` mentor-box register AND a compact timeline/flowchart SVG of the same beats. Story builds understanding; the figure builds recall. Reference implementation: the 2025 Governor assent saga (Topic 6, Note 01).
   - **A fact stated only inside an answer key does not count as covered** — it must live in the note's teaching body.
4. **Verify every PYQ before it is written down.** Search for the exact question, year, and stage. If it cannot be confirmed from a real source, it does not go into bucket (A) or (B) — either drop it or move it honestly into bucket (D) as a labelled practice question. This is the single most failure-prone step and is never skipped.
5. **Build the note to the template**, in this order: syllabus placement and logical chain → mains-oriented prose with a dedicated 🔴 Prelims block per concept → model intro line plus 2–3 value-additions → timeline/number anchors, competing views, and traps called out explicitly → PYQ analysis in the four labelled buckets (A direct, B adjacent, C where marks go, D expected/practice-only) → a dark one-page recall sheet at the very end.
6. **Reuse the established design system** rather than inventing a new one per file: Fraunces (display) + Inter (body) + IBM Plex Mono (data/labels); deep-indigo hero with gold/nebula/teal accents; the CSS classes already defined in existing note files (`.mentor`, `.prelims`, `.tip`/`.trap`, `.pyq`, `.recall`, `.series`). Visual consistency across the whole prep set matters more than novelty per file.
7. **Hand-author the required visuals**: a flowchart for any process/sequence, a nested/hierarchy diagram where containment or scale matters, a Venn diagram for any commonly-confused pair, and an infographic/annotated diagram for anything else that needs a signature visual. No external images — SVG only, numbered with a one-line caption stating the single thing to remember. **Every note carries at least two figures** — the built notes run 2–4. When laying one out, leave a clear band between the title and the first drawn element (a 16px title needs roughly 20 units of clearance below its baseline before anything else starts), and **verify the result with the geometry check in the ritual below** — a figure is not finished until it has been measured in a browser.
8. **Run the verification pass**: confirm no fabricated PYQs, confirm HTML tag balance (section/div/svg/table/figure open and close counts match), confirm the mentor tone rules in `AGENT_MENTOR_PERSONA.md` are followed (no filler, no casual address terms), and confirm the file is placed and named per `FOLDER_AND_FILE_STRUCTURE.md`.
9. **Build the question gauntlet per `TEST_INTELLIGENCE.md` Parts 4 and 4B.** Every note ships with:
   - a **bucket (A) of genuine, verified PYQs** with year and stage — a note with zero genuine PYQs is incomplete;
   - a **bucket (B) of ≥8 practice MCQs** in the observed weekly-test formats, deliberately over-weighting the measured weak ones (**≥2 negative-phrased, ≥2 "how many of the above", ≥1 assertion–reason, ≥1 pairs-matching**, remainder statements/direct), each keyed to a section of the note;
   - **≥1 Mains question with a model-answer skeleton.**
   - **Presentation is part of the requirement:** full exam layout (stem → numbered statements → instruction → four visible options), answers hidden until the learner clicks an option, verdicts naming the option letter, and every option set verified to contain the correct answer. See Part 4B for the full rules and the bugs they exist to prevent.
   The note's content must also carry the deep-reference layer (case law, scheme→Article mappings, statutory sections, exact numbers) at the depth calibration in Part 2 — if a fact would plausibly appear in the test's answer-key explanation, it goes in the note now, not after the test exposes the gap.
10. **Update the series pointers.** Every note in a multi-file topic carries a `.progress` tracker (which notes in the topic exist, which are pending) and a `.series` footer note (previous/next file). When a new note is added, update the tracker and footer in its siblings too, so the series stays internally consistent without needing a master index file.
11. **Draft in the scratchpad, finalise in Prep.** Build and validate the file outside the user's folder first; copy it in only once the verification pass is clean, since files placed in the user's folder cannot be silently renamed or deleted later.

## Before each weekly test

Run the pre-test drill defined in `TEST_INTELLIGENCE.md` Parts 4–5: a full-length 50-question mock in the exact test format (+2/−0.66, 60 minutes, self-scoring, one deliberate duplicate pair, resettable for retakes with optional shuffle), taken under timed conditions at least one day before the real test. Also run the **two-pass coverage check** (Part 5): literal schedule items, then the adjacent surface around them. After the test, run the postmortem loop before planning any new notes.

## After every weekly test — the post-test loop (mandatory, unprompted)

A result PDF arriving in a week's folder is itself the instruction. Run `TEST_INTELLIGENCE.md` **Part 5** in full before planning any new notes:

1. Parse the paper per question — format, verdict, key, time on screen.
2. Compute score ÷ class average and the gap to the topper, not the raw score alone.
3. Strict per-question fact probes on every question lost; report **covered versus genuine gap**.
4. Patch every genuine gap into the **topic note** the same day.
5. Write `Week N Test Analysis.html` — every lost question, the pattern layer, and four behavioural changes.
6. Where a Mains paper exists, write `Week N Mains Answers.html` with model answers to the `MAINS_ANSWER_CRAFT.md` standard.

Only after all six does the next week's note-building begin. A week's notes written before its predecessor's postmortem repeats the predecessor's mistakes.

## The verification ritual (run after every batch of edits — no exceptions)

Scripted, not eyeballed. Every one of these has caught a real defect in this project:

1. `html.startswith("<!DOCTYPE html>")` on every touched file.
2. **Tag-balance check** with a stack parser and a VOID-element set, run on the file *with `<script>` bodies stripped* (JS comparison operators otherwise register as tags). This caught a stray unclosed `<div>` mid-edit.
3. `node --check` on every `<script>` block.
4. **Persona check** — case-insensitive absence of forbidden address terms.
5. **Question-bank audit** — per note, count MCQs by format and confirm the Part 4 minimums; confirm every question has visible options and a letter-naming verdict.
6. **Coverage audit after any test** — per-question *fact probes* against the notes corpus (never aggregate keyword similarity, which produces false passes; see Part 3's audit-method note).
7. **Figure-geometry check — measured in a real browser, never estimated.** Run `python3 AI_KNOWLEDGE_BASE/verify_figures.py`. It opens every note in headless Chromium, reveals all tabbed sections so hidden figures lay out, and calls `getBBox()` on each `<text>` element to catch two things: text escaping the `viewBox`, and text drawn on top of other text.
8. **CSS class audit** — every class used in the markup must be defined in the file's own `<style>` block. The same script reports undefined classes alongside the figure results.

**Why 7 and 8 exist, since both defect families survive checks 1–6 untouched.** A figure can be perfectly valid markup and still position a heading straight through a box: in Topic 9's consumer-tiers figure the title sat at `y=24` while the Supreme Court box spanned `y=16–50`. DOCTYPE, tag balance, `node --check` and SVG well-formedness all passed. Separately, a class that exists nowhere in the stylesheet gets **silently ignored** by the browser — `class="cards"` (never defined; the real class is `.grid`) collapsed a card grid into full-width bars, and `tcprogress-*` instead of `tc-progress-*` turned a rounded progress pill into a bare square. Nothing in the markup is malformed in either case, so only rendering or a class-vs-stylesheet diff will find them.

**Do not replace the browser measurement with arithmetic.** A first attempt estimated text width from character count × font size. It reported eight figures as overflowing — **all eight were false positives** — and it *missed* a genuine label collision in the High Court writs figure. Proportional fonts cannot be measured by counting characters. Rendered geometry is the only check that counts.

## When asked to continue a topic

Default to the next unbuilt concept in the topic's own sequence (driven by the paper's syllabus-analysis file and, where one exists, an external day-wise study plan such as `Week 1 Plan`). Do not skip ahead or reorder without saying so.
