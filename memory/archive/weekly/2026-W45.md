# The Cross Section: Rolling synthesis, week ending 2026-11-05

The week's clearest trajectory was **precision as the arbiter of BSM models**. Three-loop running appears to exclude minimal SUSY SU(5) at Tera-Z precision. FCC-ee papers then framed the $Z$ pole as the falsification venue for flavour and HNL models. Three other threads were active:

- **Dark-matter small-scale structure:** strong-lensing evidence kept tilting toward SIDM-like core collapse.
- **Hadronic vacuum polarization:** the HVP thread gained a new BaBar $\pi\pi$ measurement that disagrees internally.
- **Old anomalies:** X17, DAMA and the LZ 248 keV event were steadily boxed in, while new papers mapped which parameter directions the data can't constrain at all.

Data were sparse beyond LHCb's first Upgrade I rare-decay result and the BaBar re-analysis. Most of the week was theory, projections and methods.

## Running themes

- **Loop order and Tera-Z decide models (heating).** Allwicher et al. [arXiv:2610.40821](https://arxiv.org/abs/2610.40821) find that minimal SU(5) points to PeV-scale SUSY at two loops but appears excluded at three. The flip comes via an IR-fixed colour-triplet mass, which Dvali et al. [arXiv:2611.03783](https://arxiv.org/abs/2611.03783) bet against with a TeV-scale long-lived triplet. Kühler et al. [arXiv:2611.00141](https://arxiv.org/abs/2611.00141) supply full one-loop SM BMHV counterterms as multi-loop EW groundwork. By 11-05 the frame was explicitly FCC-ee:
  - Greljo et al. [arXiv:2611.05464](https://arxiv.org/abs/2611.05464): flavour-chain messengers, reach of 3 → 100 TeV in $M_F/|y_F|$.
  - Vignaroli [arXiv:2611.05501](https://arxiv.org/abs/2611.05501): HNL dipoles at the $Z$ pole.
- **Lensing favors SIDM core collapse (heating).** Gilman et al. [arXiv:2610.40766](https://arxiv.org/abs/2610.40766) use 29 quads, the first population-level result. It favors 20–80 GeV dark matter with MeV mediators, pointing to a neutrinophilic scalar. This is the third such result in two weeks, after Zhang et al. and Tekverk et al., though the authors still call it "hints."
- **HVP inputs (heating).** On the τ-route isospin budget, Esparza Arellano et al. [arXiv:2611.01683](https://arxiv.org/abs/2611.01683) tightened the $\omega\pi$ correction, following Bashir et al.'s $\rho\pi\pi$ term (10-21). Then BaBar [arXiv:2611.04596](https://arxiv.org/abs/2611.04596) re-measured $\pi\pi$ with angular pion/muon separation. The new result is 525.9 ± 3.5 ± 3.8, but combined with the 2009 analysis it gives 517.8, implying an internal spread of about 8×10⁻¹⁰.
- **Flavor split (steady).** LHCb [arXiv:2611.00230](https://arxiv.org/abs/2611.00230) finds $B_{(s)}\to\mu\mu$ SM-consistent with Upgrade I data. Live tensions remain in $C_9$ and $|V_{cb}|$. CMS [arXiv:2611.01274](https://arxiv.org/abs/2611.01274) gives a hadronic-input-free $|V_{cb}|$ from top decays, but at ~19% it is too coarse to settle the puzzle.
- **Old anomalies closing; identifiability as a habit (heating).**
  - FASER [arXiv:2611.03904](https://arxiv.org/abs/2611.03904) excludes a mid-coupling X17 band.
  - Serao et al. show unbounded X17 nucleon-coupling directions [arXiv:2611.06129](https://arxiv.org/abs/2611.06129) and Ge/Xe blind directions for light mediators [arXiv:2611.04600](https://arxiv.org/abs/2611.04600).
  - DAMA remains incompatible even with an extended NREFT treatment [arXiv:2611.04890](https://arxiv.org/abs/2611.04890).
- **Compact, structured ML for triggers (steady; question shifting).**
  - CoReNet [arXiv:2610.40749](https://arxiv.org/abs/2610.40749) matches a transformer more than 100× larger with 1508 parameters.
  - SCRAMJet [arXiv:2611.00086](https://arxiv.org/abs/2611.00086) and SpikePID [arXiv:2611.00104](https://arxiv.org/abs/2611.00104) bring the same push to FPGAs.
  - Following LEAF (10-21), the issue is now what survives quantization, not whether models can shrink.
- **GW forecasts lose idealizations (steady, likely to fade).** Three 11-02 papers each relaxed one assumption: gravity couplings, dark-visible sound-wave leakage, and non-spherical bubbles. Chiang [arXiv:2611.01634](https://arxiv.org/abs/2611.01634) adds that $v_c/T_c>1$ flags type-II seesaw transitions that never complete.

## Turning points

- **Minimal SUSY SU(5) flips from viable to excluded at three loops** ([arXiv:2610.40821](https://arxiv.org/abs/2610.40821)). Higher-loop running is now a first-class input to Tera-Z GUT tests.
- **The SIDM lensing case moves from per-perturber to population level** ([arXiv:2610.40766](https://arxiv.org/abs/2610.40766)), with a concrete particle model attached.
- **"Virtual channels"** ([arXiv:2611.00086](https://arxiv.org/abs/2611.00086)): quantization-aware training can silently drop signal-carrying channels. A datalane floor recovers 3.1 points, so HGQ-style workflows are affected.
- **Squark limits move about 1 TeV upward to 2.6–3.0 TeV** ([arXiv:2611.03794](https://arxiv.org/abs/2611.03794)), and HL-LHC/FCC-hh reach estimates inherit the shift.
- **Born spreading is now public in MadGraph5_aMC@NLO**, including FxFx ([arXiv:2611.06769](https://arxiv.org/abs/2611.06769)).

## Open questions

- **BaBar internal compatibility:** how does [arXiv:2611.04596](https://arxiv.org/abs/2611.04596) quantify the tension between its 2009 and new $\pi\pi$ analyses? Watch for reactions and lattice/τ comparisons.
- **The LZ 248 keV event:** the only model so far is Roy et al.'s exothermic Higgs-portal relic [arXiv:2611.01158](https://arxiv.org/abs/2611.01158), which predicts a sub-MeV continuum for COSI.
- **Toponium vs CP-odd Higgs** in the CMS excess: the NNLO 4.87 pb result [arXiv:2611.03782](https://arxiv.org/abs/2611.03782) leaves Coulomb-scale dependence as the dominant error.
- **X17's high-coupling window**, which remains open after FASER while the unbounded directions persist.
- **Upgrade I numbers:** how much does the $B^0/B_s$ ratio tighten in [arXiv:2611.00230](https://arxiv.org/abs/2611.00230)?
- **Ne–Ne predictions:** $\Lambda/K^0_S$ within 3–5% of O–O ([arXiv:2611.04865](https://arxiv.org/abs/2611.04865)), and the robustness of $v_2$ but not $v_3$ ratios ([arXiv:2611.05239](https://arxiv.org/abs/2611.05239)).
- **Low-$Q$ $\sin^2\theta_W$ spread:** COHERENT gives 0.231 ([arXiv:2611.03751](https://arxiv.org/abs/2611.03751)), against 0.225 from CONUS+ and 0.233 from the CEνNS+ν–e combination.
- **Neutrino mass tension:** Thermal Festina Lente [arXiv:2611.02559](https://arxiv.org/abs/2611.02559) requires a lightest neutrino above 10–43 meV, in tension with DESI DR2's negative-$\sum m_\nu$ preference.
- **Large claims to check:** Suliga et al.'s ≥7.2σ UHECR light-nucleus claim [arXiv:2611.00205](https://arxiv.org/abs/2611.00205) needs a model-dependence check.

## Recurring references

- [arXiv:2610.40821](https://arxiv.org/abs/2610.40821): SU(5) loop-order flip, cited on all four days.
- [arXiv:2610.40766](https://arxiv.org/abs/2610.40766): population-level SIDM lensing.
- [arXiv:2610.40749](https://arxiv.org/abs/2610.40749): CoReNet, the anchor for the compact-ML thread.
- [arXiv:2611.01683](https://arxiv.org/abs/2611.01683) and [arXiv:2611.04596](https://arxiv.org/abs/2611.04596) (also [arXiv:2611.04621](https://arxiv.org/abs/2611.04621)): HVP inputs.
- [arXiv:2611.03904](https://arxiv.org/abs/2611.03904), [arXiv:2611.04600](https://arxiv.org/abs/2611.04600) and [arXiv:2611.06129](https://arxiv.org/abs/2611.06129): X17 and identifiability.
- [arXiv:2611.00230](https://arxiv.org/abs/2611.00230) and [arXiv:2611.01274](https://arxiv.org/abs/2611.01274): flavor.
- [arXiv:2610.40775](https://arxiv.org/abs/2610.40775), [arXiv:2610.40781](https://arxiv.org/abs/2610.40781) and [arXiv:2610.41504](https://arxiv.org/abs/2610.41504): phase-transition realism.
