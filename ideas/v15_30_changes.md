# Pattern Arithmetic v15_30 — changes from v15_29

v15_30 is v15_29 with the UnCollapse cluster merged: 24 changes at the sites below. Every closure was verified against the released text.

## What changed

- The atom is a collection of cores, each a collection of vectors; **a vector is held by exactly one core, as a nucleus holds its electrons, and no verb moves a vector from one core to another**; the containment vector records which core holds which vector.
- Each vector carries its own sort τᵢ; **Collapse takes atoms of any sorts**; V_derived and the seven metrics read every vector whatever its core or sort; a sort's share is read from the sub-atom that holds it.
- **Grain** is the partition of an atom's vectors into cores; UnCollapse acts along it; fixed at seating, coarsened by seating again, refined by no verb.
- UnCollapse takes an **identity key** (tuple of existing meta vectors: sort, source link, timestamp), falls back to **local position** when a key matches cores of different content; a series is repeated UnCollapse.
- §2.11 gains **Identity and containment**: identity is read from meta vectors and never enters equality; containment is *not* a meta vector, because it is the grouping itself and equality compares it.
- Every result is a new atom with its own timestamp and a backward link; surviving cores keep theirs. Expired cores are noise and may be removed by UnCollapse selected by expiry.
- Equality has two tests: **equal** (vectors and grouping; ignores meta vectors) and **the same individual** (also meta vectors). Equality is exact; measured readings are made comparable at seating.
- Table 3: Collapse is *yes* for every pair, like Bundle. The Future Work item on Collapse across sorts is removed.

## Checks

- 0 errors and 0 undefined references; 49 pages (v15_29: 48); about 810 words added.
- All 49 numbered equations identical to v15_29; no existing label changed its number; one label added (`subsec:process_principle_uncollapse`).
- Overfull boxes: the two of about 1 pt that were already there.
- Companion papers (`Assembly_v2`, `Inference_v2`) contain no statement this makes stale; the Quick Reference was refreshed.
- `reproduce_v15_28.py` still passes 37 of 40 (the three noted exceptions are unchanged).

## The 24 changes, in source order

### 1. Axiom 7: each vector carries its own sort
**Serves:** R20, R36, R51

**Was:**
```latex
each carrying its own phase-color $\chi_i\in[0,2\pi)$ alongside $(r_i,\hat n_i)$ and sharing the atom's own sort $\tau$ --- $v_i$ together with that shared $\tau$ forming, per vector, the same 4-tuple \hyperref[subsec:axiom1]{Axiom~1} states, still capped at $r_i\le 1$, and positive:
```
**Now:**
```latex
each carrying its own phase-color $\chi_i\in[0,2\pi)$ alongside $(r_i,\hat n_i)$ and its own sort $\tau_i$ --- $v_i$ together with $\tau_i$ forming, per vector, the same 4-tuple \hyperref[subsec:axiom1]{Axiom~1} states, still capped at $r_i\le 1$, and positive:
```

### 2. Axiom 7: containment
**Serves:** R59, R20, R36

**Was:**
```latex
The vectors are held in groups; call each group a \emph{core}. $N$ is the number of cores and $Q$ the number of vectors --- the atom's info number.
```
**Now:**
```latex
The vectors of one atom may share a sort or differ in it. They are held in groups; call each group a \emph{core}. A vector is held by exactly one core, as a nucleus holds its electrons, and no verb moves a vector from one core to another. Which core holds which vector is part of the atom, recorded as a containment vector: for each vector, the position of its core in the atom's list of cores. $N$ is the number of cores and $Q$ the number of vectors --- the atom's info number.
```

### 3. Axiom 7: V_derived over every vector, per-sort share by sub-atom
**Serves:** R20, R36, R51, R43

**Was:**
```latex
$\chi_i$ does not enter this sum, the same way $\tau$ does not participate in $T$'s rotation --- available wherever a per-vector reading is named, silent in the seven metrics below, none of which is stated in terms of it.
```
**Now:**
```latex
$\chi_i$ does not enter this sum, the same way $\tau$ does not participate in $T$'s rotation; nor do $\tau_i$ or the core a vector sits in, so the sum runs over every vector of the atom, whatever its sort --- $\chi_i$ is available wherever a per-vector reading is named, silent in the seven metrics below, none of which is stated in terms of it. What one sort's vectors, or one core's, contribute is read from the sub-atom that holds them (Section~\ref{subsec:process_principle_uncollapse}); a sub-atom is another atom, with a $V_{\text{derived}}$ of its own.
```

