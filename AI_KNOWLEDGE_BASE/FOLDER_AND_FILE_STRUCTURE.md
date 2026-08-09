# Folder & File Structure Convention

This file fixes how syllabus lines map to folders and files, so the same judgement call is not re-litigated for every new topic. It exists because cramming unrelated concepts into one growing file makes revision harder, and over-splitting a single continuous idea makes it harder too — the goal is one file per genuinely separate examinable unit.

## The merge-vs-split test

Before creating a file, ask both questions:

- Can this be revised in a single focused sitting without losing the thread?
- Does splitting this concept in two lose a narrative or logical dependency (does part 2 only make sense once part 1 is fresh)?

If both answers are yes, keep it as one file. If either answer is no, split it. This is why, for example, "historical underpinnings" and "evolution" (the Constituent Assembly's work) share one file — the second literally cannot be explained without the first — while "features" and "amendments" do not share a file with them, even though all four sit on the same official syllabus line.

## Top-level layout

```
AI_KNOWLEDGE_BASE/                  the five methodology files (this one included) — meta-documentation, not exam content
UPSC-CSE/
  GS Paper I/
    <Subject>/                      e.g. Geography
      <Concept note>.html           one file per concept, flat (no sub-numbering needed yet at this size)
  GS Paper II/
    CLAUDE_NOTES/
      UPSC_GS2_Syllabus.html        paper-level syllabus + strategy (from CLAUDE_SYLLABUS_ANALYSIS_GENERATOR_PROMPT.md)
      <Cluster name>/                e.g. Polity & Constitution, Social Justice, International Relations, Governance
        Topic N - <Topic name>/      one subfolder per numbered syllabus topic, created once that topic has 2+ note files
          01 <Concept>.html
          02 <Concept>.html
          ...
  PROMPTS/                          the two generator prompts — do not duplicate copies elsewhere
  Resources/                        third-party reference material (PDFs, decks) — not edited, only read
```

## Naming rules

- Topic subfolders: `Topic N - <Topic name in Title Case>`, where `N` matches the topic's position in that cluster's syllabus list (see the cluster's section in the paper's syllabus-analysis file).
- Concept files inside a topic subfolder: `NN <Concept name in Title Case>.html`, zero-padded two-digit prefix, in the order they should be revised (which usually follows the order of an external study plan, where one exists, or the natural logical chain otherwise).
- A topic with only one concept file does not need its own subfolder yet — leave it flat in the cluster folder until a second concept file is added, then create the subfolder and move both in.
- File names, once created in the user's Prep folder, are effectively permanent (the platform will not silently rename or delete them). Decide the final name before writing the file rather than renaming later.

## Worked example: Polity & Constitution, Topic 1 — Indian Constitution

Official syllabus line: "Indian Constitution — historical underpinnings, evolution, features, amendments, significant provisions and basic structure." Six comma-separated elements, mapped to seven files because "significant provisions" itself bundles multiple distinct examinable units:

1. `01 Historical Underpinnings and Evolution.html` — merged (one continuous narrative: colonial acts → Constituent Assembly).
2. `02 Salient Features and the Preamble.html` — merged (the Preamble is the Constitution's own statement of its features).
3. `03 Union and its Territory.html` — planned.
4. `04 Citizenship.html` — planned (kept separate from #3 despite both falling under "significant provisions" — they are distinct examinable units with their own PYQ history).
5. `05 Amendment of the Constitution.html` — planned.
6. `06 Basic Structure Doctrine.html` — planned (kept separate from #5 — amendment procedure and the basic structure limits on it are related but independently testable).
7. `07 Fundamental Rights.html` — built.
8. `08 Directive Principles of State Policy.html` — built (split from Fundamental Rights into its own file, consistent with the Citizenship/Union & Territory precedent — DPSP is a distinct examinable unit with its own PYQ history and Art. 31C conflict arc).
9. `09 Fundamental Duties.html` — built (split from DPSP into its own file for the same reason — Part IV-A has a distinct origin story (Swaran Singh Committee, 42nd Amendment) and PYQ pattern). This closes out Topic 1's note series (00–09).

## Cross-linking within a series

Every file in a multi-file topic includes a `.progress` tracker near the top (which notes exist, which are pending) and a `.series` note near the bottom (previous/next file by name). These are kept in sync across sibling files whenever a new note is added to the series — see `NOTE_GENERATION_WORKFLOW.md`, step 9.
