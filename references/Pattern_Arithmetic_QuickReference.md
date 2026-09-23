# Pattern Arithmetic — Quick Reference
*Extracted from Pattern_Arithmetic_v15_15. Section numbers refer to that document.*

**Changes since the v15_11 edition of this reference:** the introduction now opens with a stated Thesis (§0 below); $T$'s dimensional generalization is joined by an equivalent one for Offset's transport, both verified rather than merely claimed, up to $N_{\mathrm{dim}}=50$; and the Enclosure gained a fourth named convention, the allowance $\epsilon_{\text{allow}}$, for treating nearby checkpoints as the same freeze.

---

## 0. The Thesis (context, not a formal rule)

The introduction now states the paper's governing idea directly, before any axiom:

> *Mathematics need not be performed on numbers alone. Wherever a domain supplies a unit of truth and a small set of rules by which such units combine, obeyed consistently, the unit and its rules together form an arithmetic of that domain.*

Color, musical notes, Chladni figures, valence chemistry, and the mitochondrion (joined without dissolving — a natural-world instance of Assembly) are offered as *evidence* that such arithmetics exist elsewhere, not as domains this paper models. Ice's six-fold growth is named as one such domain arithmetic in its own right — and, by Axiom 0, exactly the kind refused a map onto this paper's sphere. This paper states its own rules as axioms rather than discovering them; the "settle toward stability" half of the thesis appears only in miniature, in the Enclosure (§9).

---

## 1. The Axioms

| # | Name | One-line summary |
|---|---|---|
| **0** | Admissibility of Sorts | Before any operator can be used, a sort $\tau$ must earn the right to a geometric reading — the table of who-may-use-what operators comes *after* this, not instead of it. |
| **1** | The Normalized Unit Truth State ($r\le1$) | A pattern is one typed point, not a field: $x=(r,\hat n,\chi,\tau)$, $r\in[0,1]$, $\hat n\in S^2$, $\chi\in[0,2\pi)$. A bowl is a separate finite set of such atoms. |
| **2** | The Absolute Null State ($r=0$, Black) | Vanishing strength means direction and phase are unused — an empty seat, not a field that happens to be zero everywhere. |
| **3** | Saturation (White) | The upper pole of the same bounded stage, not an infinite norm. Reached either as a single full-spectrum identity or as a bowl with many directions filled — neither pushes any single arrow past $r=1$. |
| **4** | Gather and Remove ($\oplus$, $\ominus$) | $\oplus$ is set union on bowls — it collects, it does not blend: $A\oplus A=A$. $\ominus$ removes one member. Set union needs no dimension, so this is unaffected by anything below. |
| **5** | Mix as a Reading ($\boxplus$) | A phasor operator: combines $\chi$ among states that already share a direction $\hat n$. Reads a bowl into one blended state; never moves an arrow onto a new axis. Lossy and non-associative under the cap — see §3 below. Dimension-blind wherever it applies, since it never leaves the shared axis. |
| *(unnumbered)* | Rotation preserves the unit | $\mathbf{R}\in\mathrm{SO}(3)$ turns $\hat n$, leaves $r,\chi,\tau$ untouched. The geometric engine $T$ is built from, not a second kind of blend. |
| **6** | Assembly ($\bowtie$) | The fourth verb: given two intact units, how strongly do they belong together and where do they touch? $A\bowtie B=(A,B,\kappa_{AB},U_{AB})$ — both units survive unchanged; nothing is fused. Never repels in any dimension: the alignment bracket $3+\hat n_A\cdot\hat n_B$ stays in $[2,4]$ regardless of $N_{\mathrm{dim}}$. |
| **7** | Informational Vectors & Derived Per-Atom Metrics | An atom may be a *bundle* of $N$ informational vectors rather than one — still teaching atoms under one closure, not a new species of unit. Defines $V_{\text{derived}}$ and the seven scalar metrics of §3. |