### 4. Axiom 7: metrics read all vectors
**Serves:** R43

**Was:**
```latex
Seven scalar metrics follow from the same $Q$ informational vectors (those of the cores valid at the reading time, Section~\ref{subsec:meta_vectors}),
```
**Now:**
```latex
Seven scalar metrics follow from the same $Q$ informational vectors, all of them, whichever core holds each, among the cores valid at the reading time (Section~\ref{subsec:meta_vectors}),
```

### 5. Collapse: containment kept, no shared sort
**Serves:** R20, R36, R51, R59

**Was:**
```latex
each core exactly as its source held it and none merged with another, so $N=\sum_iN_i$ and $Q=\sum_iQ_i$, all sharing the atom's one sort $\tau$ (Axiom~7's own present requirement; see the open item below).
```
**Now:**
```latex
each core exactly as its source held it and none merged with another, every vector staying in the core that held it, so $N=\sum_iN_i$ and $Q=\sum_iQ_i$, whatever sorts the contributions carry.
```

### 6. Collapse: the identity handle is now the backward link
**Serves:** R18

**Was:**
```latex
and the precondition that makes the identity-handle proposal below coherent at all: a pointer back to sources that had been consumed would point at nothing.
```
**Now:**
```latex
and the precondition that makes the backward link of Section~\ref{subsec:meta_vectors} coherent at all: a pointer back to sources that had been consumed would point at nothing.
```

### 7. Collapse: what it keeps (lossless, with a clause)
**Serves:** R63 item 1, R18

**Was:**
```latex
\paragraph{Collapse is not idempotent.} $A\oplus A \ne A$ for every
```
**Now:**
```latex
\paragraph{What Collapse keeps.} Every vector, every count, and each core's own meta vectors survive in the result, which is the sense in which Collapse is lossless. Sources that agree in content and in every meta vector are interchangeable, and nothing distinguishes them because nothing needs to; sources that differ in any are told apart by them (UnCollapse, below).

\paragraph{Collapse is not idempotent.} $A\oplus A \ne A$ for every
```

### 8. Collapse: where N and Q are kept, containment is value
**Serves:** R59, R43

**Was:**
```latex
$N$ counts cores whether or not they hold vectors; $Q$ counts only vectors. Collapse adds both counts of its operands, and an empty core adds to $N$ and not to $Q$. Meta vectors are counted in neither.
```
**Now:**
```latex
$N$ counts cores whether or not they hold vectors; $Q$ counts only vectors. Collapse adds both counts of its operands, and an empty core adds to $N$ and not to $Q$. Meta vectors are counted in neither. The counts do not say which vector sits in which core: two atoms with the same vectors and the same $N$ and $Q$ may group them differently, and UnCollapse of one core then leaves different atoms. The grouping, the containment vector of Axiom~7, is part of the atom's value, and equality compares it (Section~\ref{subsec:meta_vectors}). The metrics of Axiom~7 read all of an atom's vectors and ignore which core holds each.
```

### 9. Collapse: grain
**Serves:** granularity (v48, v50)

**Was:**
```latex
\paragraph{What $N$ does not distinguish, and what would.}
```
**Now:**
```latex
\paragraph{Grain.} The grain of an atom is the partition of its vectors into cores: fine when each core holds one reading, coarse when a core holds a window of them. UnCollapse acts along the grain: it takes back a core, never less. A core may hold any number of vectors, and the seating --- the process that supplies the atom (Axiom~7) --- chooses how many, so a ten-minute atom may be ten cores of one reading or one core of ten, and these are different atoms. Grain is fixed when an atom is seated. It can be made coarser by seating again from the vectors, which is many-to-one: the metrics and $V_{\text{derived}}$ do not change, $N$ and $D$ do, and nothing records how the vectors were grouped before. No verb can make it finer; that needs the finer atom, if it is kept, or new readings. Seating again is the paper's own promotion of a result to a unit of the next level (Section~\ref{subsec:process_principle}).

\paragraph{What $N$ does not distinguish, and what would.}
```

