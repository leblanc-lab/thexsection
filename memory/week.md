# The Cross Section — Weekly synthesis, week ending 2026-11-06

This week precision theory became a deciding factor rather than a refinement. Three-loop running excluded minimal SUSY SU(5), and FCC-ee was repeatedly framed as the decisive test. The HVP input chain drew attention from both sides in quick succession. BaBar re-measured ISR ππ and exposed an internal spread, and two generators then tightened the QED radiation that measurement depends on. Galaxy-scale lensing gave its strongest population-level push yet toward core-collapsing SIDM. Light-ion collectivity matured into a nuclear-structure probe. Several old anomalies (X17, DAMA) lost parameter space, though closure is complicated by new "what do the data actually constrain" papers. Clean exclusive flavor channels kept landing on the SM.

## Running themes

- **HVP inputs under scrutiny (heating).**
  - The τ-route isospin budget tightened again with the $\omega\pi$ correction [arXiv:2611.01683](https://arxiv.org/abs/2611.01683), following the 10-21 $\rho\pi\pi$ term.
  - BaBar's full-sample ISR ππ re-analysis [arXiv:2611.04596](https://arxiv.org/abs/2611.04596) uses angular π/μ separation and gives $a_\mu^{\pi\pi}=525.9\pm3.5\pm3.8$. The combination with 2009 is 517.8 ± 2.4 ± 3.3, an internal spread of ~8×10⁻¹⁰.
  - KKMC and SHERPA now agree to ≲0.04% on resummed QED for this process [arXiv:2611.07067](https://arxiv.org/abs/2611.07067), with a new rule for the O(1) radiative-return regime. Pions are still point-like plus a form factor.
- **Loop order and Tera-Z decide models (heating).**
  - The two- vs three-loop flip on minimal SUSY SU(5) [arXiv:2610.40821](https://arxiv.org/abs/2610.40821) anchored the thread.
  - Groundwork followed: the full one-loop SM in BMHV [arXiv:2611.00141](https://arxiv.org/abs/2611.00141).
  - A counter-bet appeared: a TeV-scale long-lived colour triplet from split Yukawas [arXiv:2611.03783](https://arxiv.org/abs/2611.03783).
  - FCC-ee was posed as the falsifier for flavour-chain messengers up to 100 TeV [arXiv:2611.05464](https://arxiv.org/abs/2611.05464).
  - On the QCD side, Adelaja et al. [arXiv:2610.40823](https://arxiv.org/abs/2610.40823) offer a tuning-free account of small-$x$ $\zeta_2$ violations, with five-loop predictions.
- **SIDM vs CDM in strong lensing (heating).** Gilman et al. [arXiv:2610.40766](https://arxiv.org/abs/2610.40766) analyze 29 quads and find halo densities consistent with gravothermal collapse. They favor 20–80 GeV DM with MeV mediators, pushed toward a neutrinophilic scalar. It is the third result in two weeks against CDM-density subhalos, and the first at population level. The authors still say "hints."
- **Light ions as nuclear-force data (heating).**
  - Ne–Ne geometry tagging appeared [arXiv:2610.40724](https://arxiv.org/abs/2610.40724).
  - The O–O $\Lambda/K^0_S$ shape is ordered by transverse density, not multiplicity, and needs sub-nucleonic structure [arXiv:2611.04865](https://arxiv.org/abs/2611.04865).
  - Ne/O $v_2$ ratios are model-robust, while $v_3$ ratios are not [arXiv:2611.05239](https://arxiv.org/abs/2611.05239).
  - Eccentricities respond linearly to all 16 N²LO LECs, and Ne–Ne mostly probes spin-orbit [arXiv:2611.08122](https://arxiv.org/abs/2611.08122).
  - At the low-multiplicity floor, ALICE [arXiv:2611.08327](https://arxiv.org/abs/2611.08327) finds partonic-flow signatures down to $N_{\rm ch}\geq25$, with uncertainty-limited bins below.
- **Phase-transition GW forecasts lose idealizations (steady).**
  - Gravity couplings change completion [arXiv:2610.40775](https://arxiv.org/abs/2610.40775).
  - Dark–visible sound-wave leakage suppresses the signal [arXiv:2610.40781](https://arxiv.org/abs/2610.40781).
  - Nucleated bubbles are non-spherical at ~10% [arXiv:2610.41504](https://arxiv.org/abs/2610.41504).
  - In the type-II seesaw, the $v_c/T_c$ criterion flags transitions that never complete; those that do are sub-LISA [arXiv:2611.01634](https://arxiv.org/abs/2611.01634).
- **Compact, structured ML (steady, question shifting).**
  - CoReNet [arXiv:2610.40749](https://arxiv.org/abs/2610.40749) matches a transformer >100× its size in $HH\to4b$ with 1508 parameters.
  - SCRAMJet [arXiv:2611.00086](https://arxiv.org/abs/2611.00086) runs in 147 ns on FPGA.
  - The open issue is now what survives quantization: SCRAMJet's "virtual channels" are a QAT failure mode, not a size limit.

## Turning points

- **Minimal SUSY SU(5) appears excluded at three loops** under Tera-Z precision and proton-decay limits [arXiv:2610.40821](https://arxiv.org/abs/2610.40821).
- **BaBar disagrees with itself.** The new and 2009 ISR ππ analyses sit ~8×10⁻¹⁰ apart [arXiv:2611.04596](https://arxiv.org/abs/2611.04596).
- **LHCb Upgrade I's first rare-decay physics** [arXiv:2611.00230](https://arxiv.org/abs/2611.00230) gives first single-experiment evidence for $B^0\to\mu\mu$ and the most precise $B_s\to\mu\mu$ BF and lifetime, all SM-consistent.
- **X17 loses a band.** FASER excludes $6\times10^{-5}<\epsilon_e<1.2\times10^{-4}$ [arXiv:2611.03904](https://arxiv.org/abs/2611.03904). DAMA still cannot coexist with LZ, PICO-60 and CDMSlite even under extended NREFT [arXiv:2611.04890](https://arxiv.org/abs/2611.04890).
- **The neutrino-current route to CMB birefringence is closed** [arXiv:2611.07578](https://arxiv.org/abs/2611.07578). The required electron coupling is already excluded.
- **Method adopted:** Born spreading is now public in MadGraph5_aMC@NLO, including FxFx [arXiv:2611.06769](https://arxiv.org/abs/2611.06769).

## Open questions

- **BaBar's internal ππ spread.** How does the paper quantify compatibility between its two analyses? Does the new QED-generator work [arXiv:2611.07067](https://arxiv.org/abs/2611.07067) shift either one?
- **Toponium vs CP-odd Higgs (CMS excess).** NNLO toponium gives 4.87 pb, with the error now dominated by the Coulomb scale [arXiv:2611.03782](https://arxiv.org/abs/2611.03782). The 2HDM interference tool [arXiv:2611.08388](https://arxiv.org/abs/2611.08388) is only a status report.
- **X17 is not cleanly closable.** A high-coupling window remains, and spectroscopy plus $g-2$ leaves unbounded nucleon-coupling directions [arXiv:2611.06129](https://arxiv.org/abs/2611.06129). The same author found Ge/Xe blind directions [arXiv:2611.04600](https://arxiv.org/abs/2611.04600).
- **$|V_{cb}|$ inclusive/exclusive.** The hadronic-input-free top-decay route [arXiv:2611.01274](https://arxiv.org/abs/2611.01274) sits at ~19% and cannot yet settle the puzzle. The $C_9$ tension is also untouched.
- **The LZ 248 keV event.** Only one model so far, an exothermic Higgs-portal relic predicting a COSI photon continuum [arXiv:2611.01158](https://arxiv.org/abs/2611.01158).
- **CMB birefringence.** The hint stands at 4.8σ (3.5σ post-dust) and is now without a neutrino explanation.
- **A Super-K $\bar\nu_e$ excess.** It now has a pion-DM model with a JUNO test [arXiv:2611.08440](https://arxiv.org/abs/2611.08440). Whether this is the 10-27 DSNB indication is unconfirmed.

## Recurring references

- [arXiv:2610.40821](https://arxiv.org/abs/2610.40821): SU(5) loop-order flip, cited on four of five days.
- [arXiv:2611.04596](https://arxiv.org/abs/2611.04596): BaBar ISR ππ (also posted as [arXiv:2611.04621](https://arxiv.org/abs/2611.04621)).
- [arXiv:2610.40766](https://arxiv.org/abs/2610.40766): 29-lens core-collapse population.
- [arXiv:2611.03782](https://arxiv.org/abs/2611.03782): NNLO pseudoscalar toponium.
- [arXiv:2611.03904](https://arxiv.org/abs/2611.03904): FASER X17 recast.
- [arXiv:2611.04600](https://arxiv.org/abs/2611.04600) / [arXiv:2611.06129](https://arxiv.org/abs/2611.06129): Serao identifiability pair.
- [arXiv:2610.40749](https://arxiv.org/abs/2610.40749) / [arXiv:2611.00086](https://arxiv.org/abs/2611.00086): compact-ML anchors.
- [arXiv:2611.01683](https://arxiv.org/abs/2611.01683): τ-route isospin budget.
