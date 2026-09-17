---
name: philosophy-review
description: >
  Weigh an idea against the project constitution in AGENTS.md.
  Use when the user wants a philosopher take, simplicity check,
  or "should we even build this".
when-to-use: philosopher, weigh this idea, is this too complex, constitution check
argument-hint: "[idea or file]"
user-invocable: true
disable-model-invocation: false
metadata:
  short-description: Test an idea against AGENTS.md
---

# Philosophy review

Read AGENTS.md first, then the idea.

Answer only:

1. **One-sentence restatement** of the idea.
2. **Decision it changes** — trade / no-trade / hold / none.
3. **Simpler cousin** that already exists (or "none").
4. **Verdict:** Keep / Simplify / Drop.
5. **If Keep:** the smallest next proof (log it, compare to ATR, etc.).

No implementation unless asked.