### 10. Collapse across differing sorts: allowed
**Serves:** R20, R36, R51

**Was:**
```latex
\paragraph{Open: Collapse across differing sorts.} Axiom~7 currently requires every vector in one atom to share the atom's single $\tau$. Two atoms differing only in sort --- equal $r$, equal $\hat n$, different $\tau$ --- cannot yet be Collapsed under that requirement, and $\chi$ does not supply what is missing: $\chi$'s stated role is distinguishing several identities already sharing one direction (Axiom~1), not distinguishing sort. Admitting a per-vector $\tau_i$ would be the natural extension, paralleling $\chi_i$'s own per-vector role, but it is not adopted here and is left open.
```
**Now:**
```latex
\paragraph{Collapse across differing sorts.} Collapse takes atoms of any sorts. Each vector carries its own sort $\tau_i$ (Axiom~7), so two atoms differing only in sort Collapse into one atom of two cores, as they Bundle into a bowl of two seats. Nothing is combined, so no relation between the sorts is claimed (\hyperref[subsec:axiom0_admissibility]{Axiom~0}), and a sort inadmissible for Tier~1 may still be held at Tier~0. The atom's $V_{\text{derived}}$ and its seven metrics read every vector whatever its sort; what one sort contributes is read from the sub-atom of its vectors (Section~\ref{subsec:process_principle_uncollapse}). Whether the whole-atom reading means anything is for the use that reads it (Section~\ref{subsec:meta_vectors}).
```

### 11. UnCollapse: label for cross-reference
**Serves:** R18

**Was:**
```latex
\subsection{Process principle: UnCollapse}
```
**Now:**
```latex
\subsection{Process principle: UnCollapse}
\label{subsec:process_principle_uncollapse}
```

### 12. UnCollapse: the core leaves with its vectors
**Serves:** R59, granularity

**Was:**
```latex
it removes exactly the one core named, and $Q$ falls by that core's vector count, one for a single-vector core.
```
**Now:**
```latex
it removes exactly the one core named, with every vector the containment vector assigns to it and nothing else, and $Q$ falls by that core's vector count, one for a single-vector core. UnCollapse acts along the atom's grain: a core is the least it can take back.
```

### 13. UnCollapse: naming the core (identity key, local position)
**Serves:** R18, R19, R50

**Was:**
```latex
\paragraph{What UnCollapse requires to be well-defined.} Removing ``$A_k$'' presumes a specific core is named, the same way $\{A\}\setminus A$ already presumes a specific member. Where every core in $A_{\text{collapse}}$ differs in value, the named core is unambiguous. Where two or more cores share identical values --- genuinely distinct sources that happen to agree exactly, or two empty cores --- their values alone cannot distinguish which is meant. Resolving this needs an identity handle, $id_i$, carried alongside each core as a meta vector (Section~\ref{subsec:meta_vectors}), external to its geometric part the way a seat $\vec P$ is external to Axiom~1's own tuple: UnCollapse is value-exact without one, in every case where values alone suffice, and identity-exact with one, in the degenerate case where they do not. This mechanism is proposed, not adopted as an axiom here, and is left for the same later treatment as the seat of Section~\ref{sec:enclosure}.
```
**Now:**
```latex
\paragraph{Naming the core.} Removing ``$A_k$'' presumes a specific core is named, the same way $\{A\}\setminus A$ presumes a specific member. A core is named by its \emph{identity key}, a tuple of meta vectors it already carries --- its sort, its source link and its timestamp (Section~\ref{subsec:meta_vectors}) --- so no new kind of meta vector is needed, and the key never enters equality. Where every core differs in value, the value names it. Where two cores agree in value but differ in key, the key names it. Where two cores agree in value and in every meta vector, they are the same source twice, interchangeable, and removing either gives the same atom. Where a key matches cores that differ in content --- two readings seated under one label --- the key cannot say which is meant, and UnCollapse takes the core's position instead: its place in the atom's list of cores, counting from $0$, unique inside the atom and meaningless outside it. Collapse and UnCollapse renumber positions: Collapse shifts the second atom's positions by the first's $N$, and UnCollapse of position $k$ lowers every position above $k$ by one. A position needs no meta vector, so UnCollapse by position works on an atom whose meta vectors have been dropped. A series of cores is taken back by repeating UnCollapse, once for each. Each step gives a new atom with its own new timestamp and a backward link naming its operand, and the cores that survive keep theirs (Section~\ref{subsec:meta_vectors}).
```