**Two further operators are built on these axioms but are not themselves axioms — both now generalize beyond three dimensions, verified rather than merely claimed:**
- **Transform ($T$)** — §3.4: an actor $w$ rotates an occupant $x$ about $w$'s own axis by $\alpha(r_w)=\pi r_w$. Beyond $N_{\mathrm{dim}}=3$, the actor's bundle supplies $N_{\mathrm{dim}}-2$ mutually orthogonal arrows to fix the axis (see the ladder in §3 below); checked invertible and non-commutative up to $N_{\mathrm{dim}}=50$, exact at $N_{\mathrm{dim}}=3$.
- **Offset** — §4.1: plants a new seat from three seats via log/exp/transport. The transport is now written for general dimension too: a rotation within the plane the two seats themselves span, needing no bundle, exact at $N_{\mathrm{dim}}=3$ against the original cross-product form.

---

## 2. Original Metrics — the base unit (Axiom 1)

The four coordinates of a single teaching atom. Nothing here is derived from anything else; every other quantity in this paper is built from these.

| Symbol | Domain | What it answers |
|---|---|---|
| $r$ | $[0,1]$ | How strong / how confidently held is this unit? |
| $\hat n$ | $S^2$ (equivalently $(\theta,\phi)$) | What direction — the semantic address? |
| $\chi$ | $[0,2\pi)$ | What internal phase/mood/hue? |
| $\tau$ | $\{\mathtt{word},\mathtt{num},\mathtt{color},\ldots\}$ | What sort — which operators may legally act on it? |

$N=1$ is the default: one atom, one arrow. Axiom 7 is what allows $N>1$.

---

## 3. Derived Metrics — built from the base unit (Axiom 7)

All of these presuppose a **bundle**: $N$ informational vectors $v_i=r_i\hat n_i$, each an instance of the Axiom 1 unit, held under one closure.

| Symbol | Formula | What it measures | Requires |
|---|---|---|---|
| $V_{\text{derived}}$ | $\displaystyle\sum_{i=1}^N v_i$ | The raw, **uncapped** vector sum of the bundle. Reads as an effective $(r,\hat n)$ pair when a single vector is needed — but is *not itself a unit* and needs a cast before acting as $T$'s actor $w$. | any $N\ge1$ |
| $S_{\text{atom}}$ | $\displaystyle\sum_i r_i$ | **Atom strength.** The correct denominator for atom-level coherence, $\lvert V_{\text{derived}}\rvert/S_{\text{atom}}$. | any $N$ |
| $\mathcal{V}_{\text{atom}}$ | $\displaystyle\sum_i r_i^3$ | **Atom volume.** Strictly $<S_{\text{atom}}$ whenever any $r_i<1$ — a forced consequence of the cap, not an assumption. | any $N$ |
| $\gamma_{\text{atom}}$ | $\mathcal{V}_{\text{atom}}/N$ | **Mean vector volume.** Average per-vector share of the total. | $N\ge1$ |
| $\mathcal{E}_{\text{atom}}$ | $\displaystyle\sum_i r_i^2$ | **Information energy.** Stands on its own (not squared strength) — the bundle's intrinsic energy *before* asking how its vectors align. | any $N$ |
| $\alpha_{\text{atom}}$ | $\dfrac{\sum_{i<j} r_ir_j(\hat n_i\cdot\hat n_j)}{\sum_{i<j} r_ir_j}$ | **Internal alignment.** Strength-weighted mean cosine similarity across all pairs — separates active cancellation ($<0$) from mere non-reinforcement, which coherence alone cannot. Checked at $N_{\mathrm{dim}}=5,20$ as a dot-product identity: dimension does not enter it. | $N\ge2$ |
| $\sigma_{\text{atom}}$ | $\dfrac{N^2}{N-1}\operatorname{Var}(s_1,\ldots,s_N)$, $s_i=r_i^3/\mathcal{V}_{\text{atom}}$ | **Volume concentration.** $0$ when spread evenly, $1$ when one vector holds it all, at every $N$. | $N\ge2$ ($:=0$ at $N=1$) |
| $\sigma_{\text{shell}}(w)$ | $\dfrac{K^2}{K-1}\operatorname{Var}(p_1,\ldots,p_K)$, bins of width $w$ (default $0.1$) | **Shell concentration.** Catches a blind spot $\sigma_{\text{atom}}$ has by construction: many vectors independently landing at the same magnitude. | needs $\ge2$ occupied shells ($=1$ at $K=1$) |

**The dimension ladder** (§3.4) — how many arrows a bundle needs before it may act as $T$'s actor $w$ beyond three dimensions:

