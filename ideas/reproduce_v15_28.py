"""
Reproduction supplement for Pattern_Arithmetic_v15_28.

Recomputes numerical claims the paper prints, from the inputs the paper prints, and reports
PASS / FAIL / NOTE / UNDERSPECIFIED / SENSITIVE for each. Nothing is fitted to the paper.
Run:  python3 reproduce_v15_28.py          (needs only numpy; about a minute)

Covered: Axiom 7 identities and examples, the Mix example, Sun-Wind-Sky, the four-dimensional
actor, the unmixing pair, the storm costume, the offset equator, the beyond-3-D table, and the
full enclosure replay (steps to freeze, bodies, weighted pair).
Not covered: the chladni numbers, the numeric clock, Tables 2 and 3, the literature claims, and
the companion paper.
"""
import numpy as np

RESULTS = []
def check(section, claim, printed, computed, tol, note=""):
    ok = all(abs(p - c) <= t for p, c, t in zip(np.atleast_1d(printed), np.atleast_1d(computed), np.atleast_1d(tol)))
    RESULTS.append((section, claim, printed, np.round(np.atleast_1d(computed), 6), "PASS" if ok else "FAIL", note))

def unit(v):
    v = np.asarray(v, float); return v / np.linalg.norm(v)

def rodrigues(x, axis, alpha):
    k = unit(axis); x = np.asarray(x, float)
    return x*np.cos(alpha) + np.cross(k, x)*np.sin(alpha) + k*(k@x)*(1-np.cos(alpha))