### 14. Meta vectors: results are new atoms; a new paragraph separating identity (meta vectors) from containment (the grouping)
**Serves:** R50, R18, R59

**Was:**
```latex
so an atom's own birth and its cores' births are separate facts. $V_{\text{derived}}$ is held per core and for the atom.
```
**Now:**
```latex
so an atom's own birth and its cores' births are separate facts. The same holds for every result, not Collapse alone: a result is a new atom with its own new $V_{\text{timestamp}}$ and a backward $V_{\text{link}}$ naming its operands, and the cores that survive into it keep theirs. $V_{\text{derived}}$ is held per core and for the atom.

\paragraph{Identity and containment.} Two things in an atom are easy to mistake for each other, and only one is a meta vector. A core's \emph{identity} is read from meta vectors it already carries: the identity key, the tuple of its sort, its source link and its timestamp. It names the core, for UnCollapse and for any use that wishes to find it, no new kind of meta vector is needed, and it never enters equality. Its \emph{containment} is not a meta vector. The containment vector records which core holds which vector --- for each vector, the position of its core in the atom's list of cores (Axiom~7) --- and so is the grouping itself, part of what the atom is: equality compares it, and a meta vector never enters equality. The identity can be dropped, and UnCollapse still works by position; the grouping cannot be dropped without making a different atom.
```

### 15. Meta vectors: expired cores may be removed
**Serves:** R19

**Was:**
```latex
The atom itself is never changed: expiry is a reading and not an edit.
```
**Now:**
```latex
The atom itself is never changed: expiry is a reading and not an edit. An expired core is noise, and removing it is optional: UnCollapse, selected by expiry and repeated, takes each such core out with the vectors it holds and gives a new atom, in which $N$ and $D$ then fall.
```

### 16. Meta vectors: equality, two tests, exact
**Serves:** R68

**Was:**
```latex
\paragraph{Equality ignores meta vectors.} Equality of cores, for $\uplus$, for $D$, and for UnCollapse's value-exactness, is on content only. Two cores of equal content born at different times are the same value, though not the same source: the identity handle proposed under UnCollapse tells sources apart, and the value does not. Were the timestamp part of the value, every core would be unique by birth time, $N-D$ would always be $0$, and $A\uplus A=A$ would never apply: three contributions $A$, $B$, $A$ have $D=2$ by content and $D=3$ with timestamps. A bowl may carry meta vectors, and $\uplus$ does not read them; anything that wishes to may.
```
**Now:**
```latex
\paragraph{Equality.} Two vectors are equal when their coordinates agree, and two cores when they hold equal vectors. Two atoms are equal when their cores can be paired off so that paired cores are equal; so grouping counts, and two atoms with the same vectors grouped differently are not equal, as UnCollapse, $N$ and $D$ show (Section~\ref{subsec:process_principle_collapse}). Meta vectors never enter this equality, the one $\uplus$, $D$ and UnCollapse use. Two individuals are the \emph{same individual} when they are equal and their meta vectors agree too: the stricter test, as $==$ differs from ``is'' in a program. Two cores of equal content born at different times are equal but not the same individual: the identity key tells them apart and the value does not. Were the timestamp part of the value, every core would be unique by birth time, $N-D$ would always be $0$, and $A\uplus A=A$ would never apply: three contributions $A$, $B$, $A$ have $D=2$ by content and $D=3$ with timestamps. Equality is exact. Measured readings are made comparable when they are seated, by rounding to a stated resolution or by seating a window of readings as one core (grain, Section~\ref{subsec:process_principle_collapse}); the techniques belong to later papers. A bowl may carry meta vectors, and $\uplus$ does not read them; anything that wishes to may.
```

