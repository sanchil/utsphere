# Companion sync to Pattern_Arithmetic_v15_28

`Assembly_v1.tex` → `Assembly_v2.tex` and `Inference_v1.tex` → `Inference_v2.tex`. Your v1 files are unchanged. The exhaustive record is `companion_sync_v15_28.diff`; this note says what kind of change each one is and what needs your eye.

| | Assembly | Inference |
|---|---|---|
| Mechanical (names, symbols, section and axiom pointers) | 11 | 30 |
| Semantic (the text now says something different because Paper 1 does) | 6 | 14 |
| Flagged for your decision | 3 | 0 |

Both compile with 0 errors and 0 undefined references; each grew by one page (Assembly 8→9, Inference 16→17); the overfull-box counts are unchanged from v1.

## What drifted, in one paragraph each

**Verb names.** Paper 1 now has Bundle `⊎` (idempotent, formerly “Gather ⊕”), Collapse `⊕` (count-preserving, new), Remove `∖`, UnCollapse `⊖`. Both companions still used Gather `⊕` and Remove `⊖`; the stack diagrams, the abstract of Inference, the film and cloud notes of Assembly, and “Gather's idempotence” all followed the old names.

**Atom structure.** “N capped arrows” and “an atom's own bundle” are now *Q informational vectors in N cores* (`D` distinct). “Bundle” is a verb, so the old noun use would now be read as the verb.

**Section and axiom pointers.** Paper 1's sections were renumbered; Inference carried eleven hard-coded section pointers, ten of them to Paper 1's old numbering (e.g. §2.7 for bowl-Mix is now §2.6; §5.6 for lexicons is now §6.6; §7.2 for unmixing is now §8.2; §3.3 for step metadata is now §4.5), plus “Axiom 6” for the walk (Axiom 6 is Assembly) and Assembly's “Axiom V4”. The eleventh (“§4.3”, to where the mechanism strains under scale) pointed at the wrong place in Inference itself; it is now a live cross-reference to the shells' section.

**Mix across differing directions is no longer open.** Inference treated it as “the companion paper's still-open case (its Future Work)”; Assembly does not mention it. Paper 1 now *refuses* it (§2.7), closed by declining. Four passages in Inference change from “still open” to “refused”, and Reading A's rotate-then-Mix is now described as keeping to that refusal. What remains open for compressing walk landings is a rotation-averaging (or other stated) rule, which Paper 1's Future Work hands to Inference.

**Multiplicity (the largest change).** Inference §8.1 argued that counting witnesses needs a separate function `m` because `⊕` was set union. Paper 1 now has Collapse, which counts. §8.1 is rewritten: witnesses are held in a Collapsed atom, `m(A)` is the number of cores of value `A`, and Bundle remains presence. The shells' table and the reference-atom construction now say their groups are Collapsed atoms (in a bowl, identical shells would share one seat and the counts in the table would be wrong).

**The substitution in Inference §2.1.** It said Axiom 1 *names this paper's own use* as the setting that should adopt the bijection. Axiom 1 actually says “a verdict accumulated from many units, say … should revisit this line”. The sentence now says that, and notes that `K=1` gives Paper 1's example.

**Assembly's parked notes for Paper 1.** “Frozen for now … held until it migrates” is out of date: the notes on what arithmetic is *for* and on precedent (Pāṇini, the chair at the table) are now in Paper 1 §1 and are marked as migrated; the note on what earns axiom status has not migrated. The status of the fourth note's comments is stated.

## For your decision (flagged in the text)

- *Film cast (Assembly):* I changed `⊕ is the cast` to `⊎ is the cast (⊕ if repeated frames must be counted)`. Which you meant depends on whether a repeated frame should count.
- *Sitting and cancelling (Assembly):* I changed “sitting is still ⊕, … cancelling is Mix … or ⊖” to “sitting is still ⊎ (⊕ where the count must be kept) … or taking a member out with ∖ (a core, with ⊖)”.
- *Camps as atoms (Assembly, added text):* a short bracketed note that Collapse is now Paper 1's verb for several atoms becoming one, so a camp read as a system-level atom is a Collapsed atom whose `V_derived` is the sum of its members' sums. It does **not** claim this equals the camp signature used in your tests.

## Left as it was, on purpose

- Every result in Assembly's development notes (the 16.0%, 69.7%, 32% against 94%, 13 against 11 systems, the tangential-force test): none of them is touched by the sync, and I did not re-run them.
- The title banner of equals signs, which overflows the margin exactly as it does in Paper 1 v15_28. It is better fixed in all three papers together.
- Assembly's draft-history phrasing (“named early in the companion paper's own development”).

## What I checked, and what I could not

- **Reproduced from Paper 1's definitions:** Inference's twinkle/little example, the 60°-then-60° landing and both pin distances (5.6°, 102.5°), the mean resultant lengths (0.9998, 0.8689, 0.11, 0.00), the `K=0.2` strengths (0.899, 0.900, 0.99999), and the transition counts (3/7, 4/7; 3/4, 1/4). All agree.
- **Could not reproduce:** Inference's direction-error simulation (2.8°, 15.1°, 29.1°, 50.7°; and 36.6° at N=2, 5.1° at N=128), because the noise model and seed are not stated; and the −0.43 against −0.50 comparison with `α_atom`. Neither was changed.

## One pending decision that would redo the pointers

If Axiom 6's energy and §10 move to Assembly (register R61), every pointer to “Axiom 6” and “§10” in both companions, and Assembly's “What Is Inherited”, would have to be redirected again. The sync here follows v15_28 as it stands.
