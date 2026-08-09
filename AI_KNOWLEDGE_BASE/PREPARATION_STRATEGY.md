# Preparation Strategy & Orientation

This file is the big-picture map: how the exam gets approached from "here is a syllabus PDF" down to "here is today's revision file." It is the reasoning behind the folder structure and workflow described in the other knowledge-base files, not a duplicate of them.

## The decomposition chain

1. **Paper.** Start at the level of a GS paper (Prelims GS, Mains GS-I through GS-IV, Optional). Each paper gets one syllabus-and-strategy file (via `CLAUDE_SYLLABUS_ANALYSIS_GENERATOR_PROMPT.md`) before any topic-level notes are written — know the terrain before marching into it.
2. **Cluster.** Within a paper, group the syllabus into a small number of thematic clusters named from the paper's own language, not generic labels. For GS-II: Polity & Constitution, Social Justice, International Relations, Governance. Each cluster gets a rough, honestly-labelled "directional" weightage and a static-vs-dynamic character call.
3. **Topic.** Each cluster decomposes into the paper's own numbered syllabus topics (nine, for GS-II's Polity & Constitution cluster). This numbering is preserved everywhere — in folder names, in note file headers — so a note's place in the whole syllabus is never ambiguous.
4. **Concept.** Each topic decomposes further into the smallest examinable units — the level at which an actual note file exists. A topic's official syllabus line is usually itself a comma-separated list of these units; where it isn't, an external study plan (chapter-by-chapter from NCERT/Laxmikanth, or a structured week-plan) supplies the breakdown instead.
5. **Note.** One concept, one file, built to `CLAUDE_NOTES_GENERATOR_PROMPT.txt` and placed per `FOLDER_AND_FILE_STRUCTURE.md`.

## Where sequencing comes from

- **Syllabus-first** for clusters and topics — the paper's own syllabus wording and order.
- **Study-plan-driven** for the day-to-day sequence of concept notes within a topic, where an external plan exists (for example, `GS Paper II/Week 1 Plan/` sequences Topic 1's concepts as: Historical Background + Making of the Constitution → Salient Features + Preamble → Union & Territory + Citizenship → Amendment + Basic Structure → Fundamental Rights, across a 7-day week culminating in a revision day).
- **PYQ-frequency-driven** for prioritisation within that sequence — a concept confirmed as a recurring repeater gets proportionally more depth and a richer PYQ section than one confirmed as low-yield. Low-yield is stated honestly, not padded to look thorough.

## The six-lens method (for any new paper or topic)

When a new paper or major topic is opened up for the first time, apply this decomposition explicitly (this is the method baked into the syllabus-analysis prompt):

1. Decompose each syllabus line into its smallest examinable units.
2. Cluster the units into natural thematic families, named from the paper's own title where possible.
3. Weight each cluster by rough, directional mark-share (never presented as an official figure).
4. Classify each cluster static (book-answered) vs dynamic (newspaper-answered).
5. Spot the 3–4 repeaters/annual magnets in each cluster.
6. Map overlaps across GS papers, Essay, and interview — a single well-covered concept (for example, RTI) often pays across Polity, Governance, and Social Justice simultaneously, which is why depth on the core repeaters is worth more than breadth across every listed sub-point.

## Revision cadence

- Each concept note ends in a one-page, print-friendly recall sheet — the artifact meant for last-mile revision, not the full note.
- A topic's note series (see `FOLDER_AND_FILE_STRUCTURE.md`) is designed to be revisable individually (open just the one concept that's weak) or as a set (open all files in a topic folder in sequence for a full topic revision pass).
- Current affairs integration happens at the concept level, not bolted on afterward: dynamic topics get their figures/reports/office-holders verified at write-time, and a note is flagged if a claim could not be independently confirmed rather than left in with false confidence.

## What "brainstorming a new topic" looks like in practice

1. Confirm the topic's position in its cluster (number, official wording) from the paper's syllabus-analysis file.
2. Check whether an external study plan already sequences that topic's concepts; if not, decompose it manually using the six-lens method above.
3. Decide merge-vs-split per concept using the test in `FOLDER_AND_FILE_STRUCTURE.md`.
4. Hand off to the note-generation workflow for each concept in turn, one file at a time, keeping the series pointers in sync.
