# The Cross Section: rolling synthesis, week ending 2026-10-15

Four digests (10-09, 10-12, 10-14, 10-15) carried five clear trajectories:

- **Normal neutrino ordering** firmed up through an independent atmospheric route.
- **The LZ 248 keV excess** produced a burst of model-building in which the solar-capture bound moved from ignored to designed-around.
- **Flavor tensions** ($R(D^{(*)})$, $C_9$, SU(3)$_F$) were restated rather than resolved, with a new >5σ SU(3)$_F$ failure.
- **Exotic-hadron claims** faced threshold and rescattering null hypotheses.
- **ML and agent tools** moved from demos into defaults.

A quieter thread ran through higher-order calculations, which mainly revealed true error budgets.

## Running themes

**Neutrino ordering and oscillation tests (heating).** Jin et al. [arXiv:2610.12208](https://arxiv.org/abs/2610.12208) combine public Super-K, DeepCore and ORCA data. They exclude inverted ordering at 3.3σ with no reactor input, against JUNO's ~2.1σ from about two weeks earlier. Model-builders already take normal ordering as input ([arXiv:2610.11789](https://arxiv.org/abs/2610.11789)). Dark-matter detectors are being repurposed for neutrino physics. Xenon solar-neutrino data already constrain the complex-NSI explanation of NOvA–T2K ([arXiv:2610.18971](https://arxiv.org/abs/2610.18971)).

**LZ 248 keV model-building (peaked, now steady).** The count ran one paper on 10-09, one on 10-12, five on 10-14 and one on 10-15. The qualitative shift came on 10-12:
- Lee et al. [arXiv:2610.13930](https://arxiv.org/abs/2610.13930) build around the solar-neutrino bound by dropping the Higgsino for a Dirac bino.
- Di Mauro [arXiv:2610.14188](https://arxiv.org/abs/2610.14188) gives the most complete single-model treatment, proposing a dedicated IceCube solar-capture analysis.
- Holdouts that do not mention solar capture persist: [arXiv:2610.12443](https://arxiv.org/abs/2610.12443), [arXiv:2610.15557](https://arxiv.org/abs/2610.15557) and [arXiv:2610.18234](https://arxiv.org/abs/2610.18234).

**Flavor tensions (heating).**
- **$R(D^{(*)})$:** Belle/Belle II world averages stay in tension despite September's "easing" ([arXiv:2610.16617](https://arxiv.org/abs/2610.16617)). Parameter-free form factors give $R(D^*)$ 2.8σ from experiment ([arXiv:2610.17289](https://arxiv.org/abs/2610.17289)).
- **$C_9$:** the $K^{*0}\mu\mu$ tensions persist ([arXiv:2610.13165](https://arxiv.org/abs/2610.13165)), and new high-$m_{K\pi}$ input arrived ([arXiv:2610.14156](https://arxiv.org/abs/2610.14156)).
- **SU(3)$_F$:** $\bar B\to DP$ needs ~60% SU(3)$_F$ breaking at >5σ ([arXiv:2610.20611](https://arxiv.org/abs/2610.20611)). This echoes August's $B\to PP$ puzzle.
- **Charm inputs:** BESIII U-spin breaking in $D^0\to K\pi\pi$ ([arXiv:2610.13101](https://arxiv.org/abs/2610.13101)) feeds the strong-phase inputs to $\gamma$.

**Thresholds versus exotics (heating).**
- Dong et al. find no required X(2370) in BESIII data ([arXiv:2610.11937](https://arxiv.org/abs/2610.11937)).
- Swanson fits di-$J/\psi$ with no exotic hadrons ([arXiv:2610.15248](https://arxiv.org/abs/2610.15248)), against the prior week's bound $cc\bar c\bar c$ claim.
- BESIII confirms a 17 MeV $\pi^0\pi^0$ threshold structure that ChPT fails to reproduce at threshold ([arXiv:2610.13097](https://arxiv.org/abs/2610.13097)).

**Tools into production (heating).**
- **Defaults:** MadNIS is now MadGraph's LO default ([arXiv:2610.17177](https://arxiv.org/abs/2610.17177)).
- **Public generators:** pyAmpliCol makes the FFT colour sums public ([arXiv:2610.10729](https://arxiv.org/abs/2610.10729)).
- **Agent benchmarks:** HEPTABench ([arXiv:2610.18454](https://arxiv.org/abs/2610.18454)) and SIDERIUS ([arXiv:2610.14024](https://arxiv.org/abs/2610.14024)) shift evaluation toward controlled, validity-based testing.
- **AI in calculations:** "AI under human supervision" reached a real calculation, the $\mathcal N=4$ EEC elliptic sector ([arXiv:2610.10734](https://arxiv.org/abs/2610.10734)). A position paper on formalization and trust followed ([arXiv:2610.14059](https://arxiv.org/abs/2610.14059)).

**Higher orders and strong transitions (steady).**
- Cold-QED N³LO ([arXiv:2610.13873](https://arxiv.org/abs/2610.13873)) and two-loop EFT of LSS ([arXiv:2610.13867](https://arxiv.org/abs/2610.13867)) both show that the next order mostly recalibrates errors.
- Strong-transition control improved: 3D EFT ([arXiv:2610.10692](https://arxiv.org/abs/2610.10692)), many-bubble GW spectra ([arXiv:2610.12389](https://arxiv.org/abs/2610.12389)), and thermal dimension-six operators found negligible ([arXiv:2610.12284](https://arxiv.org/abs/2610.12284)).
- Expanding-universe simulations cut GW amplitudes ~10× relative to Minkowski ([arXiv:2610.14806](https://arxiv.org/abs/2610.14806)).

## Turning points

- **Ordering:** 3.3σ normal ordering without reactors ([arXiv:2610.12208](https://arxiv.org/abs/2610.12208)). This is a public-data combination, not a collaboration result.
- **Decoherence:** IceCube excludes Planck-suppressed decoherence for $0\le n\le3$, including the first $n=3$ exclusion ([arXiv:2610.14144](https://arxiv.org/abs/2610.14144)).
- **Di-$J/\psi$ baseline:** Swanson's no-exotics fit, with three free background parameters, is now the bar tetraquark papers must beat ([arXiv:2610.15248](https://arxiv.org/abs/2610.15248)).
- **Neural sampling:** neural importance sampling became the MadGraph LO default ([arXiv:2610.17177](https://arxiv.org/abs/2610.17177)).
- **Error estimates:** the Bayesian missing-order estimate in [arXiv:2610.13873](https://arxiv.org/abs/2610.13873) can exceed scale variation. This repeats the prior week's jet-veto N³LL warning.

## Open questions

- **Ordering robustness:** does the 3.3σ survive scrutiny of its correlated-systematics treatment? Watch for collaboration-level follow-ups and JUNO updates.
- **NOvA–T2K:** is complex NSI viable, and do the xenon solar-neutrino constraints ([arXiv:2610.18971](https://arxiv.org/abs/2610.18971)) close more of it?
- **LZ 248 keV:** what is its origin? Watch for an actual IceCube solar-capture analysis and whether solar-agnostic papers die out.
- **SU(3)$_F$:** is the failure in the amplitude parametrization or in the symmetry expansion itself ([arXiv:2610.20611](https://arxiv.org/abs/2610.20611))?
- **$|V_{cb}|$:** a DIS route offers orthogonal systematics ([arXiv:2610.18961](https://arxiv.org/abs/2610.18961)). The Frascati workshop review is a useful status reference ([arXiv:2610.19917](https://arxiv.org/abs/2610.19917)).
- **Hadron spectroscopy:**
  - Expect theory papers on the BESIII $\pi^0\pi^0$ structure.
  - The X(2370) glueball-vs-$\phi h_1$ question remains open.
  - Search for the compact $X_b$ partner ~60 MeV below $B\bar B^*$ predicted in [arXiv:2610.19066](https://arxiv.org/abs/2610.19066).
- **Phase-transition GWs:** how much of the phenomenology survives the ~10× amplitude reduction?
- **Hadronic inputs:** a $\sigma_{\pi N}$ number from [arXiv:2610.20362](https://arxiv.org/abs/2610.20362) would settle the FLAG-vs-Roy–Steiner hedge. Small-$x$ pion PDFs are contested: Yang et al. strongly disfavor a vanishing pion gluon in response to Fantômas ([arXiv:2610.19415](https://arxiv.org/abs/2610.19415)).

## Recurring references

- **Neutrinos:** [arXiv:2610.12208](https://arxiv.org/abs/2610.12208), [arXiv:2610.14144](https://arxiv.org/abs/2610.14144), [arXiv:2610.18971](https://arxiv.org/abs/2610.18971)
- **LZ:** [arXiv:2610.13930](https://arxiv.org/abs/2610.13930), [arXiv:2610.14188](https://arxiv.org/abs/2610.14188)
- **Flavor:** [arXiv:2610.20611](https://arxiv.org/abs/2610.20611), [arXiv:2610.16617](https://arxiv.org/abs/2610.16617), [arXiv:2610.17289](https://arxiv.org/abs/2610.17289), [arXiv:2610.14156](https://arxiv.org/abs/2610.14156), [arXiv:2610.18961](https://arxiv.org/abs/2610.18961)
- **Hadrons:** [arXiv:2610.15248](https://arxiv.org/abs/2610.15248), [arXiv:2610.11937](https://arxiv.org/abs/2610.11937), [arXiv:2610.13097](https://arxiv.org/abs/2610.13097)
- **Tools:** [arXiv:2610.17177](https://arxiv.org/abs/2610.17177), [arXiv:2610.18454](https://arxiv.org/abs/2610.18454), [arXiv:2610.10734](https://arxiv.org/abs/2610.10734)
- **Higher orders and transitions:** [arXiv:2610.13873](https://arxiv.org/abs/2610.13873), [arXiv:2610.10692](https://arxiv.org/abs/2610.10692), [arXiv:2610.14806](https://arxiv.org/abs/2610.14806)