| Space | Sphere | Fixed part (the "axis") | What turns |
|---|---|---|---|
| $\mathbb{R}^2$ | $S^1$, a circle | a point, dimension $0$ | one plane |
| $\mathbb{R}^3$ | $S^2$ | a line, dimension $1$ | one plane |
| $\mathbb{R}^4$ | $S^3$ | a plane, dimension $2$ | one plane |
| $\mathbb{R}^5$ | $S^4$ | a $3$-D space, dimension $3$ | one plane |
| $\mathbb{R}^{N_{\mathrm{dim}}}$ | $S^{N_{\mathrm{dim}}-1}$ | dimension $N_{\mathrm{dim}}-2$ | one plane |

A teaching atom ($N=1$) is therefore a legal actor only at $N_{\mathrm{dim}}=3$; beyond that, the bundle must supply $N_{\mathrm{dim}}-2$ **mutually orthogonal** arrows. Verified invertible and non-commutative up to $N_{\mathrm{dim}}=50$.

---

## 4. Other named derived quantities (by operator)

For completeness — these are built *within* a specific axiom/operator rather than being general per-atom metrics.

| Symbol | Formula | Lives in | What it is |
|---|---|---|---|
| $U_{AB}$ | $-\dfrac{r_Ar_B}{2}\cdot\dfrac{3+\hat n_A\cdot\hat n_B}{(d_{AB}^2+\varepsilon_{AB}^2)^{3/2}}$, $\varepsilon_{AB}=r_A+r_B$ | Axiom 6 | Assembly's interaction energy. Always $<0$ for nonzero strengths — never repels, in any dimension. |
| $\kappa_{AB}$ | $\hat n_A+\hat n_B$ (unnormalized) | Axiom 6 | Assembly's contact point; defined at every angle, including antipodal ($=\mathbf 0$). |
| $\alpha(r_w)$ | $\pi r_w$ | §3 (Transform) | Maps an actor's strength to a rotation angle; full strength ($r_w=1$) gives a $180°$ turn. |
| $z_B$, $\boxplus(B)$ | $\sum_{x\in B} r_xe^{i\chi_x}$; result $=(\min(1,\lvert z_B\rvert),\hat n,\arg z_B,\tau)$ | Axiom 5 | Mix's one-step bowl reading — the reason binary Mix is non-associative under the cap. |
| $v$, transport, $\hat n_*$ | $v=\log_{\hat n_m}(\hat n_k)$; $\hat n_*=\exp_{\hat n_w}(\text{transport}_{m\to w}(v))$ | §4.1 (Offset) | The copied walk: log the source pair, transport the tangent vector, exponentiate at the new seat. At $N_{\mathrm{dim}}=3$, transport is the original cross-product rotation about $\hat n_m\times\hat n_w$; in general, it is a rotation within the plane $\hat n_m,\hat n_w$ themselves span — the two seats name the turning plane, so no bundle is needed. The two forms agree exactly at $N_{\mathrm{dim}}=3$. |
| $F_i$ | $-\nabla_{\vec P_i}\sum_{j\ne i}U_{ij}$ | §9 (Enclosure) | Force on a seated unit — descended without mass or momentum. |
| freeze condition | $\max_i\lvert F_i\rvert<\eta$ | §9.2 (Enclosure) | A configuration below threshold $\eta$ is a *checkpoint*: it may be frozen and taken as the accepted solution — not exact rest, since the pull never reaches zero at finite distance, so left longer every configuration drifts toward one pile. |
| $\vec P_{c,k}$ | $\dfrac{\sum_{i\in G_k} r_i\vec P_i}{\sum_{i\in G_k} r_i}$ | §9.3 (Enclosure) | A camp's body — the strength-weighted centre of its members, read *after* motion, not sought during it. |
| $\epsilon_{\text{allow}}$ | (named, not derived) | §9.3 (Enclosure) | **Allowance.** Two checkpoints whose bodies differ by less than $\epsilon_{\text{allow}}$ are read as the same freeze; a fourth named convention alongside $\eta$, $\delta$, and the census cut — not a truth of $U_{AB}$. A camp read this way is still only a checkpoint on its members, never a new unit in its own right. |

---

*This reference is a summary aid only; the equation numbers and full derivations live in Pattern_Arithmetic_v15_15.tex.*
