# The Cross Section: rolling synthesis, week ending 2026-10-23

This week the field audited its inputs more than it chased new anomalies. The LZ 248 keV conversation turned from "which model survives?" to "how significant is the event?" Two key inputs, the electron-recoil (ER) tail and the dark-matter halo tail, both came under direct challenge. A broader error-budget thread ran from scale variations to ML PDF fits and microlensing limits. SU(3)$_F$ breaking became a recurring pressure point across B decays and charm baryons. The cleanest positive results were confirmations of theory: the hot Yang-Mills $g^6$ pressure matched the lattice, and the CVC weak-magnetism prediction was observed in the free neutron. Inference tooling, especially compressed taggers and simulation-based inference (SBI), advanced steadily.

## Running themes

- **LZ 248 keV: from model-building to auditing the significance (heating on inputs, fading on models).**
  - Bandyopadhyay et al. [arXiv:2610.27105](https://arxiv.org/abs/2610.27105) showed that the published calibration leaves the ER tail loosely constrained. A plausible tail makes the ER contribution comparable to the whole quoted background.
  - X. Zhang et al. [arXiv:2610.28731](https://arxiv.org/abs/2610.28731) found no local dark matter above ~900 km/s.
  - Model-building thinned out. Kim et al. [arXiv:2610.25423](https://arxiv.org/abs/2610.25423) built a shared LZ/Galactic Center excess (GCE) origin. Tan et al. [arXiv:2610.25925](https://arxiv.org/abs/2610.25925) proposed a hexaquark reading. Ibe et al. [arXiv:2610.29335](https://arxiv.org/abs/2610.29335) went to a heavy pseudo-Dirac doublet.
  - Two days (10-19, 10-23) had no LZ papers at all.

- **Error budgets and modeling assumptions (heating).**
  - Canonero et al. [arXiv:2610.25091](https://arxiv.org/abs/2610.25091) proposed going beyond 7-point scale variation.
  - de Vries et al. [arXiv:2610.28742](https://arxiv.org/abs/2610.28742) showed radiative corrections bias $\xi_{31}$ and raise the $0\nu\beta\beta$ rate by ~5%.
  - Elmer et al. [arXiv:2610.30239](https://arxiv.org/abs/2610.30239) found that three ML methods give the same triplet-PDF central values but different uncertainties.
  - Morales-Zapien et al. [arXiv:2610.30510](https://arxiv.org/abs/2610.30510) weakened the OGLE primordial black hole (PBH) bound by up to ~6× through halo and lens modeling alone.
  - Lind [arXiv:2610.31103](https://arxiv.org/abs/2610.31103) put the Monte Carlo top mass 240–330 MeV below the pole mass.

- **SU(3)$_F$ breaking under strain (heating).**
  - The normalisation error of LHCb's $\Xi_b^-\to\Xi^-\mu^+\mu^-$ [arXiv:2610.22452](https://arxiv.org/abs/2610.22452) is dominated by SU(3) breaking.
  - Theory responded with first-order U-spin sum rules ([arXiv:2610.24975](https://arxiv.org/abs/2610.24975)) and flavor-selective production to separate the $D_0^*(2300)$ poles ([arXiv:2610.26175](https://arxiv.org/abs/2610.26175)).
  - Belle/Belle II's $\Lambda_c^+\to\Lambda K^+\eta$ [arXiv:2610.31377](https://arxiv.org/abs/2610.31377) came in well above SU(3) expectations. It is the third strained system this season, after $B\to PP$ and $B\to DP$.

- **Neutrino anomalies weakening (steady).**
  - Barčot et al. [arXiv:2610.23474](https://arxiv.org/abs/2610.23474) review several neutrino tensions, now weakened but without an uncontested explanation.
  - Barenboim et al. [arXiv:2610.28744](https://arxiv.org/abs/2610.28744) refuted observable RG running of mixing.
  - IceCube shifted to precision with a $\nu_\mu$ CC cross section from 150 GeV to 40 TeV ([arXiv:2610.24068](https://arxiv.org/abs/2610.24068)). Its 1.9σ Lorentz-invariance-violation preference ([arXiv:2610.25214](https://arxiv.org/abs/2610.25214)) remains weak.

- **ML tooling moving into inference (steady, heating).**
  - Tagger compression continued. SParTA [arXiv:2610.27106](https://arxiv.org/abs/2610.27106) matched ParT with one-seventh the parameters. Agarwal et al. [arXiv:2610.29439](https://arxiv.org/abs/2610.29439) distilled ParT-level performance into a 2k-parameter student.
  - Sequential SBI for masses and widths arrived with Bahl et al. [arXiv:2610.30245](https://arxiv.org/abs/2610.30245).
  - Foundation models reached neutrino telescopes with CURTAIN [arXiv:2610.30894](https://arxiv.org/abs/2610.30894).

## Turning points

- **The $g^6$ hot Yang-Mills pressure was completed twice and agrees with the lattice.** Kajantie et al. [arXiv:2610.23675](https://arxiv.org/abs/2610.23675) and Chala et al. [arXiv:2610.23676](https://arxiv.org/abs/2610.23676) closed a gap open for over two decades. This directly validates the dimensional-reduction EFT, unlike recent "next order" results that mainly exposed true error budgets.
- **The halo tail undercut the Higgsino rescue.** Graham et al. (10-16) needed velocities up to 1100 km/s to evade the solar-capture bound. [arXiv:2610.28731](https://arxiv.org/abs/2610.28731) finds no tail there.
- **Dwarf spheroidals narrowed the GCE.** Kim et al. [arXiv:2610.26648](https://arxiv.org/abs/2610.26648) leave only τ-rich channels and light-mediator $4b$ cascades. Abazajian et al. [arXiv:2610.23713](https://arxiv.org/abs/2610.23713) show the 20 GeV halo excess is foreground-dependent.
- **The $|V_{cb}|$ escape for $C_9$ is closed.** Crivellin et al. [arXiv:2610.22490](https://arxiv.org/abs/2610.22490) give a no-go: CKM unitarity violation cannot produce the deficit without fine-tuning.
- **Weak magnetism was observed in the neutron.** Camarasa-Domene et al. [arXiv:2610.26792](https://arxiv.org/abs/2610.26792) find $g_M=4.47(87)$ and exclude zero at 5.1σ. The result is robust to tensions in the neutron lifetime dataset.

## Open questions

- **Will LZ release the calibrations** that [arXiv:2610.27105](https://arxiv.org/abs/2610.27105) says are needed to pin down the ER tail? Every 248 keV model inherits this uncertainty.
- **Is the NA61/SHINE charged-over-neutral kaon excess real?** [arXiv:2610.23498](https://arxiv.org/abs/2610.23498) reports an excess in Ar+Sc that known mechanisms do not explain. It is consistent from 2.6 to 200 GeV, uncertainties are sizeable, and it needs confirmation from other experiments.
- **Lattice vs. data-driven HVP.** The gap remains open. Li et al. [arXiv:2610.26130](https://arxiv.org/abs/2610.26130) use the correlation between $a_e$ and $a_\mu$ hadronic contributions. Bashir et al. [arXiv:2610.28506](https://arxiv.org/abs/2610.28506) supply the isospin-breaking correction for the τ route.
- **Will a symmetry-breaking framework absorb the SU(3)$_F$ excess,** or will the $\Lambda_c$ rate stay anomalous?
- **Neutrino mass ordering.** Gluza et al. [arXiv:2610.27270](https://arxiv.org/abs/2610.27270) find inverted ordering fits most mixing schemes better. That sits awkwardly with the replacement of Jin et al.'s 3.3σ normal-ordering result.
- **Expect replies** to [arXiv:2610.28744](https://arxiv.org/abs/2610.28744).
- **Birefringence sources keep multiplying.** New proposals include a stiff pseudoscalar ([arXiv:2610.27082](https://arxiv.org/abs/2610.27082)) and axion–monopole dynamics ([arXiv:2610.27059](https://arxiv.org/abs/2610.27059)). Astrophysical axion searches could close the stiff-pseudoscalar window.

## Recurring references

- LZ inputs: [arXiv:2610.27105](https://arxiv.org/abs/2610.27105), [arXiv:2610.28731](https://arxiv.org/abs/2610.28731)
- GCE: [arXiv:2610.23713](https://arxiv.org/abs/2610.23713), [arXiv:2610.26648](https://arxiv.org/abs/2610.26648), [arXiv:2610.25423](https://arxiv.org/abs/2610.25423)
- Error budgets: [arXiv:2610.25091](https://arxiv.org/abs/2610.25091), [arXiv:2610.30239](https://arxiv.org/abs/2610.30239), [arXiv:2610.30510](https://arxiv.org/abs/2610.30510)
- Hot QCD: [arXiv:2610.23675](https://arxiv.org/abs/2610.23675), [arXiv:2610.23676](https://arxiv.org/abs/2610.23676)
- SU(3)$_F$: [arXiv:2610.31377](https://arxiv.org/abs/2610.31377), [arXiv:2610.22452](https://arxiv.org/abs/2610.22452)
- Flavor no-go: [arXiv:2610.22490](https://arxiv.org/abs/2610.22490)
- Taggers: [arXiv:2610.27106](https://arxiv.org/abs/2610.27106), [arXiv:2610.29439](https://arxiv.org/abs/2610.29439)
