# Pattern Arithmetic — Quick Reference, Index and Glossary
*Extracted from Pattern_Arithmetic_v15_28. Section numbers (§) and equation numbers (eq.) refer to that document. Every number in Part 9 was recomputed from the paper's printed inputs (reproduce_v15_28.py).*


---

## 0 · The soul of the paper, on one page


> **The soul in eight paragraphs**
>
> **Thesis (§1).** Mathematics need not be performed on numbers alone. Wherever a domain supplies a *unit of truth* — the smallest thing it treats as one — and a small set of rules by which such units combine, obeyed consistently, the unit and its rules form an *arithmetic of that domain*. Counting ($1+1=2$, “how many?”) is one instance, not the only one: the word “add” names a different rule, and therefore a different kind of unit, for a colour, a note, a word.
> **The unit (Axiom 1, §2.2).** One typed point, not a field: $x=(r,\hat n,\chi,\tau)$ with strength $r\in[0,1]$, direction $\hat n\in S^2$ (a *semantic* address, not a place), phase $\chi\in[0,2\pi)$, sort $\tau$ (which buttons may be pressed). The sphere is the stage; the unit is the vector.
> **The spine (§3.1).** A *bowl* of seated units ($\uplus$) is read by a *path* ($T$) to a *result*; a result may be seated again (*levels are closed*). A unit does not know what it constitutes: **a seated word does not know the poem; the path knows it.** One bowl, several ways to read it.
> **Six verbs, six questions.** $\uplus$ *what is present?* · $\oplus$ *what is combined, nothing discarded?* · $\boxplus$ *what composite results?* · $T$ *what happens, in what order?* · offset *what walk is reused?* · $\bowtie$ *how do two units relate while both still sit?* Three have a counterpart that takes something back ($\setminus$, $\ominus$); Mix's own, $\boxminus$, is proven impossible.
> **Six laws worth remembering.** $A\uplus A=A$ · $A\oplus A\neq A$ for every $A$ · Mix is lossy and, under the cap, non-associative · $T_aT_b\neq T_bT_a$ yet $T_{w^*}T_w=\mathrm{id}$ · Assembly never repels ($U_{AB}<0$) · UnMix does not exist.
> **What it refuses, on purpose.** Mix across differing directions (declined, not left open) · UnMix · a geometric reading for any sort with no structure-preserving map (Axiom 0; most physical domains) · combining across sorts (no stated rule) · treating a costume (storm, forest, table and chair) as a model.
> **What it keeps honest.** Every law is deterministic: the same printed starting units — read at the same time, where any carries an expiry — give the same result. Every choice (the clip, $\alpha=\pi r$, $\eta$, $\delta$, the census cut, $\epsilon_{\text{allow}}$) is a *named convention*, not a truth of the algebra.
> **How an atom is counted (§2.10).** An atom is $N$ *cores* holding $Q$ informational *vectors*; $D\le N$ of the cores are distinct. Teaching atom: $N=Q=1$. Empty atom (black): $N=1$, $Q=0$. Beside its content an atom may carry *meta vectors* (time, expiry, place, links, $V_{\text{derived}}$) that describe it and are no part of what it says (§2.11).


---

## 1 · The verbs

