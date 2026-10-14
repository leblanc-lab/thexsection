# The Cross Section: rolling synthesis, week ending 2026-10-14

This week covers four digests (10-08, 10-09, 10-12, 10-14). The busiest thread was the **LZ 248 keV excess**. Model-building on it peaked at five papers on 10-14, and the solar-neutrino bound went from something papers ignored to a design input and then to a proposed test. **Hadron spectroscopy** moved toward threshold and rescattering explanations: three separate results weakened exotic-state readings. **Phase-transition and gravitational-wave work** gained both lattice and perturbative control, and then got a 10× downward correction from expansion. **Higher-order perturbation theory** kept producing the same lesson: the new order mostly reveals the true error budget. Two sharp nulls changed conversations. A public-data atmospheric combination gave normal ordering at 3.3σ, and IceCube excluded Planck-suppressed decoherence. **ML and agent tooling** moved from demos to defaults.

## Running themes

- **LZ 248 keV recoil: heating up.** The arc runs from fits that skip solar capture, to the Sun as a composition probe, to models built around the solar bound, to the Sun as a test.
  - Lian et al. [arXiv:2610.09753](https://arxiv.org/abs/2610.09753) show that Higgsino-pair inelastic fits overproduce solar neutrinos, while singlino ground states survive.
  - Lee et al. [arXiv:2610.13930](https://arxiv.org/abs/2610.13930) drop the Higgsino for an $R$-symmetric Dirac bino.
  - Di Mauro [arXiv:2610.14188](https://arxiv.org/abs/2610.14188) proposes an IceCube solar-capture analysis, with dijet and relic tests also specified.
  - Holdouts whose abstracts still omit the solar bound: [arXiv:2610.12443](https://arxiv.org/abs/2610.12443), [arXiv:2610.15557](https://arxiv.org/abs/2610.15557), [arXiv:2610.18234](https://arxiv.org/abs/2610.18234).
- **First-order transitions and GWs: steady and maturing.**
  - Lattice work on 10-08 showed that Chern–Simons production survives supercooling [arXiv:2610.09257](https://arxiv.org/abs/2610.09257) and added the first metric perturbations [arXiv:2610.09325](https://arxiv.org/abs/2610.09325).
  - On 10-09, Gould et al.'s 3D EFT for strong transitions [arXiv:2610.10692](https://arxiv.org/abs/2610.10692) checked scale cancellation through NNLO, and many-bubble spectra were assembled from two-bubble libraries [arXiv:2610.12389](https://arxiv.org/abs/2610.12389).
  - On 10-14, Zou et al. [arXiv:2610.14806](https://arxiv.org/abs/2610.14806) found GW amplitudes in an expanding Universe about 10× below Minkowski simulations.
- **Perturbation theory at its edges: steady.**
  - Renormalon cancellation by trans-series terms [arXiv:2610.10059](https://arxiv.org/abs/2610.10059).
  - A Padé estimate of the $\alpha_s^7$ coefficient of $H\to gg$ [arXiv:2610.09874](https://arxiv.org/abs/2610.09874).
  - N³LO cold QED [arXiv:2610.13873](https://arxiv.org/abs/2610.13873).
  - Two-loop EFT of LSS [arXiv:2610.13867](https://arxiv.org/abs/2610.13867), where 49 coefficients absorb the gain and $\sigma_8$ barely improves.
  - Pattern across these: scale bands understate the uncertainty.
- **Exotics versus thresholds: heating up toward "no exotic needed."**
  - Dong et al. [arXiv:2610.11937](https://arxiv.org/abs/2610.11937) find no required X(2370) in the BESIII refit.
  - Swanson [arXiv:2610.15248](https://arxiv.org/abs/2610.15248) fits di-$J/\psi$ with rescattering alone (χ²/ndf = 56/50).
  - BESIII [arXiv:2610.13097](https://arxiv.org/abs/2610.13097) sees a 17 MeV $\pi^0\pi^0$ threshold structure that ChPT fails at threshold to reproduce.
  - BESIII also had a run of firsts: the $J/\psi\to e^+e^-\eta_c$ Dalitz decay [arXiv:2610.09626](https://arxiv.org/abs/2610.09626) and U-spin breaking in $D^0\to K\pi\pi$ [arXiv:2610.13101](https://arxiv.org/abs/2610.13101).
- **ML and AI tooling: heating up, moving into production.**
  - pyAmpliCol [arXiv:2610.10729](https://arxiv.org/abs/2610.10729) packages FFT colour sums into a public generator.
  - The "with AI under human supervision" EEC elliptic sector [arXiv:2610.10734](https://arxiv.org/abs/2610.10734).
  - The heptokens tokenizer [arXiv:2610.13876](https://arxiv.org/abs/2610.13876).
  - MadNIS becomes MadGraph's LO default [arXiv:2610.17177](https://arxiv.org/abs/2610.17177).
  - Agent benchmarks: HEPTABench [arXiv:2610.18454](https://arxiv.org/abs/2610.18454) (Haiku 4.5 goes from 8% to 79% with domain tools) and SIDERIUS [arXiv:2610.14024](https://arxiv.org/abs/2610.14024).
  - The position paper [arXiv:2610.14059](https://arxiv.org/abs/2610.14059) raises trust and verification questions.
- **Flavor anomalies: steady and unresolved.**
  - The $R(D^{(*)})$ world-average tension persists despite September's Belle II easing [arXiv:2610.16617](https://arxiv.org/abs/2610.16617).
  - Theory gives $R(D^*)=0.267(5)$, 2.8σ from experiment [arXiv:2610.17289](https://arxiv.org/abs/2610.17289).
  - LHCb proceedings say the $K^{*0}\mu\mu$ tensions persist [arXiv:2610.13165](https://arxiv.org/abs/2610.13165), and LHCb adds new high-$m_{K\pi}$ input [arXiv:2610.14156](https://arxiv.org/abs/2610.14156).

## Turning points

- **Neutrino mass ordering.** Jin et al. [arXiv:2610.12208](https://arxiv.org/abs/2610.12208) combine public Super-K, DeepCore and ORCA data and exclude inverted ordering at 3.3σ without reactor input. This is independent of JUNO's 2.1σ, though it is not a collaboration result. Model-builders already take normal ordering as given [arXiv:2610.11789](https://arxiv.org/abs/2610.11789).
- **IceCube decoherence.** The null [arXiv:2610.14144](https://arxiv.org/abs/2610.14144) excludes natural Planck-suppressed decoherence for $E^n$ scaling with $0\le n\le3$, including the first exclusion at $n=3$.
- **Light Binos.** LZ-2024 removes sub-100 GeV resonant Binos at >4σ under conservative assumptions [arXiv:2610.10219](https://arxiv.org/abs/2610.10219).
- **Lattice chiral gauge theory.** Craig [arXiv:2610.09093](https://arxiv.org/abs/2610.09093) gives a candidate nonperturbative lattice definition of the SM. It holds on admissible fields and is not a simulation recipe. A Hamiltonian disk-boundary route followed the next day [arXiv:2610.11035](https://arxiv.org/abs/2610.11035).
- **Cold QED at N³LO.** [arXiv:2610.13873](https://arxiv.org/abs/2610.13873) closes the order left open since 1977 and is a template for cold quark matter.
- **Neural importance sampling as default.** MadNIS [arXiv:2610.17177](https://arxiv.org/abs/2610.17177) is now what most users will run without noticing.

## Open questions

- **LZ 248 keV.** Which candidates survive once solar capture is applied everywhere? Watch for an IceCube or Super-K solar analysis and for holdout papers addressing the bound.
- **Di-$J/\psi$ and exotics.** Do tetraquark papers now test themselves against Swanson's rescattering null? What is the 274 MeV $\pi^0\pi^0$ threshold structure? Is the glueball-vs-$\phi h_1$ question still alive after the X(2370) refit?
- **Order of the chiral transition (Pisarski).** Do 2+1 $T_\chi$ extrapolations shift after the new finite-size correction [arXiv:2610.10350](https://arxiv.org/abs/2610.10350)?
- **GW normalization.** Does the 10× expansion suppression propagate into phenomenology built on Minkowski lattices?
- **Atmospheric ordering combination.** Will the correlated-systematics treatment hold up under scrutiny, or get a collaboration-level follow-up?
- **$R(D^{(*)})$ and $C_9$.** Both remain open. Watch Belle II updates and fits that use the new LHCb input.
- **Uncertainty beyond scale variation.** Do Bayesian missing-order estimates get adopted more widely?

## Recurring references

- [arXiv:2610.09753](https://arxiv.org/abs/2610.09753), [arXiv:2610.13930](https://arxiv.org/abs/2610.13930), [arXiv:2610.14188](https://arxiv.org/abs/2610.14188): the solar-bound arc for LZ.
- [arXiv:2610.10219](https://arxiv.org/abs/2610.10219): the LZ-2024 Bino exclusion.
- [arXiv:2610.12208](https://arxiv.org/abs/2610.12208): the 3.3σ ordering anchor.
- [arXiv:2610.09093](https://arxiv.org/abs/2610.09093): lattice SM measure.
- [arXiv:2610.10692](https://arxiv.org/abs/2610.10692), [arXiv:2610.14806](https://arxiv.org/abs/2610.14806): transition control and the expansion correction.
- [arXiv:2610.13873](https://arxiv.org/abs/2610.13873): N³LO cold QED and its uncertainty lesson.
- [arXiv:2610.15248](https://arxiv.org/abs/2610.15248), [arXiv:2610.11937](https://arxiv.org/abs/2610.11937), [arXiv:2610.13097](https://arxiv.org/abs/2610.13097): threshold-vs-exotic baselines.
- [arXiv:2610.16617](https://arxiv.org/abs/2610.16617): flavor tension status.
- [arXiv:2610.17177](https://arxiv.org/abs/2610.17177), [arXiv:2610.18454](https://arxiv.org/abs/2610.18454): tooling going to production.
