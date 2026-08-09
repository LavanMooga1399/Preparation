# UPSC CSE Prep — System Overview

This is the entry point to the knowledge base for this preparation project, kept in `AI_KNOWLEDGE_BASE/` at the root of the Prep folder, separate from the actual exam content in `UPSC-CSE/`. It explains how the folder is organised, how notes get generated, and where to look for the other reference documents. Read this first; the other four files go deeper on one aspect each.

## The seven knowledge-base files

- **PREP_SYSTEM_OVERVIEW.md** (this file) — orientation and index.
- **AGENT_MENTOR_PERSONA.md** — the mentor role, tone rules, and non-negotiables Claude follows in this project.
- **NOTE_GENERATION_WORKFLOW.md** — the concrete step-by-step process for turning a syllabus line into a finished note file, and which prompt in `PROMPTS/` governs which deliverable.
- **FOLDER_AND_FILE_STRUCTURE.md** — the naming and foldering convention, with the worked Topic 1 example.
- **PREPARATION_STRATEGY.md** — the big-picture orientation: how the syllabus is decomposed into subjects, clusters, topics, and concepts, and how that maps to a study plan.
- **MAINS_ANSWER_CRAFT.md** — the standing method for writing Mains answers: the examiner's real reading behaviour, the scoring model, the directive-word table, the six GS-II question archetypes, the value-addition arsenal, time/word discipline, and a self-scoring rubric. **Binding on every model answer written in this project.**
- **TEST_INTELLIGENCE.md** — the living intelligence file built from actual weekly-test postmortems: the test-maker's question formats and depth calibration, Lavan's measured error patterns with countermeasures, the mandatory question-gauntlet requirements for every note, and the weekly postmortem loop. **Binding on every note generated from Week 3 onward** — updated after every test.

## Orientation, in one paragraph

The exam is approached top-down: paper → cluster → topic → concept. A GS paper's official syllabus is first decomposed into thematic clusters (see the syllabus-analysis files), each cluster into its named topics, and each topic into the smallest examinable concepts — the level at which an actual note file gets written. This mirrors how the syllabus itself is worded (each topic line is usually a comma-separated list of concepts) and how standard reference books (NCERT, Laxmikanth) chapter their material.

## Current state of the Prep folder (as of this writing)

- `UPSC-CSE/GS Paper I/Geography/` — one finished concept note (Origin of the Universe).
- `UPSC-CSE/GS Paper II/CLAUDE_NOTES/` — syllabus-and-strategy file for the whole paper, plus four cluster folders (Polity & Constitution, Social Justice, International Relations, Governance). Polity & Constitution has a `Topic 1 - Indian Constitution/` subfolder with the first concept notes in progress.
- `UPSC-CSE/GS Paper II/Week 1 Plan/` — an external day-wise study plan (NCERT/Laxmikanth chapter references) used as one input for sequencing which concept gets written up next.
- `UPSC-CSE/PROMPTS/` — the two reusable generator prompts that govern note quality and structure. Treat these as contracts, not suggestions — see `NOTE_GENERATION_WORKFLOW.md`.
- `UPSC-CSE/Resources/` — third-party PDFs/decks (PYQ compilations, AI-prompt libraries) used as research aids, not as note content to copy verbatim.

## Ground rule that shapes everything else

Do not merge unrelated concepts into one file for convenience, and do not fragment one continuous idea into artificial pieces either. The test is: can this be revised as a single sitting, and does splitting it lose the narrative thread? If yes to both, it is one file. Otherwise, split. See `FOLDER_AND_FILE_STRUCTURE.md` for the worked example.