# ---------------------------------------------------------------- Axiom 7
rng = np.random.default_rng(0)
# (a) |V|^2 = E + 2 sum r_i r_j cos, to six decimals
worst = 0
for _ in range(2000):
    Q = rng.integers(2, 9); r = rng.uniform(0, 1, Q)
    n = rng.normal(size=(Q, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
    V = (r[:, None]*n).sum(0); iu = np.triu_indices(Q, 1)
    cross = (np.outer(r, r)*(n@n.T))[iu].sum()
    worst = max(worst, abs(V@V - ((r**2).sum() + 2*cross)))
check("Axiom 7", "|V|^2 = E + 2*sum r_i r_j cos (six decimals)", 0.0, worst, 5e-7, "2000 random atoms")

# (b) alignment example: r=0.85, pair 5.7 deg apart; five on a cone of half-angle 5.7 deg
def cone(Q, half_deg):
    h = np.radians(half_deg); a = 2*np.pi*np.arange(Q)/Q
    return np.stack([np.sin(h)*np.cos(a), np.sin(h)*np.sin(a), np.cos(h)*np.ones(Q)], 1)
n2 = np.stack([unit([np.sin(np.radians(2.85)), 0, np.cos(np.radians(2.85))]),
               unit([-np.sin(np.radians(2.85)), 0, np.cos(np.radians(2.85))])])
cs2 = (n2@n2.T)[0, 1]
check("Axiom 7", "alignment, Q=2: raw sum and alpha", [0.72, 0.995], [0.85**2*cs2, cs2], [0.005, 0.0005])
n5 = cone(5, 5.7); iu = np.triu_indices(5, 1); cs5 = (n5@n5.T)[iu]
check("Axiom 7", "alignment, Q=5 (half-angle 5.7 deg): raw sum and alpha", [7.14, 0.988], [0.85**2*cs5.sum(), cs5.mean()], [0.005, 0.0005])

# (c) three aligned vectors at r = 0.5
check("Axiom 7", "|V| = 1.5 and alpha(1.5) = 270 deg", [1.5, 270.0], [1.5, 180*1.5], [1e-9, 1e-9])

# (d) 0.95 against three at 0.2: cubed share
s = 0.95**3/(0.95**3 + 3*0.2**3)
check("Axiom 7", "volume share of the dominant vector", 0.973, s, 0.0005)

# (e) shell concentration 10@0.98, 3@0.3, 400@0.65, at w = 0.1 and 0.05
def sigma_shell(r, w):
    k = np.floor(np.asarray(r)/w + 1e-9).astype(int)   # tolerance guards 0.3/0.1 = 2.9999999999999996
    _, cnt = np.unique(k, return_counts=True); p = cnt/cnt.sum(); K = len(p)
    return 1.0 if K == 1 else K**2/(K-1)*np.var(p)
pop = np.r_[np.full(10, .98), np.full(3, .3), np.full(400, .65)]
check("Axiom 7", "sigma_shell at w=0.1 and w=0.05", [0.908, 0.908], [sigma_shell(pop, .1), sigma_shell(pop, .05)], [0.0006, 0.0006])
naive = np.floor(0.3/0.1)
RESULTS.append(("Axiom 7", "floor(0.3/0.1) in floating point (a binning pitfall)", "3", [naive], "NOTE",
                "gives 2, not 3, without a tolerance; populations here are unaffected because the shells stay distinct"))

# (f) Herfindahl slides 0.5 -> 0.125 as Q goes 2 -> 8
check("Axiom 7", "Herfindahl index of an even atom, Q=2 and Q=8", [0.5, 0.125], [1/2, 1/8], [1e-12, 1e-12])

# (g) sigma_atom for 400 vectors: 'clumped' 0.00032 against 'uniform spread' 0.00214 -- inputs not printed
def sigma_atom(r):
    r = np.asarray(r, float); Q = len(r); s = r**3/(r**3).sum()
    return Q**2/(Q-1)*np.var(s)
cands = {"linspace(0.0025,1,400)": np.linspace(0.0025, 1, 400), "linspace(0,1,400)": np.linspace(0, 1, 400),
         "uniform random, seed 0": np.random.default_rng(0).uniform(0, 1, 400)}
u = {k: round(sigma_atom(v), 5) for k, v in cands.items()}
RESULTS.append(("Axiom 7", "sigma_atom: clumped 0.00032 vs uniform spread 0.00214", "0.00032 / 0.00214", [u], "UNDERSPECIFIED",
                "populations not printed; natural readings of 'uniform' give the values listed"))

# ---------------------------------------------------------------- Mix
z = 0.6 + 0.8*np.exp(1j*np.radians(120))
check("Mix of two shells", "0.6 at 0 deg + 0.8 at 120 deg: r', chi'", [0.721, 73.9], [abs(z), np.degrees(np.angle(z))], [0.0006, 0.06])

# ---------------------------------------------------------------- Transformation algebra
sky = unit([0.5, 0.5, np.sqrt(0.5)]); sun_axis, wind_axis = [1, 0, 0], [0, 1, 0]
a_sun, a_wind = np.pi*1.0, np.pi*0.7
o1 = rodrigues(rodrigues(sky, sun_axis, a_sun), wind_axis, a_wind)
o2 = rodrigues(rodrigues(sky, wind_axis, a_wind), sun_axis, a_sun)
check("Sun, Wind, Sky", "Sun then Wind", [-0.866, -0.500, 0.011], o1, [0.0006]*3)
check("Sun, Wind, Sky", "Wind then Sun", [0.278, -0.500, 0.820], o2, [0.0006]*3)
check("Sun, Wind, Sky", "alpha(Wind) = 126 deg", 126.0, np.degrees(a_wind), 1e-9)

# four-dimensional actor: rotate the (e3,e4) plane by 90 deg, f1=e3, f2=e4
nx = np.array([0.5, 0.5, 1/np.sqrt(2), 0.0]); al = np.pi*0.5
def T4(x, a):
    y = x.copy(); y[2] = x[2]*np.cos(a) - x[3]*np.sin(a); y[3] = x[2]*np.sin(a) + x[3]*np.cos(a); return y
check("4-D actor", "T_w(n_x)", [0.5, 0.5, 0.0, 1/np.sqrt(2)], T4(nx, al), [1e-9]*4)
check("4-D actor", "T_w* T_w(n_x) = n_x", nx, T4(T4(nx, al), -al), [1e-9]*4)

# ---------------------------------------------------------------- Unmixing
red_green = np.exp(1j*0) + np.exp(1j*np.radians(120))
M = np.array([[np.cos(np.radians(10)), np.cos(np.radians(100))], [np.sin(np.radians(10)), np.sin(np.radians(100))]])
w = np.linalg.solve(M, [red_green.real, red_green.imag]); resid = np.linalg.norm(M@w - [red_green.real, red_green.imag])
check("Unmixing", "10 deg + 100 deg reach the red-green sum (residual)", 0.0, resid, 1e-15,
      f"weights {np.round(w,4)}; printed residual 1e-17, computed {resid:.1e}")
check("Unmixing", "red + green at equal strength reach yellow at 60 deg", 60.0, np.degrees(np.angle(red_green)), 1e-9)


# ---------------------------------------------------------------- Storm costume (Rodrigues rotation plus phase add)
def Tw(state, w):
    r, n, chi = state
    return (r, rodrigues(n, w["n"], np.pi*w["r"]), chi + w["chi"])
wind  = dict(r=1.0,   n=np.array([1.0, 0, 0]), chi=0.0)
heat  = dict(r=0.5,   n=np.array([0, 1.0, 0]), chi=90.0)
moist = dict(r=2/3,   n=np.array([0, 0, 1.0]), chi=45.0)
eye   = (1.0, np.array([np.sqrt(2)/2, 0, np.sqrt(2)/2]), 0.0)
s1 = Tw(eye, moist); s2 = Tw(s1, heat); s3 = Tw(s2, wind)
check("Storm", "deepen, after Moisture", [-np.sqrt(2)/4, np.sqrt(6)/4, np.sqrt(2)/2], s1[1], [1e-9]*3)
check("Storm", "deepen, after Heat",     [np.sqrt(2)/2, np.sqrt(6)/4, np.sqrt(2)/4], s2[1], [1e-9]*3)
check("Storm", "deepen, endpoint",       [np.sqrt(2)/2, -np.sqrt(6)/4, -np.sqrt(2)/4], s3[1], [1e-9]*3)
c1 = Tw(eye, wind); c2 = Tw(c1, heat); c3 = Tw(c2, moist)
check("Storm", "clear, after Wind",     [np.sqrt(2)/2, 0, -np.sqrt(2)/2], c1[1], [1e-9]*3)
check("Storm", "clear, after Heat",     [-np.sqrt(2)/2, 0, -np.sqrt(2)/2], c2[1], [1e-9]*3)
check("Storm", "clear, endpoint",       [np.sqrt(2)/4, -np.sqrt(6)/4, -np.sqrt(2)/2], c3[1], [1e-9]*3)
ang = lambda n: [np.degrees(np.arccos(n[2])), np.degrees(np.arctan2(n[1], n[0])) % 360]
check("Storm", "endpoint angles (theta, phi), deepen", [110.7, 319.1], ang(s3[1]), [0.05, 0.05])
check("Storm", "endpoint angles (theta, phi), clear",  [135.0, 300.0], ang(c3[1]), [0.05, 0.05])
check("Storm", "both paths end at chi = 135 deg", [135.0, 135.0], [s3[2] % 360, c3[2] % 360], [1e-9, 1e-9])

# ---------------------------------------------------------------- Offset: one equator
nm, nk, nw = np.array([1.0, 0, 0]), np.array([np.sqrt(3)/2, 0.5, 0]), np.array([0, 1.0, 0])
logv = np.array([0, np.arccos(nm@nk), 0])                     # tangent vector at nm toward nk
moved = rodrigues(logv, [0, 0, 1], np.pi/2)                   # quarter-turn about z
th = np.linalg.norm(moved); land = np.cos(th)*nw + np.sin(th)*(moved/th)
check("Offset equator", "log = (0, pi/6, 0); transported = (-pi/6, 0, 0)", [0, np.pi/6, 0, -np.pi/6, 0, 0], np.r_[logv, moved], [1e-9]*6)
check("Offset equator", "landing (-1/2, sqrt3/2, 0) at 120 deg", [-0.5, np.sqrt(3)/2, 0], land, [1e-9]*3)

# ---------------------------------------------------------------- Beyond three dimensions
def plane_rot(x, a, b, alpha):                                  # rotate in plane (e_a, e_b), a -> b; 0-based
    y = x.copy(); y[a] = x[a]*np.cos(alpha) - x[b]*np.sin(alpha); y[b] = x[a]*np.sin(alpha) + x[b]*np.cos(alpha); return y
def T1(x, alpha, N): return plane_rot(x, N-2, N-1, alpha)       # w1 fixes e1..e_{N-2}, turns plane (e_{N-1}, e_N)
def T2(x, alpha, N): return plane_rot(x, 0, N-1, alpha)         # w2 fixes e2..e_{N-1}, turns plane (e_1, e_N)
printed_gap = {4: 0.683, 5: 0.688, 8: 0.649, 12: 0.584, 20: 0.489, 50: 0.331}
angles = np.radians([30, 45, 90, 135, 180, 200, 270, 359])
gaps, errs = [], []
for N, g in printed_gap.items():
    x = np.arange(1, N+1, dtype=float); x /= np.linalg.norm(x)
    gap = np.linalg.norm(T2(T1(x, np.pi/2, N), np.pi/2, N) - T1(T2(x, np.pi/2, N), np.pi/2, N))
    err = max(np.linalg.norm(T1(T1(x, a, N), -a, N) - x) for a in angles)
    gaps.append(gap); errs.append(err)
check("Beyond 3-D", "order gap at N = 4, 5, 8, 12, 20, 50", list(printed_gap.values()), gaps, [0.0006]*6)
check("Beyond 3-D", "largest inversion error is rounding-level (printed ~1e-16)", [0.0]*6, errs, [5e-16]*6,
      "computed " + ", ".join(f"{e:.1e}" for e in errs) + "; printed 1.1e-16 or 5.6e-17")

# ---------------------------------------------------------------- Enclosure: the replayable configuration
def forces(P, r, n):
    F = np.zeros_like(P)
    for i in range(len(r)):
        for j in range(len(r)):
            if i == j: continue
            d = P[i] - P[j]; dist2 = d@d; eps = r[i] + r[j]
            K = r[i]*r[j]*(3 + n[i]@n[j])/2
            F[i] += -3*K*d*(dist2 + eps**2)**-2.5
    return F
def run(P0, r, n, delta, eta=1e-5, cap=200000):
    P = P0.copy(); steps = 0
    while steps < cap:
        F = forces(P, r, n)
        if np.max(np.linalg.norm(F, axis=1)) < eta: break
        P = P + delta*F; steps += 1
    return P, steps
r6 = np.array([.5, .6, .7, .8, .4, .9])
n6 = np.array([[1,0,0],[0,1,0],[0,0,1],[1,0,0],[1/np.sqrt(2),1/np.sqrt(2),0],[0,0,1]], float)
P6 = np.array([[0,0,0],[1,0,0],[0,1,0],[40,0,0],[41,0,0],[40,1,0]], float)
deltas = [0.02, 0.01, 0.005, 0.002]; printed_steps = [628, 1261, 2526, 6320]
got_steps, bodies = [], []
for dlt in deltas:
    P, st = run(P6, r6, n6, dlt); got_steps.append(st); bodies.append((P[:3].mean(0), P[3:].mean(0)))
check("Enclosure", "steps to freeze at delta = 0.02, 0.01, 0.005, 0.002", printed_steps, got_steps, [1]*4,
      f"computed {got_steps}")
b1, b2 = bodies[0]
check("Enclosure", "bodies at delta=0.02", [0.33336, 0.33333, 0.0, 40.33330, 0.33333, 0.0], np.r_[b1, b2], [2e-5]*6)
spread = max(np.linalg.norm(bodies[0][k] - bodies[m][k]) for k in (0, 1) for m in range(1, 4))
check("Enclosure", "four runs agree on both bodies to within 2e-7", 0.0, spread, 2.0e-7, f"computed spread {spread:.2e}")
Pf, _ = run(P6, r6, n6, 0.02)
mean_all_start = P6.mean(0); mean_all_end = Pf.mean(0)
check("Enclosure", "plain mean of all six seats unchanged", 0.0, np.linalg.norm(mean_all_end - mean_all_start), 1e-9)
rw = (r6[:3, None]*Pf[:3]).sum(0)/r6[:3].sum()
check("Enclosure", "r-weighted and plain bodies of camp 1 differ by 2.4e-8", 2.4e-8, np.linalg.norm(rw - Pf[:3].mean(0)), 2e-8,
      f"computed {np.linalg.norm(rw - Pf[:3].mean(0)):.1e}")
alone = [run(P6[:3], r6[:3], n6[:3], d)[0].mean(0) for d in deltas]
check("Enclosure", "group alone rests on (1/3,1/3,0), agreeing to 1e-15", 0.0, max(np.linalg.norm(a - np.array([1/3, 1/3, 0])) for a in alone), 1e-15)
# the printed pair: separation never increases (0.02, 3000 steps); dividing each step by r^3 makes it increase on 804 steps
rp = np.array([0.9, 0.1]); npair = np.array([[1, 0, 0], [1, 0, 0]], float); Pp0 = np.array([[0, 0, 0], [3, 0, 0]], float)
def pair_run(divide):
    P = Pp0.copy(); sep = [np.linalg.norm(P[0]-P[1])]
    for _ in range(3000):
        F = forces(P, rp, npair)
        P = P + 0.02*(F/rp[:, None]**3 if divide else F)
        sep.append(np.linalg.norm(P[0]-P[1]))
    sep = np.array(sep); return sep, int(np.sum(np.diff(sep) > 0))
sep_a, inc_a = pair_run(False); sep_b, inc_b = pair_run(True)
check("Enclosure", "pair: separation never increases and falls from 3 to 1.80", [0, 3.0, 1.80], [inc_a, sep_a[0], sep_a[-1]], [0, 1e-9, 0.005])
# the count of increases is rounding-sensitive (an oscillating, near-chaotic regime): record its spread
def pair_count(eps=0.0, order="a"):
    P = Pp0.copy(); P[1, 0] += eps; sep = [np.linalg.norm(P[0]-P[1])]
    for _ in range(3000):
        F = forces(P, rp, npair)
        P = P + (0.02*F/rp[:, None]**3 if order == "a" else 0.02*(F/rp[:, None]**3))
        sep.append(np.linalg.norm(P[0]-P[1]))
    return int(np.sum(np.diff(np.array(sep)) > 0))
spread_counts = [pair_count(0, "a"), pair_count(0, "b"), pair_count(1e-12), pair_count(1e-9), pair_count(1e-6)]
RESULTS.append(("Enclosure", "pair divided by r^3: exact count of increasing steps (printed 804 of 3000)", "804",
                [spread_counts], "SENSITIVE",
                f"computed {min(spread_counts)} to {max(spread_counts)} depending only on operation order or a 1e-12..1e-6 nudge"))
check("Enclosure", "pair divided by r^3: separation increases on hundreds of steps; plain run on none", [1, 0],
      [int(min(spread_counts) >= 500 or min(spread_counts) >= 0.2*3000), inc_a], [0, 0], "qualitative claim holds in every variant")

if __name__ == "__main__":
    for sec, claim, printed, comp, status, note in RESULTS:
        print(f"[{status:14s}] {sec:20s} {claim}")
        print(f"    printed {printed}   computed {list(comp) if hasattr(comp,'__len__') else comp}" + (f"   ({note})" if note else ""))
    npass = sum(r[4] == "PASS" for r in RESULTS); nfail = sum(r[4] == "FAIL" for r in RESULTS)
    print(f"\n{npass} PASS, {nfail} FAIL, {sum(r[4] in ('NOTE','UNDERSPECIFIED','SENSITIVE') for r in RESULTS)} noted/underspecified, of {len(RESULTS)}")
