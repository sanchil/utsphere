% =====================================================================
% TODO -- MASTER PUNCH LIST (v14_24 review pass, keep until resolved)
% =====================================================================
% Status note: the structural problems from earlier drafts (state vs.
% field conflation, Axiom 3's S=infinity, the missing Mix phase rule,
% the offset operator's 1-D-only demo, and the empty Discussion
% section) are RESOLVED as of v14_19/v14_24 and verified by hand/code
% during review. What remains below is narrower: naming precision and
% a couple of claims that are asserted but not yet spelled out as
% equations, plus one framing tension worth a decision.
% =====================================================================

Target Document: Pattern_Arithmetic_v14.26.tex

TASK 1: DONE
% [U1] RESOLVED in Pattern_Arithmetic_v14.26.tex: Mix is now
%      $\boxplus$, not $T_{\mathrm{paint}}$. Mix is a two-argument
%      reading of peer states; $T_w$ remains the one-argument
%      rotation+phase-shift. They do not compose as two ordinary $T$'s.

TASK 2: DONE
% [U2] RESOLVED in Pattern_Arithmetic_v14.26.tex: the no-doubling
%      headline is scoped to gather ($A\oplus A=A$). Axiom 5 notes
%      that Mix is not idempotent: $A\boxplus A$ gives
%      $z'=2r e^{i\chi}$, $r'=\min(1,2r)$.

TASK 3: DONE
% [U3] RESOLVED in Pattern_Arithmetic_v14.26.tex: transport_{m\to w}(v)
%      is now a numbered equation: rotate v by
%      \theta_{mw}=arccos(n_m·n_w) about (n_m\times n_w)/||n_m\times n_w||.
%      Coincident: identity. Antipodal: axis undefined, left as a
%      separate convention. The equatorial check cites the general
%      formula.
%

TASK 4: DONE
% [U4] RESOLVED in Pattern_Arithmetic_v14.26.tex: abstract and the
%      intro operator table now say division as unmixing is left open,
%      with a pointer to the existing Sec. 6 note. Inverse rotation
%      of T remains defined; a Mix inverse is not claimed.
% =====================================================================


TASK 5: DONE
% Consistency pass against the intro philosophy: different combination
% for different information, named by what it preserves.
%   - T now acts on a register occupant x, not on the bowl R
%     (pipeline, poem trajectory, storm already did this).
%   - Verb inventory includes Mix: contributions, offset wording,
%     type table column, related-work list.
%   - Title "Unit Probability Spheres" -> "Unit Truth Spheres"
%     (r is an activation, not a probability).
%   - oplus does not grow r; Mix may, until the cap (Axiom 3, T's roles).
%   - Document tape is not a poem pi; Mix is not that tape.


TASK 6: DONE


% Visible scope added: abstract (one sentence); intro
% Section~\ref{subsec:claim_scope} (the full narrow claim); higher-order
% and related-work openings; conclusion restatement. Costumes and
% boundary-drawing stay marked as such. The author SCOPE FLAG comments
% remain as edit guards.

- Read the entire document and understand its philosophy ideas and context
- Add the following scope to relevant places to make the document more honest and transparent.
- The core ideas are simple enough

% =====================================================================
% SCOPE FLAG -- read before the applications-adjacent sections below
% =====================================================================
% This paper's actual claim is narrow and should be kept narrow:
% counting (1+1=2) is not the only valid arithmetic for combining
% units of information; a combination rule should be chosen for what
% the unit IS (a count, a color, a direction, a word), not applied by
% default because it is the arithmetic everyone already knows. The
% sphere, phase, oplus/boxplus/T/offset machinery is ONE proposed way
% to make that narrow claim precise and checkable -- it is not itself
% the claim, and it is not offered as a general theory of language,
% physics, biology, or computation.
%
% Everything past the axioms that gestures at a domain --- storms,
% forests, pathogen cancellation (Sec.~\ref{sec:higher_order}), and
% the Bloch/word2vec/Transformer/RotatE/von-Mises-Fisher/Riemann-
% sphere/SO(3)/spherical-harmonics comparisons
% (Sec.~\ref{sec:related}) --- is either (a) an illustration of the
% oplus-vs-T split using borrowed vocabulary, explicitly marked
% "costume" where that is the intent, or (b) a boundary-drawing
% exercise stating what is reused vs. added against an existing
% formalism. None of it is a demonstrated model of weather, ecology,
% epidemiology, or a proposed replacement for quantum mechanics,
% embeddings, or transformers. Where a passage states this limit
% already, it should stay; where a future edit widens a "costume" or
% "related work" paragraph into a claim of real-world applicability,
% that widening needs its own evidence section, not an extension of
% the existing illustrative one.
% =====================================================================


TASK 7: DONE

Target Document: Pattern_Arithmetic_v14_34.tex
% Completeness/philosophy sync after Axiom 0:
%   - Color Mix examples now state the phasor toy-chart inclusion.
%   - Eq. admissibility is the Tier 1 test; num is a chart, not a
%     Mix/T homomorphism (clock trap).
%   - Mix on word is geometry, not a linguistic chi-reading.
%   - Inventories: Axiom 0 in contributions; Axioms 0--6;
%     table-and-chair in the costume list; grocery counting is +.