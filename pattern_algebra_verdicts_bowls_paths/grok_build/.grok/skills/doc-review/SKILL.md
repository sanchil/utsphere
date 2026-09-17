---
name: doc-review
description: >
  Review and evaluate a document, design note, or attached file.
  Use when the user says review this document, evaluate this write-up,
  critique this design, or assess this spec.
when-to-use: document review, evaluate this, critique this doc, review the attached file
argument-hint: "[path or paste]"
user-invocable: true
metadata:
  short-description: Review and score a document
---

# Document review

Read the target document first (path, paste, or @file).
If none is given, ask which file.

Use AGENTS.md as the constitution when it exists.

## Output format (always use this shape)

### Verdict
One of: **Ship** / **Revise** / **Reject**

### One-sentence summary
What the document is trying to do.

### What works
3–6 concrete strengths. Quote or point to sections.

### What is weak
Gaps, contradictions, hand-waving, missing definitions.
Each item: problem → why it matters → how to fix.

### Philosophy check
- Can a careful beginner explain the core idea in one sentence?
- Does each new idea change a decision, or is it decoration?
- What simpler alternative already exists?

### Score (1–5)
| Axis | Score | Note |
|------|-------|------|
| Clarity | | |
| Coherence | | |
| Evidence | | |
| Usefulness | | |
| Simplicity | | |

### Next edit
The single highest-leverage change. Not a laundry list.

## Rules
- Do not rewrite the whole document unless asked.
- Do not invent facts the text does not support.
- Prefer short, sharp comments over polite padding.