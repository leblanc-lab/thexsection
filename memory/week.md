# The Cross Section: weekly synthesis, week ending 2026-10-28

The week's dominant thread was the honesty of error bars. It started with physics inputs, such as halo models, radiative corrections and MC-mass definitions, and by 10-28 had reached the statistical machinery itself. The LZ 248 keV event kept losing explanations and drew no new papers on 10-23 or 10-28. Small-system QGP physics shifted from existence proofs to discriminating measurements, led by ALICE's O–O φ flow. Two neutrino results set up follow-ups: a refutation of observable RG running of mixing, and Super-K's 2.6σ relic-supernova hint. ML taggers moved from compression to diagnosis.

## Running themes

**Assumptions inside the error bar (heating up).** Examples accumulated through the week:
- Radiative corrections shift $0\nu\beta\beta$ rates by ~5% ([arXiv:2610.28742](https://arxiv.org/abs/2610.28742)). Three-body currents entered shell-model matrix elements ([arXiv:2610.32947](https://arxiv.org/abs/2610.32947)).
- Three ML methods give the same triplet-PDF central values but different uncertainties ([arXiv:2610.30239](https://arxiv.org/abs/2610.30239)).
- Updated halo and lens models alone weaken OGLE PBH bounds ~6× ([arXiv:2610.30510](https://arxiv.org/abs/2610.30510)).
- The Pythia MC top mass sits 240–330 MeV below the pole mass ([arXiv:2610.31103](https://arxiv.org/abs/2610.31103)).
- On 10-28 the thread reached fitters: BFGS runs ~10× faster than Migrad ([arXiv:2610.35927](https://arxiv.org/abs/2610.35927)), NTK modes separate signal from noise ([arXiv:2610.36034](https://arxiv.org/abs/2610.36034)), and the Hessian method misses nPDF minima ([arXiv:2610.37254](https://arxiv.org/abs/2610.37254)).

**LZ 248 keV event (cooling).**
- The Gaia-anchored halo tail cuts off near ~900 km/s ([arXiv:2610.28731](https://arxiv.org/abs/2610.28731)). That undercuts Graham et al.'s (10-16) thermal-Higgsino rescue, which needed a tail to 1100 km/s.
- Sterile-fermion up-scattering needs near-nonperturbative couplings ([arXiv:2610.32747](https://arxiv.org/abs/2610.32747)).
- The remaining routes are costly: heavy pseudo-Dirac doublets need fine-tuned CP violation ([arXiv:2610.29335](https://arxiv.org/abs/2610.29335)).
- Work is drifting toward generic inelastic-DM phenomenology, such as the inelastic neutrino fog ([arXiv:2610.35789](https://arxiv.org/abs/2610.35789)).

**Small-system QGP (heating up).**
- ALICE's first O–O $I_{AA}$ shows weaker away-side suppression than central Pb–Pb ([arXiv:2610.35331](https://arxiv.org/abs/2610.35331)).
- Then came φ $v_2$ ([arXiv:2610.36237](https://arxiv.org/abs/2610.36237)) and a nonflow subtraction validated on Angantyr ([arXiv:2610.36922](https://arxiv.org/abs/2610.36922)).
- The year's anchor remains CMS's O–O baryon-to-meson enhancement ([arXiv:2608.18256](https://arxiv.org/abs/2608.18256)).

**Top threshold and mass schemes (steady).**
- Buccioni et al.'s analytic two-loop $t\bar t$ amplitudes come with a public threshold evaluator ([arXiv:2610.32543](https://arxiv.org/abs/2610.32543)).
- Fontes et al. find linear IR terms cancel through NNLO with a short-distance mass ([arXiv:2610.36065](https://arxiv.org/abs/2610.36065)).
- Both feed the toponium-vs-continuum argument. Ball et al. (prior week) showed any threshold excess is entangled with $m_t$.

**ML: taggers and agents (steady, changing character).**
- Taggers: distillation reached a 2k-parameter student matching ParT ([arXiv:2610.29439](https://arxiv.org/abs/2610.29439)). By 10-28 the work was diagnostic: model stitching locates the Lund-plane deficit ([arXiv:2610.37137](https://arxiv.org/abs/2610.37137)).
- Agents: they produced analytic NLO results ([arXiv:2610.31745](https://arxiv.org/abs/2610.31745)), while QFT-Bench showed correct answers with unfaithful reasoning ([arXiv:2610.33134](https://arxiv.org/abs/2610.33134)).
- Inference layer: SBI extended to masses and widths ([arXiv:2610.30245](https://arxiv.org/abs/2610.30245)), and foundation-model pretraining transferred to neutrino telescopes ([arXiv:2610.30894](https://arxiv.org/abs/2610.30894)).

**Axions off and on the haloscope (steady).**
- Off the haloscope: $^{229}$Th clocks respond linearly to imperfect axions ([arXiv:2610.30238](https://arxiv.org/abs/2610.30238)), and bound supernova ALPs give limits from a cold neutron star ([arXiv:2610.30255](https://arxiv.org/abs/2610.30255)).
- Back in the cavity: pre-excited modes give a signal linear in $g_{a\gamma}$ ([arXiv:2610.31717](https://arxiv.org/abs/2610.31717)), with sensitivity claims resting on simulation.

## Turning points

- **Observable RG running of neutrino mixing refuted** ([arXiv:2610.28744](https://arxiv.org/abs/2610.28744)). Mixing is fixed on-shell, and short-baseline data cap production-to-detection angle shifts at 0.7°–2.4°. This kills a class of proposed signatures.
- **φ flows like a meson** ([arXiv:2610.36237](https://arxiv.org/abs/2610.36237)). Its $v_2$ tracks the $K^0_S$, not the near-mass Λ, which favors recombination over mass ordering.
- **Measured halo tail** ([arXiv:2610.28731](https://arxiv.org/abs/2610.28731)). This is now the default input for 248 keV papers.
- **Genus-two geometry in a physical finite remainder** ([arXiv:2610.32543](https://arxiv.org/abs/2610.32543)).
- **CONUS+ reaches 10.2σ** reactor CEνNS, with $N_s/N_{\rm SM}=0.91\pm0.14$ ([arXiv:2610.37318](https://arxiv.org/abs/2610.37318), [arXiv:2610.37345](https://arxiv.org/abs/2610.37345)).

## Open questions

- **DSNB hint.** Super-K reports 2.6σ ([arXiv:2610.35619](https://arxiv.org/abs/2610.35619)). It is unclear how much comes from background rejection versus the spectral fit. Watch for independent analyses.
- **GCE as fluctuation.** Time-dependent cosmic-ray transport can mimic the excess ([arXiv:2610.32845](https://arxiv.org/abs/2610.32845)), following foreground-dependence (10-19) and dSph-corridor (10-20) results. Watch whether Fermi-LAT templates adopt time dependence.
- **SIDM vs CDM in lensing perturbers.** SIDM subhalos match far more often, at ~0.6 vs ~0.002 for PJ011646 ([arXiv:2610.31881](https://arxiv.org/abs/2610.31881)).
- **SU(3)$_F$ strain, third system.** Belle/Belle II observe $\Lambda_c^+\to\Lambda K^+\eta$ well above SU(3)$_F$ expectations ([arXiv:2610.31377](https://arxiv.org/abs/2610.31377)), after $B\to PP$ and $B\to DP$.
- **Negative effective $\sum m_\nu$.** Dark-sector interactions don't rescue a positive value ([arXiv:2610.33729](https://arxiv.org/abs/2610.33729)). Late reheating may lower the cosmological mass density ([arXiv:2610.36062](https://arxiv.org/abs/2610.36062)).
- **Low-energy weak mixing angle.** CONUS+ gives $0.225\pm0.022$, versus the combined CEνNS+ν–e $0.233^{+0.007}_{-0.006}$ ([arXiv:2610.31254](https://arxiv.org/abs/2610.31254)).
- **Replies to the RG-running refutation** are expected.
- **$|V_{cb}|$.** Low-scale Pati–Salam predicts $|V_{cb}|=0.042\pm0.002$ ([arXiv:2610.33152](https://arxiv.org/abs/2610.33152)), against the month's inclusive/exclusive split.

## Recurring references

- [arXiv:2610.28731](https://arxiv.org/abs/2610.28731): halo tail; the LZ and microlensing reference point.
- [arXiv:2610.30239](https://arxiv.org/abs/2610.30239): ML-PDF uncertainty anatomy, cited again on 10-28.
- [arXiv:2610.28742](https://arxiv.org/abs/2610.28742): $\beta\beta$ radiative corrections, paired with [arXiv:2610.32947](https://arxiv.org/abs/2610.32947).
- [arXiv:2610.31745](https://arxiv.org/abs/2610.31745): FeynFacet, the agentic-theory anchor.
- [arXiv:2610.35331](https://arxiv.org/abs/2610.35331) and [arXiv:2608.18256](https://arxiv.org/abs/2608.18256): O–O small-system anchors.
- [arXiv:2610.31254](https://arxiv.org/abs/2610.31254): neutrino-only $\sin^2\theta_W$ baseline.
- [arXiv:2610.25423](https://arxiv.org/abs/2610.25423): Kim et al.'s dark-Higgs model for both the LZ event and the GCE, which reappeared on 10-27.
