# The Cross Section — Rolling Synthesis, week ending 2026-08-31

A methods-and-precision week with few collaboration headlines but several durable trajectories. The dominant arc was **strong-CP**, which opened with a lattice confirmation of the problem and closed with the axion cosmology/detection side of the same story. Running underneath nearly every day was the **autodiff/GPU tooling wave**, now saturating simulation, amplitude analysis, likelihood fitting, and event generation alike. Collider results were overwhelmingly SMEFT-framed and null-or-clean; the one refusing anomaly, as ever, was **R(D\*)**. Two genuine experimental firsts (CMS, LHCb) landed on the final day without disturbing the SM.

## Running themes

**Strong-CP, lattice → cosmology (heating up).** The week's clearest spine. Blum et al. extracted the nEDM from topological-charge density and confirmed strong-CP is real, $|\bar\theta|\lesssim10^{-11}$ ([arXiv:2608.22587](https://arxiv.org/abs/2608.22587)); Li et al. followed with the first direct lattice $\tilde g_{\pi NN}$, the hadronic coupling one rung up ([arXiv:2608.23685](https://arxiv.org/abs/2608.23685)). By 08-31 the thread had moved to axions: Gorghetto et al. evade the domain-wall problem via PQ-violating operators and predict an nEDM within two orders of current limits ([arXiv:2608.27553](https://arxiv.org/abs/2608.27553)), alongside Dvali et al.'s fiber-based ALP detection ([arXiv:2608.27551](https://arxiv.org/abs/2608.27551)) and Di Vecchia et al.'s 1PI revisit ([arXiv:2608.28253](https://arxiv.org/abs/2608.28253)). Watch for the predicted nEDM signal as an experimental target.

**The tooling wave (dominant, still accelerating).** Differentiable/GPU infrastructure appeared every day: calibrated normalizing-flow fast-sim ([arXiv:2608.21509](https://arxiv.org/abs/2608.21509)), differentiable Parnassus ([arXiv:2608.22873](https://arxiv.org/abs/2608.22873)) and neutrino generator ADoNIS ([arXiv:2608.25107](https://arxiv.org/abs/2608.25107)), GPU photon transport for DUNE ([arXiv:2608.27306](https://arxiv.org/abs/2608.27306)), and the standout RABBIT differentiable profile-likelihood minimizer ([arXiv:2608.26376](https://arxiv.org/abs/2608.26376)). A sub-current is **amplitude analysis getting industrialized**: SINNs learning $\pi\pi$ amplitudes under unitarity/analyticity/crossing plus dispersive pole extraction ([arXiv:2608.23750](https://arxiv.org/abs/2608.23750), [arXiv:2608.23738](https://arxiv.org/abs/2608.23738)), and the 100×-faster GPU PWA framework CTPWA ([arXiv:2608.25963](https://arxiv.org/abs/2608.25963)).

**EFT-as-default on top/electroweak data (steady).** Englert et al. read single-top/$tH$ rate shifts as a coherent SMEFT pattern no minimal UV multiplet reproduces ([arXiv:2608.21510](https://arxiv.org/abs/2608.21510)); ATLAS's full-Run-2 $tZq$ measurement folded straight into dimension-6 limits ([arXiv:2608.25476](https://arxiv.org/abs/2608.25476)); FCC-ee third-generation FCNC projections extended the reading to future machines ([arXiv:2608.27183](https://arxiv.org/abs/2608.27183)).

**Dark matter breadth (steady).** A wide 08-28 spread — paleo-detectors, IceCube annihilation limits reaching the thermal benchmark ([arXiv:2608.26258](https://arxiv.org/abs/2608.26258)), sub-GeV direct/indirect complementarity ([arXiv:2608.26467](https://arxiv.org/abs/2608.26467)), and revived baryon–DM coincidence models — extended 08-31 with celestial and astrometric-lensing probes ([arXiv:2608.27957](https://arxiv.org/abs/2608.27957), [arXiv:2608.27557](https://arxiv.org/abs/2608.27557)).

**Quantum observables at colliders (heating up).** The magic/entanglement program went precision with the first NLO EW corrections to entanglement and stabilizer Rényi entropy in lepton collisions ([arXiv:2608.27559](https://arxiv.org/abs/2608.27559)), joined by quantum-circuit Drell-Yan and QML benchmarking.

## Turning points

- **[arXiv:2608.22587](https://arxiv.org/abs/2608.22587)** — lattice nEDM confirms strong-CP and demonstrates a method extendable to other CP-violating operators; set the week's agenda.
- **[arXiv:2608.25705](https://arxiv.org/abs/2608.25705)** — Braathen et al.'s model-independent higher-order class shifts the Higgs $\kappa_3$ bound from 6.1 to ~4.9; a genuine correction to how self-coupling limits are read, with a public tool.
- **[arXiv:2608.22845](https://arxiv.org/abs/2608.22845)** — Tomalak et al.'s $\Delta(1232)$ contribution restores power counting and nulls the $g_A$ radiative shift, feeding the lattice-vs-experiment $g_A$ debate.
- **[arXiv:2608.28377](https://arxiv.org/abs/2608.28377)** — CMS's first leptoquark search via muon–quark scattering: a new production mode, not another pair-production limit.

## Open questions

- **R(D\*) refuses to soften.** Chen et al.'s exclusive $|V_{cb}|=(39.18\pm0.47)\times10^{-3}$ yields an SM $R(D^{(*)})$ region with "little overlap" with data ([arXiv:2608.24332](https://arxiv.org/abs/2608.24332)). Against a consolidating-on-nulls flavor front, this is the standout tension — watch N³LO $|V_{ub}|$ progress ([arXiv:2608.28172](https://arxiv.org/abs/2608.28172)) too.
- **Significance accounting.** Zhang et al.'s procedural reading of the look-elsewhere effect (3σ global → ~4σ binary) ([arXiv:2608.24872](https://arxiv.org/abs/2608.24872)) continues last week's search-budget thread; expect it invoked whenever new bumps appear.
- **Strangeness horn unresolved.** NA61's system-size ladder shows no single framework fits the $K^+/\pi^+$ horn, with a $3.7\sigma$ enhancement step ([arXiv:2608.28189](https://arxiv.org/abs/2608.28189)).
- **Glueball identity of X(2370)** — competing radial-hybrid vs mixing interpretations, all proposing (not settling) BESIII/Belle II discriminators.

## Recurring references

- **[arXiv:2608.22587](https://arxiv.org/abs/2608.22587)** & **[arXiv:2608.23685](https://arxiv.org/abs/2608.23685)** — the strong-CP lattice pair (nEDM + $\tilde g_{\pi NN}$); anchor for the axion follow-ons.
- **[arXiv:2608.27553](https://arxiv.org/abs/2608.27553)** — Gorghetto et al.'s domain-wall evasion with a testable nEDM prediction.
- **[arXiv:2608.24332](https://arxiv.org/abs/2608.24332)** — the reference $|V_{cb}|$/R(D*) point.
- **[arXiv:2608.26376](https://arxiv.org/abs/2608.26376)** (RABBIT) & **[arXiv:2608.25963](https://arxiv.org/abs/2608.25963)** (CTPWA) — the week's flagship tooling anchors.
- **[arXiv:2608.23750](https://arxiv.org/abs/2608.23750)** — S-matrix-informed neural amplitudes, transferable beyond $\pi\pi$.