### 17. Table 3: Collapse, (word,num)
**Serves:** R20, R36, R51

**Was:**
```latex
$(\mathtt{word},\mathtt{num})$ & no & yes$^{\ddagger}$ & open$^{\P}$ &
```
**Now:**
```latex
$(\mathtt{word},\mathtt{num})$ & no & yes$^{\ddagger}$ & yes$^{\P}$ &
```

### 18. Table 3: Collapse, (num,word)
**Serves:** R20, R36, R51

**Was:**
```latex
$(\mathtt{num},\mathtt{word})$ & no & yes$^{\ddagger}$ & open$^{\P}$ &
```
**Now:**
```latex
$(\mathtt{num},\mathtt{word})$ & no & yes$^{\ddagger}$ & yes$^{\P}$ &
```

### 19. Table 3: Collapse, any other pair
**Serves:** R20, R36, R51

**Was:**
```latex
$(\tau_1,\tau_2)$ any other & no & yes$^{\ddagger}$ & open$^{\P}$ & open
```
**Now:**
```latex
$(\tau_1,\tau_2)$ any other & no & yes$^{\ddagger}$ & yes$^{\P}$ & open
```

### 20. Table 3 footnote: Collapse is yes for every pair
**Serves:** R20, R36, R51

**Was:**
```latex
$^{\P}$Collapse, unlike Bundle, is \emph{yes} only within one sort, not for every pair: $(\mathtt{num},\mathtt{num})$ is \emph{yes} because Collapse never computes the clock-trap sum that refuses Mix there --- it keeps every core exactly as it was rather than blending them, so there is no wrong arithmetic answer to produce. Cross-sort pairs are marked \emph{open}, not \emph{no}: this is the gap named in Section~\ref{subsec:process_principle_collapse} as not yet adopted --- Collapse across differing sorts needs a per-vector $\tau_i$ extension that Axiom~7 does not currently grant, and absence of that extension is a stated omission, not a proof of impossibility, unlike $\boxminus$'s own \emph{no} (Section~\ref{subsec:process_principle_unmix}).
```
**Now:**
```latex
$^{\P}$Collapse, like Bundle, is \emph{yes} for every pair, of one sort or of two: it keeps every core exactly as it was and computes nothing, so a sort mismatch has nothing to corrupt, and $(\mathtt{num},\mathtt{num})$ is \emph{yes} because Collapse never computes the clock-trap sum that refuses Mix there. It differs from Bundle in keeping the count. A Collapsed atom of several sorts claims no relation among them (\hyperref[subsec:axiom0_admissibility]{Axiom~0}); each vector carries its own $\tau_i$ (Axiom~7).
```

### 21. Table 3 footnote: Tier 0 sorts may be Collapsed
**Serves:** R20, R36, R51

**Was:**
```latex
it may be Bundled, and its other operators remain open until
```
**Now:**
```latex
it may be Bundled or Collapsed, and its other operators remain open until
```

### 22. Mix refusal paragraph: Collapse needs no shared sort
**Serves:** R20, R36, R51

**Was:**
```latex
since Collapse's only requirement is a shared sort (\hyperref[subsec:process_principle_collapse]{Process principle: Collapse}), not a shared direction.
```
**Now:**
```latex
since Collapse requires neither a shared direction nor a shared sort (\hyperref[subsec:process_principle_collapse]{Process principle: Collapse}).
```

### 23. Future Work: the open item on Collapse across sorts is closed
**Serves:** R20, R36, R51

**Was:**
```latex
\paragraph{Open: Collapse across differing sorts.} Stated in full where Collapse itself is defined (Section~\ref{subsec:process_principle_collapse}), not repeated here: Axiom~7 requires every vector in one Collapsed atom to share the atom's single $\tau$, so Collapse, unlike Bundle, cannot yet combine across sorts. Filed in this list so this roundup does not silently omit it.
```
**Now:**
```latex
(deleted)
```

### 24. Meta vectors: V_link names by the identity key
**Serves:** R18

**Was:**
```latex
an identifier such as the identity handle proposed under UnCollapse, or any other
```
**Now:**
```latex
an identifier such as the identity key of UnCollapse (Section~\ref{subsec:process_principle_uncollapse}), or any other
```