| Verb | Question | Defining rule | Counterpart | Where |
|---|---|---|---|---|
| **Bundle** $\uplus$ | What is present? | Union on bowls: $B_1\uplus B_2=B_1\cup B_2$. Idempotent, commutative, associative; **sort-blind**; discards order and count. $A\uplus A=A$; $A\uplus B=\{A,B\}$. | **Remove** $\setminus$: $\{A\}\setminus A=\emptyset$ (empty bowl $\neq$ black $\mathbf 0$). | §2.5, eq. 5–7 |
| **Collapse** $\oplus$ | What is combined, with nothing discarded? | Keeps every core of every operand, merges none: $N=\sum N_i$, $Q=\sum Q_i$. **Not** idempotent: $A\oplus A=A^{\langle2\rangle}$. One sort per atom today; across sorts open. Each core keeps its meta vectors. | **UnCollapse** $\ominus$: returns the atom without one core; $N\to N-1$ ($N\ge2$); at $N=1$ leaves black; $Q$ falls by that core's vector count. | §3.3, §3.4 |
| **Mix** $\boxplus$ | What composite state results? | Phasor sum at a shared $\hat n$: $z'=\sum r_ie^{i\chi_i}$, $r'=\min(1,\lvert z'\rvert)$, $\chi'=\arg z'$; $\tau'=\tau$; black if $z'=0$. Over a bowl, one step: $\boxplus(B)$, $z_B=\sum_{x\in B}r_xe^{i\chi_x}$. Lossy; commutative; binary form non-associative under the cap. **Refused** across differing $\hat n$. | **UnMix** $\boxminus$: **impossible** — a Mixed result does not determine its sources. | §2.6, eq. 8–9; §3.2; §8.2 |
| **Transform** $T$ | What happens, and in what order? | $T_w(x)=\bigl(r_x,\ \mathrm{Rot}_{\hat n_w}(\alpha(r_w))\,\hat n_x,\ (\chi_x+\chi_w)\bmod2\pi,\ \tau_x\bigr)$, $\alpha(r_w)=\pi r_w$. Leaves $r_x,\tau_x$ alone. $T_{\mathbf0}=\mathrm{id}$; composition associative; $T_aT_b\neq T_bT_a$. | Inverse actor $w^*=(r_w,-\hat n_w,-\chi_w\bmod2\pi,\tau_w)$, so $T_{w^*}T_w=\mathrm{id}$. | §4.2–4.3, eq. 20, 22 |
| **Offset** | What walk is reused? | $v=\log_{\hat n_m}(\hat n_k)$; $\hat n_*=\exp_{\hat n_w}\bigl(\mathrm{transport}_{m\to w}(v)\bigr)$; $r_*=r_w$, $\chi_*=(\chi_w+\chi_k-\chi_m)\bmod2\pi$, $\tau_*=\tau_w$. Copies a walk; does not mint the name. Not $T$. | — | §5.1, eq. 29–35 |
| **Assembly** $\bowtie$ | How do two units relate while both still sit? | $A\bowtie B=(A,B,\kappa_{AB},U_{AB})$. Both operands survive unchanged; nothing is fused. $U_{AB}<0$ always: the bracket $3+\hat n_A\!\cdot\!\hat n_B$ stays in $[2,4]$. | — | §2.9, eq. 12–14 |

Schoolbook $+$ (“how many?”) lives only in `num` mode (decode, add in $\mathbb Z$, encode; §6.2). The paper reserves each verb name “the way a keyword is reserved in a programming language”: once given a meaning it is not reused elsewhere for an unrelated or informal sense (Table 1).


---

## 2 · The axioms

| # | Name | One-line content | Where |
|---|---|---|---|
| **0** | Admissibility of Sorts | A sort $\tau$ may claim a geometric $\chi$- or $T$-reading only through a map $\varphi_\tau:D_\tau\to\mathcal S$ with $\varphi_\tau(a\circ_\tau b)\approx\boxplus(\varphi_\tau(a),\varphi_\tau(b))$ or $T_{\varphi_\tau(a)}(\varphi_\tau(b))$ at a stated fidelity (**Tier 1**). **Tier 0** (`word`, `num`) is inert. An inadmissible sort (e.g. snowflake, $D_{6h}$ growth) may still be seated, at Tier 0 only. A sort absent from the table is undecided, not admitted. | §2.1, eq. 1 |
| **1** | Normalized Unit Truth State | A pattern is one typed point, $x=(r,\hat n,\chi,\tau)$, $r\le1$ a normalized activation (not a probability). A bowl is a separate finite set of such atoms. The bound is imposed by clipping — a choice, with its trade stated (not injective; $r=1$ is a value, not a limit). | §2.2, eq. 2 |
| **2** | Absolute Null State (Black) | $r=0\Rightarrow x=\mathbf0$: direction and phase unused — an *empty seat*. As an atom: $N=1$, $Q=0$. A vector of strength zero is not an arrow. | §2.3, eq. 3 |
| **3** | Saturation (White) | The upper pole of the same bounded stage: one full-spectrum name, or a saturated bowl. No unit is $r=\infty$. “Density” = many identities share the stage without overwrite. | §2.4, eq. 4 |
| **4** | Bundle and Remove | $\uplus$ collects (union, idempotent); $\setminus$ removes one member. Sort-blind: sort discipline governs what may later be *done* with a bowl, not who may sit in it. | §2.5, eq. 5–7 |
| **5** | Mix as a reading | A phasor operator: combines $\chi$ among states that already share $\hat n$; never moves an arrow. A reading returns a state and leaves the bowl intact. | §2.6, eq. 8–9 |
| — | Mix across differing directions: refused; chladni inclusion | Cross-mode coexistence is $\uplus$, not $\boxplus$: mode space is not closed under addition. Refusal is the closure — settled by declining, not by finding a rule. `chladni` is Tier 1: exact within one mode, undefined across modes. | §2.7, eq. 10 |
| — | Rotation preserves the unit | $\mathbf R\in\mathrm{SO}(3)$ turns $\hat n$ and leaves $r,\chi,\tau$: the geometric engine of $T$, not a second blend. | §2.8 |
| **6** | Assembly | Relates two intact units by a contact point and an interaction energy; never repels; completed by the enclosure's seats $\vec P$. | §2.9, eq. 12–14 |
| **7** | Informational vectors and derived per-atom metrics | An atom may hold $N$ cores of $Q$ informational vectors under one closure, each an instance of Axiom 1, all one sort. Defines $V_{\text{derived}}$, seven scalar metrics, $Q_{\text{eff}}$, the empty atom. | §2.10 |
| — | Meta vectors (not an axiom) | What an atom carries *beside* its content: uncapped, not informational, in neither $N$ nor $Q$; rides with its core. | §2.11 |


---

## 3 · The unit, its coordinates, and the counts

| Symbol | Domain | What it answers |
|---|---|---|
| $r$ | $[0,1]$ | How strong / how confidently held is this unit? |
| $\hat n$ (or $(\theta,\phi)$) | $S^2$ (higher: $S^{N_{\mathrm{dim}}-1}$) | What direction — the semantic address? |
| $\chi$ | $[0,2\pi)$ | What internal phase / mood / hue? |
| $\tau$ | $\{\mathtt{word},\mathtt{num},\mathtt{color},$ $\mathtt{note\text{-}pitch},\mathtt{chladni},\ldots\}$ | What sort — which operators may legally act on it? ($	au$ does not move the arrow.) |

| Term | Meaning |
|---|---|
| **teaching atom** | The 4-tuple of Axiom 1: one arrow, $N=Q=1$. One state among several an atom can be in. |
| **atom** (Collapsed) | $N$ cores holding $Q$ informational vectors $v_i=(r_i,\hat n_i,\chi_i)$, $0<r_i\le1$, under one closure; all vectors share one sort $\tau$. Arises by Collapse or is seated directly by whatever supplies the seat. |
| **core** | A group of vectors held together in an atom. Holds any number of vectors: one, many, or none. “Core” is reserved for this sense. |
| $N$ | Number of **cores**. A count of the stored atom: does not change with the reading time $t$. |
| $Q$ | Number of informational **vectors** — “the atom's info number”. $Q\ge N$ is usual, not a rule. Read over the cores valid at $t$. |
| $D$ | Number of **distinct cores** among the $N$: two cores coincide exactly when $\uplus$ would seat them together (content only; empty cores coincide; meta vectors never enter). $D\le N$, equality iff every core is distinct. Stored count. |
| $N-D$ | How many times some core repeated. |
| $A^{\langle k\rangle}$ | $k$ identical copies of $A$; has $kN_A$ cores. $A\oplus A=A^{\langle2\rangle}$. |
| **empty atom** | Black: $N=1$, $Q=0$. $S,\mathcal V,\mathcal E,V_{\text{derived}}=0$; $\gamma_{\text{atom}}=0$, $\sigma_{\text{atom}}=0$ by convention; $\alpha_{\text{atom}}$, $\sigma_{\text{shell}}$, $Q_{\text{eff}}$ undefined. Collapse keeps a silent contribution: $A\oplus0$ has one more core, same vectors; $0\oplus0\neq0$. |
| **mass number / atomic number** | $N$ reads like a nucleus's mass number (every core counted), $D$ like its atomic number (distinct cores). An analogy of shape only. |


---

## 4 · Metrics (Axiom 7, §2.10)

Named in the paper: *atom strength*, *atom volume*, *mean vector volume*, *atom coherence*, *effective vector count*; $\mathcal E_{\text{atom}}$ is “the atom's intrinsic energy”; $\alpha_{\text{atom}}$, $\sigma_{\text{atom}}$, $\sigma_{\text{shell}}$ are its fifth, sixth and seventh metrics, described but not named (descriptive labels below are marked). All presuppose an atom of $Q$ informational vectors $v_i=r_i\hat n_i$. None is used by any verb; each is read over the cores valid at the reading time. Identity: $\lvert V_{\text{derived}}\rvert^2=\mathcal E_{\text{atom}}+2\sum_{i<j}r_ir_j(\hat n_i\!\cdot\!\hat n_j)$, the structure of a variance of a sum.

| Symbol | Formula | What it measures | Requires |
|---|---|---|---|
| $V_{\text{derived}}$ | $\displaystyle\sum_{i=1}^{Q}r_i\hat n_i$ ($\chi$ excluded) | The raw, **uncapped** vector sum; per core and per atom (the atom's is the sum of its cores'). Reads as an effective pair $r=\lvert V\rvert$, $\hat n=V/r$ for a weight or a direction; not itself a unit; needs a cast into $[0,1]$ before acting as $T$'s actor. | any $Q$ |
| $S_{\text{atom}}$ | $\displaystyle\sum_ir_i$ | **Atom strength.** Denominator of atom coherence. | any $Q$ |
| $\mathcal V_{\text{atom}}$ | $\displaystyle\sum_ir_i^3$ | **Atom volume.** Strictly $<S_{\text{atom}}$ whenever any $r_i<1$ — forced by the cap. | any $Q$ |
| $\gamma_{\text{atom}}$ | $\mathcal V_{\text{atom}}/Q$ | **Mean vector volume.** | $Q\ge1$ ($:=0$ at $Q=0$) |
| $\mathcal E_{\text{atom}}$ | $\displaystyle\sum_ir_i^2$ (eq. 15) | **Intrinsic energy** (the paper's phrase). Stands on its own; the energy the vectors would carry if every pair were orthogonal. | any $Q$ |
| $\alpha_{\text{atom}}$ | $\dfrac{\sum_{i<j}r_ir_j(\hat n_i\cdot\hat n_j)}{\sum_{i<j}r_ir_j}$ (eq. 16) | *Fifth metric; unnamed.* Strength-weighted mean cosine similarity across all internal pairs; separates active cancellation ($<0$) from mere non-reinforcement, which atom coherence cannot. | $Q\ge2$ |
| $\sigma_{\text{atom}}$ | $\dfrac{Q^2}{Q-1}\operatorname{Var}(s_1,\ldots,s_Q)$, $s_i=r_i^3/\mathcal V_{\text{atom}}$ (eq. 17) | *Sixth metric; unnamed* (concentration of volume). $0$ when even, $1$ when one vector holds all. Equals the normalized Herfindahl index of the cubed shares. | $Q\ge2$ ($:=0$ at $Q\le1$) |
| $\sigma_{\text{shell}}(w)$ | $1$ if $K=1$; else $\dfrac{K^2}{K-1}\operatorname{Var}(p_1,\ldots,p_K)$, $p_k=n_k/Q$, bins of width $w$ (default $0.1$) (eq. 18) | *Seventh metric; unnamed* (concentration across shells). Catches what $\sigma_{\text{atom}}$ cannot: many vectors independently landing at the same magnitude. | $Q\ge1$ |
| $Q_{\text{eff}}$ | $S_{\text{atom}}^2/\mathcal E_{\text{atom}}$ | **Effective vector count** — not an eighth metric. $1\le Q_{\text{eff}}\le Q$; scale-free; the largest vector holds at least $1/Q_{\text{eff}}$ of the strength; a *count*, with $Q_{\text{eff}}/Q$ the size-free form. | $S_{\text{atom}}>0$ |
| **atom coherence** | $\lvert V_{\text{derived}}\rvert/S_{\text{atom}}$ | How much strength survives into one resultant; $1$ for aligned vectors, falling toward $0$. Also a cast of $V_{\text{derived}}$ into $[0,1]$. | $S_{\text{atom}}>0$ |


---

## 5 · Meta vectors (§2.11)

**What they are.** Values that describe an atom and are no part of what it says. Not capped; not informational; counted in neither $N$ nor $Q$; outside the seven metrics and $D$; no admissibility of their own; **not a coordinate** (the four coordinates and the sort tag are unchanged). They ride with the cores they describe. Anything beyond that — what a meta vector *means* — is extracted by context or by the path that reads it.

| Kind | Held | What it is |
|---|---|---|
| $V_{\text{derived}}$ | per core and per atom | Sum of the informational vectors, recomputed whenever the content is. Already in the paper (Axiom 7). |
| seat $\vec P$ | per unit or bowl | External position in unbounded Euclidean space; enters only $d_{AB}=\lvert\vec P_B-\vec P_A\rvert$ (§10.1). Already in the paper. |
| $V_{\text{timestamp}}$ | per core | When the core was born, an **absolute** (non-cyclic) time, so age $=t-V_{\text{timestamp}}$ is derived, never stored. An optional clock-face vector (minute on $\phi$, hour on $\chi$, $\theta$ at the equator) groups by time of day but cannot replace it. A Collapse result also gets its own new timestamp. |
| $V_{\text{expiry}}$ | per core | When the core stops being valid. **Absence means no expiry.** Valid at $t$ iff $t$ is earlier than every expiry it carries. |
| $V_{\text{location}}$ | per core | A point on a sphere (latitude as polar angle, longitude as azimuth). Not a sort: a place is a coordinate, not a claim with a strength. |
| $V_{\text{link}}$ | per core | Names another atom by one of that atom's meta vectors, never by content (a word is never linked to a poem). Only **backward** links are stored, at birth; forward and bidirectional links are views (a search for atoms whose backward link names a given one). A Collapse result gets a backward link naming its sources. |


### Rules that govern all of them

| Rule | Statement |
|---|---|
| **Form** | Always vectors, with no constraint on form. A scalar meta vector takes a designated axis of its core and carries its value as the coordinate there (uncapped), so vector distance is the difference of values; more coordinates (a plane or more) where a kind needs them. Which axis suits which kind is a recommendation (a catalogue, §6.7), not an axiom. |
| **Turning** | Turn an atom as a whole (same rotation and phase shift on each vector): $V_{\text{derived}}$ turns with it; scalar meta vectors are carried unchanged; angles, magnitudes and distances among the information vectors and $V_{\text{derived}}$ are preserved. |
| **Atoms are not edited** | An atom is a value. Change is Collapse or UnCollapse, each returning a new atom; recorded meta vectors never change after birth. There is no “last modified”. |
| **Equality ignores them** | Equality of cores (for $\uplus$, $D$, UnCollapse) is on content only. Were the timestamp part of the value, $N-D$ would always be $0$ and $A\uplus A=A$ would never apply. |
| **Expiry is a reading** | Everything is read at a time $t$ (default now). An expired core contributes no vectors and reads as a black core; $N$, $D$ are stored counts and do not change with $t$; $Q$, $V_{\text{derived}}$, the metrics and every process read only valid cores. An atom's expiry applies to all its cores; a contribution's expiry is carried onto each of its cores at Collapse. A backward link is lineage, not participation, and stays readable. |
| **Nothing loses identity** | Under Collapse, Bundle and Mix the individual persists as meta vectors; this is persistence, not recovery. Mix leaves its sources unconsumed and names them by backward links; UnMix stays impossible. |
| **Absence is not zero** | For any meta vector: an absent location is not $(0,0)$; “expiry $0$ means none” would read as already expired. |
| **No verb changes one** | No verb changes a meta vector or takes one as an operand; a verb may read one (Assembly reads $V_{\text{derived}}$ and the seat). A meta vector never becomes an actor. |
| **Uses** | Group atoms for a task (collect, order, assemble). Grouping needs a comparison stated with each kind (great-circle for a location, cyclic for a clock face, equality for an identifier); none is common to all. Direction is the cleaner assembly rule; magnitude enters as a weight. Links declare structure and Assembly's energy produces it from geometry and a seat; the two are separate. Links can carry an order past $\uplus$, which does not read them, so order still comes from outside and the path is where it is walked. At contact the best partner of an atom of strength $0.60$ has strength $0.30$; at separation $3$ it is the strongest available. |


---

## 6 · Other named quantities, by operator

| Symbol | Formula | Lives in | What it is |
|---|---|---|---|
| $U_{AB}$ | $-\dfrac{r_Ar_B}{2}\cdot\dfrac{3+\hat n_A\cdot\hat n_B}{(d_{AB}^2+\varepsilon_{AB}^2)^{3/2}}$ (eq. 13) | §2.9 | Assembly's interaction energy. Product $r_Ar_B$: how strong; bracket in $[2,4]$: how aligned (at most a factor of two); denominator: how far. Always $<0$ for nonzero strengths; exactly $0$ for a black unit. |
| $\varepsilon_{AB}$ | $r_A+r_B$ | §2.9 | Softening length, derived by reading $r$ as a radius. |
| $\kappa_{AB}$ | $\hat n_A+\hat n_B$ (unnormalized; eq. 14) | §2.9 | Contact point; defined at every angle, $=\mathbf0$ at antipodal. Its magnitude falls from $2$ to $0$. |
| polarity | $\lvert r_A-r_B\rvert$ | §2.9 | Labels a bond as balanced or lopsided; does not change what the relation does. |
| $d_{AB}$, $\hat r_{AB}$ | $\lvert\vec P_B-\vec P_A\rvert$, $(\vec P_B-\vec P_A)/d_{AB}$ (eq. 46) | §10.1 | Separation and separation axis; no axis derived from orientation is used. |
| $\alpha(r_w)$ | $\pi r_w$ | §4.2 | Strength to rotation angle; $r_w=1$ gives $180^\circ$. |
| $z_B$ | $\sum_{x\in B}r_xe^{i\chi_x}$; $\boxplus(B)=(\min(1,\lvert z_B\rvert),\hat n,\arg z_B,\tau)$ (eq. 9) | §2.6 | Mix's one-step bowl reading; the reason binary Mix is non-associative under the cap. |
| $\log_{\hat p}$, $\exp_{\hat p}$ | $\frac{\theta}{\sin\theta}(\hat q-(\hat p\cdot\hat q)\hat p)$; $\cos\lVert v\rVert\,\hat p+\sin\lVert v\rVert\,v/\lVert v\rVert$ (eq. 29–30) | §5.1 | Walk from $p$ to $q$ as a tangent vector, and back. |
| transport | $\mathrm{Rot}_{\hat u}(\theta_{mw})\,v$, $\hat u=\hat n_m\times\hat n_w/\lVert\cdot\rVert$ (eq. 32–33); general $N_{\mathrm{dim}}$: a rotation within the plane the two seats span (eq. 35) | §5.1 | Carries the walk from seat $m$ to seat $w$. The two seats name the turning plane, so no Collapse is needed. Exactly the cross-product form at $N_{\mathrm{dim}}=3$. |
| $F_i$ | $-\nabla_{\vec P_i}\sum_{j\neq i}U_{ij}$; step $\vec P_i\leftarrow\vec P_i+\delta F_i$ (eq. 47) | §10.2 | Force on a seated unit, descended with no mass and no momentum. |
| freeze at resolution $\eta$ | $\max_i\lvert F_i\rvert<\eta$ (eq. 48) | §10.2 | A stated checkpoint, not exact rest: the pull is positive at every finite separation, so left longer every configuration drifts toward one pile. |
| camp, body $\vec P_{c,k}$ | $\dfrac{\sum_{i\in G_k}r_i\vec P_i}{\sum_{i\in G_k}r_i}$ (eq. 49) | §10.3 | A frozen group and its strength-weighted centre, read *after* motion. A system of camps is the *set* of bodies, never one grand average. |
| $\epsilon_{\text{allow}}$ | named, not derived | §10.3 | Checkpoints whose bodies differ by less are read as the same freeze. |


---

## 7 · Sorts, tiers, and who may do what

| Sort | Native law $\circ_\tau$ | Mix/$T$ map? | Tier |
|---|---|---|---|
| `num` | schoolbook $+$ | no (chart only) | 0 |
| `word` | none claimed | n/a | 0 |
| `note-pitch` | pitch-class sum | near-exact | 1 |
| `color` | additive light | phasor Mix (here; a toy $0^\circ/120^\circ/60^\circ$ chart — not CIE, not linear RGB) | 1 |
| `chladni` | modal superposition | exact within a mode; undefined across | 1 (restricted) |
| `snowflake` | $D_{6h}$ growth | no | Tier 1 no; Tier 0 yes |

| Pair | $+$ | $\uplus$ | $\oplus$ | $\boxplus$ | $T_w(x)$ | $x-a+b$ |
|---|---|---|---|---|---|---|
| (`word`,`word`) | no | yes | yes | yes$^\dagger$ | yes | yes |
| (`num`,`num`) | yes | yes | yes | no (clock trap) | no | no |
| (`word`,`num`), (`num`,`word`) | no | yes | open | no | typed | no |
| (`color`,`color`) | no | yes | yes | yes | yes | open |
| (`note-pitch`,`note-pitch`) | no | yes | yes | yes | yes | open |
| (`chladni`,`chladni`) | no | yes | yes | yes (within a mode) | open | open |
| any other pair | no | yes | open | open | open | open |

§6.4 (Table 3). Every Mix entry is also subject to the place restriction (shared $\hat n$). $\uplus$ is *yes* for every pair: a bowl records presence and makes no domain claim. $\oplus$: same sort yes, cross-sort open. $^\dagger$Mix on two words is geometry, not a $\chi$-reading of language. **A document is a sequence, not a blend** (§6.3): words and numbers meet only by *juxtaposition*, *typed action* ($T$ across sorts needs an explicit output sort) or *cast*; $\mathrm{dawn}\uplus37.4$ has no meaning until one side is cast.


---

## 8 · Dimensions: how an actor grows beyond three

| Space | Sphere | Fixed part (the “axis”) | What turns |
|---|---|---|---|
| $\mathbb R^2$ | $S^1$ | a point, dim 0 | one plane |
| $\mathbb R^3$ | $S^2$ | a line, dim 1 | one plane |
| $\mathbb R^4$ | $S^3$ | a plane, dim 2 | one plane |
| $\mathbb R^5$ | $S^4$ | a 3-D space, dim 3 | one plane |
| $\mathbb R^{N_{\mathrm{dim}}}$ | $S^{N_{\mathrm{dim}}-1}$ | dim $N_{\mathrm{dim}}-2$ | one plane |

A teaching atom ($Q=1$) is a legal actor **only at $N_{\mathrm{dim}}=3$**; beyond that the actor's atom must supply $N_{\mathrm{dim}}-2$ mutually orthogonal arrows ($Q\ge N_{\mathrm{dim}}-2$ is necessary, not sufficient): $T_w(x)=(r_x,\ \hat n_x^F+\mathrm{Rot}_{\alpha(r_w)}\hat n_x^{P},\ \chi_x+\chi_w,\ \tau_x)$, eq. 23. Orientation of $F^\perp$ is a convention, stated once. Checked invertible at every angle tested and non-commutative at $N_{\mathrm{dim}}=4,5,8,12,20,50$; exact at $N_{\mathrm{dim}}=3$. Offset's transport generalizes without any Collapse. Mix, Bundle and $\alpha_{\text{atom}}$ are dimension-blind. The paper keeps $\mathbb R^3$ as its standing assumption (§4.4).


---

## 9 · Numbers worth remembering (all recomputed from the printed inputs)

| Claim | Printed value | Where |
|---|---|---|
| $(1\angle0^\circ)\boxplus(1\angle120^\circ)$ (red, green) | $1\angle60^\circ$, yellow | §2.6 |
| $0.6\angle0^\circ\boxplus0.8\angle120^\circ$ | $r'\approx0.721$, $\chi'\approx73.9^\circ$ | §2.6, §8.1 |
| $A\boxplus A$ | $r'=\min(1,2r)$ — not idempotent | §2.6 |
| $A=B=1\angle0^\circ$, $C=1\angle180^\circ$ (by hand) | $(A\boxplus B)\boxplus C=$ black, $A\boxplus(B\boxplus C)=1\angle0^\circ$; one-step $z_B=1$ | §2.6 |
| Clock, $M=24$: $7+5$ and Mix of the two marks | $12$ (decode, add, encode); Mix gives $\chi'=90^\circ$, hour $6$ | §6.2 |
| Sun, Wind, Sky ($r_{\text{Sun}}=1$, $r_{\text{Wind}}=0.7$) | Sun then Wind $(-0.866,-0.500,0.011)$; Wind then Sun $(0.278,-0.500,0.820)$; $\alpha_{\text{Wind}}=126^\circ$ | §4.6 |
| Four-dimensional actor, $r_w=0.5$ | $T_w(\hat n_x)=(\tfrac12,\tfrac12,0,\tfrac1{\sqrt2})$, recovered by $w^*$ | §4.7 |
| Order gap, $N_{\mathrm{dim}}=4,5,8,12,20,50$ | $0.683,\ 0.688,\ 0.649,\ 0.584,\ 0.489,\ 0.331$ | §4.4 |
| Storm: Deepen / Clear endpoints | $(0.7071,-0.6124,-0.3536)$, $(110.7^\circ,319.1^\circ)$ / $(0.3536,-0.6124,-0.7071)$, $(135^\circ,300^\circ)$; both $\chi=135^\circ$ | §9.1 |
| Offset on an equator ($0^\circ,30^\circ,90^\circ$) | lands at $(-\tfrac12,\tfrac{\sqrt3}2,0)$, $120^\circ$ — a protractor check, not the operator | §5.2 |
| Unmixing: $0^\circ/120^\circ$ against $10^\circ/100^\circ$ | same phasor sum (weights $0.643$, $0.766$); residual at rounding level | §8.2 |
| Alignment, $r=0.85$, pairs $5.7^\circ$ apart | $Q=2$: raw $0.72$, $\alpha=0.995$; $Q=5$ on a cone of half-angle $5.7^\circ$: $7.14$, $0.988$ | §2.10 |
| Three aligned at $r=0.5$ | $\lvert V\rvert=1.5$, $\alpha(1.5)=270^\circ$ — not a rotation $T$ accepts uncast | §2.10 |
| Dominant vector $0.95$ against three at $0.2$ | volume share $0.973$ | §2.10 |
| Best partner for an atom of $r=0.60$ (Assembly energy) | at contact $r_B=0.30$; at separation $3$ the strongest available ($1.0$) | §2.11 |
| $\sigma_{\text{shell}}$: $10@0.98$, $3@0.3$, $400@0.65$ | $0.908$ at $w=0.1$ and $w=0.05$ | §2.10 |
| Enclosure, six printed units, $\eta=10^{-5}$ | $628,\ 1261,\ 2526,\ 6320$ steps at $\delta=0.02,\ 0.01,\ 0.005,\ 0.002$; two camps $\{1,2,3\}$, $\{4,5,6\}$; bodies $(0.33336,0.33333,0)$, $(40.33330,0.33333,0)$; runs agree to $2\times10^{-7}$; $r$-weighted and plain bodies differ by $2.4\times10^{-8}$ | §10.4 |
| Enclosure, pair $r=0.9$, $r=0.1$, $\delta=0.02$ | separation never increases, $3\to1.80$; dividing each step by $r^3$ (a $729$-fold weighting) makes it oscillate | §10.4 |

**Where a printed number cannot be reproduced exactly:** the $\sigma_{\text{atom}}$ comparison ($0.00032$ clumped against $0.00214$ uniform) and the “$2.200$ against $2.150$” strength comparison, because their populations are not printed (a uniform spread over $(0,1]$ gives $0.0032$); the count of $804$ of $3000$ steps on which the pair's separation increases, which is rounding-sensitive (about $830$–$855$ in replays; the qualitative claim is robust); and shell binning at floating-point edges ($\lfloor0.3/0.1\rfloor$ is $2$ in floating point), where the printed populations are unaffected.


---

## 10 · Named conventions — choices, not truths

| Convention | What it fixes | Where |
|---|---|---|
| the clip $r'=\min(1,\lvert z\rvert)$ | How the cap is imposed. An order-preserving bijection $\lvert z\rvert\mapsto\lvert z\rvert/(1+\lvert z\rvert)$ would bound without discarding but makes $r=1$ a limit. The clip is kept; the trade is stated. | §2.2 |
| $\alpha(r)=\pi r$ | The simplest monotone map from strength to rotation angle. | §4.2 |
| orientation of $F^\perp$ | Which direction counts as $+\alpha$ beyond three dimensions; any consistent choice, stated once. | §4.4 |
| toy colour chart | Phasor Mix on $0^\circ/120^\circ/60^\circ$; neither CIE nor linear RGB. | §2.1, §2.6 |
| numeric chart | $\chi=2\pi k/M$, $M=24$, at a fixed direction with $r=1$. | §6.1–6.2 |
| shell width $w$ | Default $0.1$ (ten shells on $[0,1]$); reported with $\sigma_{\text{shell}}$. | §2.10 |
| $\eta$, $\delta$, census cut, $\epsilon_{\text{allow}}$ | Freeze threshold; step size; how camps are counted; when two checkpoints are the same freeze. The enclosure's four measurement conventions. | §10.2–10.3 |
| reading time $t$ | Default now; fixing it keeps every law deterministic. “Now” is external context, as the lexicon is. | §1.4, §2.11 |
| standard dictionaries and the meta-vector catalogue | Recommendations, recorded and left open; not axioms. | §6.7 |


---

## 11 · Stated open, or not claimed

| Item | Status in the paper | Where |
|---|---|---|
| Collapse across differing sorts | Open. Axiom 7 requires every vector in one atom to share the atom's single $\tau$; Collapse across sorts needs a per-vector $\tau_i$ extension that Axiom 7 does not currently grant. | §3.3, §12.1 |
| Collapsed atom as the actor of $T$ | An example is not claimed here; a cast is named at the call site. | §2.10 |
| Identity handle $id_i$ | Proposed, not adopted: tells same-valued sources apart in UnCollapse. | §3.4 |
| Reducing a path by merging close actors | Sequential actors already compose into one rotation for free (closure). Replacing merely *close* actors is a different operation, coarse-graining, whose shape only is stated: it yields an additional derived actor *beside* its sources and removes none. Which merge rule, and what drift bound, belongs to Inference. | §12.1 |
| Dimensionality | The sphere $S^2$ is where the idea is taught; embedding-scale dimensions are a later choice. | §6.8, §12.1 |
| Offset on Tier-1 sorts; antipodal offset | Untested here; antipodal seats have no unique short geodesic and that convention is not used. | §5.1, §6.4 |
| Combining across sorts | No rule stated at all (a colour with a charge; a chord with a valence bond). | §1, §2.1 |
| Verdicts | Saying what a resting state *means* is a later reading, not a verb here. | §1 |


---

## 12 · Document map

| § | Title | What you will find |
|---|---|---|
| 1 | Introduction | Thesis; examples of other arithmetics; Pāṇini; scope of the claim (1.4); determinism. |
| 2 | Axiomatic Foundations | Axioms 0–7, Mix refusal and chladni (2.7), rotation (2.8), Assembly (2.9), metrics (2.10), meta vectors (2.11). |
| 3 | Process Principles | Bundle–path–result and levels (3.1); UnMix (3.2); Collapse (3.3); UnCollapse (3.4). |
| 4 | Transformation Algebra | $T$: definition, properties, beyond three dimensions, poems as trajectories, worked examples. |
| 5 | Offset | Log, carry, exponential; the equator check; offset is not $T$. |
| 6 | Encodings, Sorts, Mixed Documents | `num` and `word`; the clock; a document is a sequence; operator legality; lexicons; standard dictionaries. |
| 7 | A Sketch of Conventions | Case and language do not move the address; a bag is not a sentence; a numeral is not a word until cast. |
| 8 | Operational Algebra | Mix of two shells; why unmixing is ill-posed; spectral storage (later). |
| 9 | Higher-order systems | Costumes: storm, table and chair, forest, pathogen. |
| 10 | The Enclosure | Seats, rest and freeze, camps and bodies, a replayable configuration, what it does not supply. |
| 11–12 | Discussion; Conclusion | Related work (Bloch sphere, embeddings, transformers, RotatE, von Mises–Fisher, Riemann sphere, $\mathrm{SO}(3)$, spherical harmonics); future work. |


---

## 13 · A–Z index of terms with special meanings

| Term | Meaning | Where |
|---|---|---|
| **Actor** $w$ | The unit that acts in $T_w(x)$: supplies axis, strength (→ angle) and phase. Beyond three dimensions it must supply $N_{\mathrm{dim}}-2$ orthonormal arrows. | §4.2, §4.4 |
| **Admissible** (geometrically) | A sort with a stated map $\varphi_\tau$ at a stated fidelity (Tier 1). Absent from the table = undecided, not admitted. | §2.1, eq. 1 |
| **Age** | $t-V_{\text{timestamp}}$; derived, never stored (a stored age is wrong once time passes). | §2.11 |
| **Allowance** $\epsilon_{\text{allow}}$ | Checkpoints whose bodies differ by less are read as one freeze; a named convention. | §10.3 |
| **Arithmetic** (of a domain) | A unit of truth plus a small set of rules for combining such units, obeyed consistently. | §1 |
| **Assembly** $\bowtie$ | Relates two intact units by $(\kappa_{AB},U_{AB})$ without fusing them. | §2.9 |
| **Atom** | The typed unit. *Teaching atom*: one arrow. *Collapsed atom*: $N$ cores, $Q$ vectors, one closure. | §2.2, §2.10 |
| **Atom coherence** | $\lvert V_{\text{derived}}\rvert/S_{\text{atom}}$. | §2.10 |
| **Axis** ($\hat n_w$, fixed part $F$) | The line (3-D) or subspace of dimension $N_{\mathrm{dim}}-2$ that $T$ leaves fixed. | §4.4 |
| **Black** $\mathbf0$ | $r=0$: an empty seat; $N=1$, $Q=0$; $T_{\mathbf0}=\mathrm{id}$; the identity of nothing else. Distinct from the empty bowl $\emptyset$. | §2.3, §2.5 |
| **Body** $\vec P_{c,k}$ | A frozen camp's strength-weighted centre, measured afterwards by an observer; a description, not a destination. | §10.3, eq. 49 |
| **Bowl** | A finite set of seated units: who is present. No order, no reading, no representation of the reading to come. May carry meta vectors; $\uplus$ does not read them. | §2.2, §2.5, §3.1 |
| **Bundle** $\uplus$ | Union on bowls; idempotent; sort-blind. | §2.5 |
| **Camp** | A separated group frozen at resolution $\eta$; their number is whatever the law, the seats and $\eta$ produce. | §10.3 |
| **Cast** (three uses) | (a) lexicon cast $E_L$: token to state (eq. 42); (b) sort cast, e.g. $E_{\mathtt{num}\to\mathtt{word}}$ (§6.3); (c) the cast of the uncapped $V_{\text{derived}}$ back into $[0,1]$ so it may act as $T$'s actor — the clip, or atom coherence (§2.10). | §6.6, §6.3, §2.10 |
| **Census cut** | The stated separation (or chain of short links) used to count camps; a convention. | §10.3 |
| **Chart** | An exact, invertible encoding (e.g. `num`); not a Mix or $T$ homomorphism. | §2.1, §6.2 |
| **Checkpoint** | One freeze read at some $\eta$ after some time; not a destination. | §10.3 |
| **Clip** | $r'=\min(1,\lvert z\rvert)$; the chosen way to bound strength; not injective. | §2.2, §2.6 |
| **Clock trap** | Mix on $(\mathtt{num},\mathtt{num})$: geometrically defined, type-refused. $7$ and $5$ Mix to hour $6$. | §6.2 |
| **Collapse** $\oplus$ | Count-preserving combination; keeps every core; not idempotent. | §3.3 |
| **Companion paper** | *Pattern Arithmetic: Inference from Bowls and Paths* — reference atoms, classification, abstention; where unmixing and path reduction are left. | §1, §3.2, §12.1 |
| **Contact point** $\kappa_{AB}$ | $\hat n_A+\hat n_B$, unnormalized; $\mathbf0$ at antipodal. | §2.9, eq. 14 |
| **Core** | A group of vectors held together in an atom; any number of vectors. Reserved word. | §2.10 |
| **Costume** | An illustration of the $\uplus$-versus-$T$ split (storm, table and chair, forest, pathogen); not a model. | §1.4, §9 |
| **Counting trap** | $A\uplus A\uplus A\uplus A\setminus A=\emptyset$: four gathers are one seat, one removal empties it. | §2.5, eq. 7 |
| **Density** | Many identities can share the stage without overwrite. Not a metric and not infinite information. | §2.4 |
| **Determinism** | Same printed starting units (read at the same time where any carries an expiry) give the same result, step for step. Printing makes a result replayable; it does not make it right. | §1.4 |
| **Dictionary pin / doorbell** | A seated unit for a name (man, storm, calm, Night). The algebra does not mint it; a lexicon or learning rule seats it. | §9.1, §5.2, §6.6 |
| **Direction** $\hat n$ | A pattern's semantic address, not its physical position. | §2.2, §10.1 |
| **Effective vector count** $Q_{\text{eff}}$ | $S^2/\mathcal E$; how many equally strong vectors carry the same energy. | §2.10 |
| **Empty atom** | Black: $N=1$, $Q=0$. | §2.3, §2.10 |
| **Empty bowl** $\emptyset$ | A bowl with no occupant; $\neq\mathbf0$. $T_{\mathbf0}$ is defined, $T_\emptyset$ is not. | §2.5, eq. 6 |
| **Enclosure** | Seats, rest and camps: where Assembly's separation comes from. | §10 |
| **Energy** (two senses) | The atom's intrinsic energy $\mathcal E_{\text{atom}}=\sum r_i^2$ (§2.10, eq. 15); the interaction energy $U_{AB}$ (§2.9, eq. 13). Not interchangeable. | §2.10, §2.9 |
| **Equality** (of cores) | On content only; meta vectors never enter. | §2.11 |
| **Expiry** $V_{\text{expiry}}$ | When a core stops being valid; absence = none; an expired core reads as black. | §2.11 |
| $F_i$ (**force**) | $-\nabla_{\vec P_i}\sum_{j\neq i}U_{ij}$. | §10.2, eq. 47 |
| **Freeze** (at resolution $\eta$) | $\max_i\lvert F_i\rvert<\eta$. A freeze, not a stop. | §10.2, eq. 48 |
| **Identity handle** $id_i$ | Proposed, not adopted: tells same-valued sources apart. | §3.4 |
| **Individual** vs **value** | Under Collapse, Bundle, Mix the individual (with its meta vectors) persists; value is content only. | §2.11 |
| **Informational vector** | One of an atom's $Q$ arrows $v_i=(r_i,\hat n_i,\chi_i)$, $0<r_i\le1$. | §2.10 |
| **Levels are closed** | A result may be seated again and Bundled, walked, read at the next level. | §3.1 |
| $E_L$ (**lexicon**) | A map from one language's tokens onto states; case and language do not move the address. | §6.6, §7, eq. 42 |
| **Link** $V_{\text{link}}$ | Backward provenance stored at birth; forward and bidirectional are views. | §2.11 |
| **Location** $V_{\text{location}}$ | A point on a sphere carried as a meta vector; not a sort. | §2.11 |
| **Meta vector** | A value that describes an atom and is no part of what it says. | §2.11 |
| **Mix** $\boxplus$ | Phasor reading of states sharing a direction. | §2.6 |
| **Mix across differing directions** | Refused. Settled by declining, not by finding a rule. | §2.7 |
| **Mode** (`chladni`) | A vibration mode; Mix exact within one, undefined across. | §2.7 |
| **Non-associativity** (Mix) | A consequence of the cap: the binary operator is not associative; the one-step bowl reading is. | §2.6 |
| **Non-commutativity** ($T$) | Inherited from $\mathrm{SO}(3)$; the only thing that lets two poems from one bowl diverge. | §4.3, eq. 22 |
| **Occupant** (register occupant) | The single current unit on the sphere that $T$ acts on. | §2.2, §3.1 |
| **Offset** | Copies a walk; does not mint the landing's name. | §5 |
| **Order gap** | $\lvert T_{w_2}T_{w_1}\hat n_x-T_{w_1}T_{w_2}\hat n_x\rvert$. | §4.4 |
| **Path / walk / trajectory** | An ordered sequence of actors on an occupant; a poem is a $T$-walk. Order enters here and not in the bowl. | §3.1, §4.5 |
| **Phase** $\chi$ | Internal phase / mood / hue: adds under $T$, sums as a phasor under Mix; reserved for mood, not language. | §2.2, §7 |
| **Polarity** | $\lvert r_A-r_B\rvert$. | §2.9 |
| **Pratyāhāra; vipratiṣedha** | Pāṇini's sound-class shorthand and his conflict-resolution rule; offered as kinship, not identity. | §1 |
| **Reading** | An operation that returns a state and leaves its inputs intact (Mix, a $T$-path, Collapse); also, expiry is a reading. | §2.6, §3.3, §2.11 |
| **Remove** $\setminus$ | Takes one member out of a bowl. | §2.5 |
| **Rest** | A freeze at a stated resolution, never exact stillness. | §10.2 |
| **Result** | Whatever the path makes of the bowl. | §3.1 |
| **Rotation** | $\mathrm{SO}(3)$ turn of $\hat n$ only. | §2.8 |
| **Seat** $\vec P$ | External position vector; a meta vector; enters only $d_{AB}$. | §10.1, eq. 46 |
| **Seated unit** | A unit loaded on the sphere, pinned by a lexicon or a learned map. | §1.4, §3.1 |
| **Shell** | (a) a width-$w$ bin of strength in $\sigma_{\text{shell}}$ (§2.10); (b) one phased identity at a direction in Mix (“two shells, not an angle”, §8.1). | §2.10, §8.1 |
| **Softening length** $\varepsilon_{AB}$ | $r_A+r_B$, derived by reading $r$ as a radius. | §2.9 |
| **Sort** $\tau$ | Says which operators may legally act on a unit; does not move the arrow. | §2.2, §6 |
| **Stage** $\mathcal S$ | The unit sphere (or its higher analogue): the sphere is the stage, the unit is the vector. | §2.2 |
| **Step** $\delta$ | Numerical sampling convention for the descent. | §10.2 |
| **Strength** $r$ | Normalized activation in $[0,1]$. | §2.2 |
| **Tape** | An ordered sequence of tokens; a document. | §6.3 |
| **Teaching atom** | One 4-tuple, $N=Q=1$. | §2.2 |
| **Tier 0 / Tier 1** | Inert seating; or explicit inclusion by a stated $\varphi_\tau$. | §2.1 |
| **Timestamp** $V_{\text{timestamp}}$ | Absolute birth time of a core; a Collapse result has its own. | §2.11 |
| **Transform** $T$ | Rotate the occupant about the actor's axis by $\pi r_w$ and add the actor's phase. | §4 |
| **Transport** | Carries a tangent vector from seat $m$ to seat $w$ in Offset. | §5.1, eq. 33, 35 |
| **Turn** (an atom) | Same rotation and phase shift on each vector; $V_{\text{derived}}$ turns, scalar meta vectors are carried. | §2.11 |
| **UnCollapse** $\ominus$ | Returns the atom without one core. | §3.4 |
| **UnMix** $\boxminus$ | Impossible: sources not determined by the result. | §3.2, §8.2 |
| **Valid** (core) | At $t$ iff $t$ is earlier than every expiry it carries. | §2.11 |
| **Volume** $\mathcal V_{\text{atom}}$ | $\sum r_i^3$, “atom volume”; descriptive only, deliberately excluded from motion. | §2.10 |
| **White** | Saturation of the bowl, or a full-spectrum name; never $r=\infty$. | §2.4 |
| $D$ | Distinct cores among the $N$. | §3.3 |
| $N$ | Cores. | §2.10 |
| $N_{\mathrm{dim}}$ | Dimension of the ambient space; $3$ is the standing assumption. | §4.4 |
| $Q$ | Informational vectors; “the atom's info number”. | §2.10 |
| $U_{AB}$ | Assembly's interaction energy. | §2.9, eq. 13 |
| $V_{\text{derived}}$ | Uncapped sum of the informational vectors. | §2.10 |
| $z_B$ | Phasor sum of a bowl. | §2.6, eq. 9 |
