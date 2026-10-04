"""
Assembly probes for Pattern_Arithmetic_v15_28 (Axiom 6 energy, Section 10 descent and freeze).

Three questions, answered with the paper's own pair energy U_AB and step rule P_i <- P_i + delta*F_i:
  A. Is the step size stable?   (explicit Euler needs delta < 2/lambda_max; a too-large delta silently corrupts results)
  B. Does the energy alone sort a mixed population by content?   (two kinds with antipodal directions, the most
     favourable case; freeze at eta, then count camps at several census cuts)
  C. Where do free atoms gather?   (random strengths and directions; the paper's descent conserves the plain mean)

Scope: equal strengths and two antipodal kinds in B; one family of random seats; fixed seeds. These are probes,
not a general result. Run:  python3 assembly_probe_v15_28.py   (numpy only; about a minute)
"""
import numpy as np

def forces(P, r, n):
    diff = P[:, None, :] - P[None, :, :]; d2 = (diff**2).sum(-1); eps = r[:, None] + r[None, :]
    K = r[:, None]*r[None, :]*(3 + n@n.T)/2
    coef = -3*K*(d2 + eps**2)**-2.5; np.fill_diagonal(coef, 0)
    return (coef[:, :, None]*diff).sum(1)

def components(P, cut):
    N = len(P); near = np.linalg.norm(P[:, None] - P[None], axis=-1) < cut; lab = -np.ones(N, int); c = 0
    for i in range(N):
        if lab[i] < 0:
            stack = [i]; lab[i] = c
            while stack:
                j = stack.pop()
                for k in np.where(near[j] & (lab < 0))[0]: lab[k] = c; stack.append(k)
            c += 1
    return lab, c

N = 40
r = np.full(N, 0.5)
kind = np.r_[np.zeros(N//2, int), np.ones(N//2, int)]
n = np.where(kind[:, None] == 0, [1.0, 0, 0], [-1.0, 0, 0])

# ---- A. stability
P = 1e-6*np.random.default_rng(0).normal(size=(N, 3)); f0 = forces(P, r, n); J = np.zeros((3*N, 3*N)); h = 1e-6
for i in range(N):
    for k in range(3):
        Q = P.copy(); Q[i, k] += h; J[:, 3*i + k] = ((forces(Q, r, n) - f0)/h).ravel()
lam = np.abs(np.linalg.eigvalsh((J + J.T)/2)).max()
print(f"A. stiffness eigenvalue at the collapsed state: {lam:.1f}; explicit Euler is stable only for delta < {2/lam:.4f}")
print("   delta = 0.05 is therefore unstable for 40 atoms; this script uses delta = 0.005.\n")

# ---- B. freeze at eta = 1e-3, then census at several cuts
delta, eta = 0.005, 1e-3
cuts = [0.05, 1e-2, 1e-3, 1e-4, 1e-5]
rows = []
for seed in range(10):
    P = np.random.default_rng(seed).uniform(0, 4, (N, 3))
    while np.linalg.norm(forces(P, r, n), axis=1).max() >= eta:
        P = P + delta*forces(P, r, n)
    centres = [P[kind == k].mean(0) for k in (0, 1)]
    within = max(np.linalg.norm(P[kind == k] - P[kind == k].mean(0), axis=1).max() for k in (0, 1))
    row = [np.linalg.norm(P - P.mean(0), axis=1).max(), np.linalg.norm(centres[0] - centres[1]), within]
    for cut in cuts:
        lab, c = components(P, cut); row += [c, np.mean([len(set(kind[lab == k])) == 1 for k in range(c)])]
    rows.append(row)
o = np.array(rows)
print("B. 40 atoms in a cube of side 4, two antipodal kinds, equal strength 0.5; frozen at eta = 1e-3 (10 seeds)")
print(f"   size of the whole pile              : {o[:, 0].mean():.2e}")
print(f"   distance between the kinds' centres : {o[:, 1].mean():.2e}")
print(f"   spread inside a kind                : {o[:, 2].mean():.2e}   (ratio between/within {np.mean(o[:, 1]/o[:, 2]):.1f})")
print("   census cut | camps | share of camps holding one kind only")
for i, cut in enumerate(cuts):
    print(f"   {cut:>9.0e} | {o[:, 3 + 2*i].mean():5.1f} | {o[:, 4 + 2*i].mean():.2f}")

# ---- C. where free atoms gather
res = []
for seed in range(8):
    rng = np.random.default_rng(100 + seed); M = 30
    rr = rng.uniform(0.2, 0.95, M); v = rng.normal(size=(M, 3)); nn = v/np.linalg.norm(v, axis=1)[:, None]
    P0 = rng.uniform(0, 6, (M, 3)); plain = P0.mean(0); weighted = (rr[:, None]*P0).sum(0)/rr.sum(); P = P0.copy()
    for _ in range(3000): P = P + 0.01*forces(P, rr, nn)
    res.append((np.linalg.norm(P.mean(0) - plain), np.linalg.norm(plain - weighted)))
res = np.array(res)
print(f"\nC. random strengths 0.2-0.95 and random directions, 30 atoms, 8 seeds")
print(f"   centre of the pile vs plain mean of the starting seats : {res[:, 0].max():.1e} (largest)")
print(f"   plain mean vs strength-weighted mean of the seats      : {res[:, 1].mean():.3f} (average)")
print("   the pile forms where the seats' plain mean was; strength and direction do not move it.")
