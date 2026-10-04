"""
Inference probes for Pattern_Arithmetic_v15_28 (the T-step of Section 4, in three dimensions).

Paper 1 gives the forward map: an actor w = (r_w, n_w, chi_w) turns an occupant x about n_w by angle pi*r_w and
adds chi_w to its phase. Inference has to go the other way: guess the actors, or the path, from what was observed.
Two questions about that backward direction:

  1. One observed step x -> y. How many actors (axis, strength) explain it exactly?
  2. How often would a *random* actor from a bowl explain a step to within a tolerance, by chance alone?

Scope: three dimensions; x and y random on the sphere; fixed seed. Probes, not theorems of the paper.
Run:  python3 inference_probe_v15_28.py   (numpy only; a few seconds)
"""
import numpy as np
rng = np.random.default_rng(7)

def unit(v): return v/np.linalg.norm(v, axis=-1, keepdims=True)
def rot(x, k, a):                                   # Rodrigues rotation, vectorised; x, k: (M,3), a: (M,)
    a = a[:, None]
    return x*np.cos(a) + np.cross(k, x)*np.sin(a) + k*(k*x).sum(-1, keepdims=True)*(1 - np.cos(a))

# ------------------------------------------------------------------ 1. one step leaves the actor underdetermined
M = 20000
x = unit(rng.normal(size=(M, 3))); y = unit(rng.normal(size=(M, 3)))
s = np.arccos(np.clip((x*y).sum(-1), -1, 1))        # angle between before and after
d = unit(x - y); e1 = unit(np.cross(d, rng.normal(size=(M, 3)))); e2 = np.cross(d, e1)
worst = 0.0; rmin = np.full(M, 9.0)
for phi in np.linspace(0, np.pi, 7, endpoint=False) + 0.1:
    k = np.cos(phi)*e1 + np.sin(phi)*e2             # any axis perpendicular to (x - y) turns x onto y
    px = x - (x*k).sum(-1, keepdims=True)*k; py = y - (y*k).sum(-1, keepdims=True)*k
    a = np.arctan2((k*np.cross(px, py)).sum(-1), (px*py).sum(-1))
    k_use = np.where(a[:, None] < 0, -k, k); a_use = np.abs(a)      # flip the axis so the angle lies in [0, pi]
    worst = max(worst, np.linalg.norm(rot(x, k_use, a_use) - y, axis=-1).max())
    rmin = np.minimum(rmin, a_use/np.pi)                            # strength r = angle / pi
ex = np.where((s > np.radians(59)) & (s < np.radians(61)))[0][0]
print("1. One observed step x -> y")
print(f"   {M} random pairs, 7 axes each on the great circle of axes perpendicular to (x - y)")
print(f"   every axis maps x onto y exactly: largest error {worst:.1e}")
print(f"   the strength needed depends on the axis chosen: from s/pi (axis x cross y) up to 1 (axis x+y, a half turn)")
print(f"   example, {np.degrees(s[ex]):.0f} deg apart: from {s[ex]/np.pi:.3f} to 1.000")
print("   The phase part IS identified: chi_w = chi_after - chi_before. The axis and strength are not.")

# ------------------------------------------------------------------ 2. chance explanation of a step
M = 400000
x = unit(rng.normal(size=(M, 3))); y = unit(rng.normal(size=(M, 3)))
k = unit(rng.normal(size=(M, 3))); r = rng.uniform(0, 1, M)
sep = np.degrees(np.arccos(np.clip((rot(x, k, np.pi*r)*y).sum(-1), -1, 1)))
print("\n2. Chance that a random actor (axis uniform, strength uniform on [0,1]) explains a step within a tolerance")
print(f"   {'tolerance':>10} | {'one actor':>9} | {'cap fraction (1-cos)/2':>22} | {'bowl of 10':>10} | {'bowl of 100':>11}")
for rho in (2, 5, 10, 20):
    p = (sep < rho).mean(); base = (1 - np.cos(np.radians(rho)))/2
    print(f"   {rho:>8} deg | {p:>9.5f} | {base:>22.5f} | {1 - (1 - p)**10:>10.3f} | {1 - (1 - p)**100:>11.3f}")
print("   For steps between arbitrary states the chance of an explanation is the area of the tolerance cap,")
print("   whatever the strengths; a larger bowl or a looser tolerance explains more by chance alone.")
