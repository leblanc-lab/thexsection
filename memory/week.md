# The Cross Section: Rolling synthesis, week ending 2026-10-27

The week moved from building models to auditing inputs. The 248 keV LZ event had driven seven weeks of model-building. This week its background estimate ([arXiv:2610.27105](https://arxiv.org/abs/2610.27105)) and its halo tail ([arXiv:2610.28731](https://arxiv.org/abs/2610.28731)) were questioned directly, and new explanations kept failing. The same instinct to check what goes into an error bar showed up in ML PDF fits, microlensing bounds, top-mass definitions and $0\nu\beta\beta$ nuclear inputs. Small-scale structure leaned further toward SIDM, while the Galactic Center excess got its most deflationary reading yet. Late in the week, Super-K reported the first hint of the diffuse supernova neutrino background (DSNB) at 2.6σ. Throughout, ML compression and AI agents for theory advanced steadily.

## Running themes

- **The LZ 248 keV event: models cooling, systematics heating.** The event had no new papers on two days this week. Explanations that did appear needed extreme corners:
  - a 10²–10⁴ TeV pseudo-Dirac doublet with fine-tuned CP violation ([arXiv:2610.29335](https://arxiv.org/abs/2610.29335));
  - sterile-fermion up-scattering at the edge of perturbativity, judged "not compelling" ([arXiv:2610.32747](https://arxiv.org/abs/2610.32747)).

  The inelastic kinematics are now being generalized beyond the event: neutrino-fog maps ([arXiv:2610.35789](https://arxiv.org/abs/2610.35789)), AGN-spike bounds ([arXiv:2610.35620](https://arxiv.org/abs/2610.35620)) and differentiable anisotropic velocity distributions ([arXiv:2610.28758](https://arxiv.org/abs/2610.28758)).
- **Assumptions inside the error bar (heating).** This is the week's connective thread:
  - LZ's electron-recoil (ER) tail ([arXiv:2610.27105](https://arxiv.org/abs/2610.27105));
  - ML triplet-PDF uncertainties, where calibration depends on covariance correlations, not pointwise width ([arXiv:2610.30239](https://arxiv.org/abs/2610.30239));
  - OGLE PBH bounds weakened up to ~6× by halo and lens models alone ([arXiv:2610.30510](https://arxiv.org/abs/2610.30510));
  - Pythia MC top mass 240–330 MeV below the pole mass ([arXiv:2610.31103](https://arxiv.org/abs/2610.31103));
  - double-β radiative corrections raising $0\nu\beta\beta$ rates by ~5% ([arXiv:2610.28742](https://arxiv.org/abs/2610.28742));
  - the first chiral three-body currents in shell-model $0\nu\beta\beta$ ([arXiv:2610.32947](https://arxiv.org/abs/2610.32947)).
- **Small-scale dark matter: CDM under pressure, GCE deflating (heating).**
  - No CDM subhalo out of more than 5000 is dense enough to match the observed perturbers ([arXiv:2610.27236](https://arxiv.org/abs/2610.27236)).
  - SIDM matches all three perturbers far more often, for example ~0.6 vs ~0.002 for PJ011646, and simultaneous fits need $w\gtrsim10^2$ km/s ([arXiv:2610.31881](https://arxiv.org/abs/2610.31881)). Unitarity links between elastic and annihilation SIDM cross sections ([arXiv:2610.27056](https://arxiv.org/abs/2610.27056), [arXiv:2610.27089](https://arxiv.org/abs/2610.27089)) are relevant here.
  - Time-dependent cosmic-ray transport alone reproduces GCE-sized residuals ([arXiv:2610.32845](https://arxiv.org/abs/2610.32845)). This follows earlier foreground-dependence (10-19) and dSph-corridor (10-20) results.
- **Neutrino ordering and mixing structure (steady, contested).**
  - Most mixing schemes fit inverted ordering (IO) better, and TM₂ is excluded at >3σ ([arXiv:2610.27270](https://arxiv.org/abs/2610.27270)). This came the same day Jin et al.'s 3.3σ normal-ordering result was replaced.
  - A fusion-algebra model yields IO with $m_3=0$ ([arXiv:2610.35587](https://arxiv.org/abs/2610.35587)).
  - Cosmology still prefers negative effective $\sum m_\nu$ even with dark-sector interactions ([arXiv:2610.33729](https://arxiv.org/abs/2610.33729)).
- **ML and agents (steady, maturing).**
  - Taggers keep shrinking: LEAF at 35 ns ([arXiv:2610.27078](https://arxiv.org/abs/2610.27078)), SParTA ([arXiv:2610.27106](https://arxiv.org/abs/2610.27106)), and a 2k-parameter distilled student matching ParT ([arXiv:2610.29439](https://arxiv.org/abs/2610.29439)).
  - Inference tooling now includes sequential SBI for masses and widths ([arXiv:2610.30245](https://arxiv.org/abs/2610.30245)) and foundation models for neutrino telescopes ([arXiv:2610.30894](https://arxiv.org/abs/2610.30894)).
  - The agent thread ran from the AI-theory blueprint ([arXiv:2610.28505](https://arxiv.org/abs/2610.28505)) to agent-derived NLO hard functions in FeynFacet ([arXiv:2610.31745](https://arxiv.org/abs/2610.31745)). QFT-Bench then found frontier models score above 95% while giving unfaithful reasoning ([arXiv:2610.33134](https://arxiv.org/abs/2610.33134)).
- **Axions spreading across channels (steady).**
  - Off-haloscope proposals: $^{229}$Th clocks sensitive to PQ quality ([arXiv:2610.30238](https://arxiv.org/abs/2610.30238)), and bound supernova ALPs heating PSR J2144−3933 ([arXiv:2610.30255](https://arxiv.org/abs/2610.30255)).
  - Inside the haloscope: a non-Poisson quantum treatment ([arXiv:2610.30250](https://arxiv.org/abs/2610.30250)), pre-excited cavities ([arXiv:2610.31717](https://arxiv.org/abs/2610.31717)) and a likelihood treatment giving 1.4× stronger upper limits ([arXiv:2610.34325](https://arxiv.org/abs/2610.34325)).
  - Birefringence gained non-axion-standard sources: a stiff pseudoscalar ([arXiv:2610.27082](https://arxiv.org/abs/2610.27082)) and axion–monopole dynamics ([arXiv:2610.27059](https://arxiv.org/abs/2610.27059)).

## Turning points

- **[arXiv:2610.27105](https://arxiv.org/abs/2610.27105)** is the first paper to question the LZ event's significance itself. Plausible ER tails, matching the executable model to 0.47% in the $N_e$ quantiles, can be as large as the whole quoted background.
- **[arXiv:2610.28731](https://arxiv.org/abs/2610.28731)** finds no local dark matter above ~900 km/s from a Gaia-plus-LMC halo reconstruction. That undercuts Graham et al.'s (10-16) halo rescue of the thermal Higgsino, which needed a tail to 1100 km/s. It also shifts inferred LZ splittings by up to ~130 keV.
- **[arXiv:2610.28744](https://arxiv.org/abs/2610.28744)** argues that observable RG running of neutrino mixing is an artifact. Short-baseline data already bound any angle change between production and detection to 0.7°–2.4°.
- **[arXiv:2610.32543](https://arxiv.org/abs/2610.32543)** gives the complete two-loop $t\bar t$ amplitudes, the first with genus-two functions in the finite remainder. Its public threshold evaluator is directly relevant to toponium fits, which Ball et al. tied to $m_t$.
- **[arXiv:2610.35619](https://arxiv.org/abs/2610.35619)**: Super-K reports a DSNB indication of $3.6^{+1.6}_{-1.5}$ cm⁻²s⁻¹ above 13.3 MeV at 2.6σ, robust across spectral models. It is the first non-limit result for this signal.

## Open questions

- Will the calibrations proposed in [arXiv:2610.27105](https://arxiv.org/abs/2610.27105) be performed, and does the halo of [arXiv:2610.28731](https://arxiv.org/abs/2610.28731) survive scrutiny? Either could collapse the event's model space.
- The GCE deflation ([arXiv:2610.32845](https://arxiv.org/abs/2610.32845)) weighs against joint LZ+GCE models such as [arXiv:2610.25423](https://arxiv.org/abs/2610.25423), which reappeared 10-27. Watch whether Fermi-LAT templates adopt time dependence.
- Mass ordering: the IO preference in mixing-scheme fits sits against earlier NO claims. Look for replies to [arXiv:2610.28744](https://arxiv.org/abs/2610.28744).
- How much of the DSNB 2.6σ comes from better atmospheric-background rejection versus the spectral fit? Watch for follow-ups from SK-Gd.
- Flavor-symmetry strain now spans $B\to PP$, $B\to DP$ (~60% breaking) and charm baryons. $\Lambda_c^+\to\Lambda K^+\eta$ was observed at >10σ well above SU(3) expectations ([arXiv:2610.31377](https://arxiv.org/abs/2610.31377)).
- Several flavor numbers await confrontation:
  - the $|V_{cb}|=0.042\pm0.002$ low-scale Pati–Salam prediction ([arXiv:2610.33152](https://arxiv.org/abs/2610.33152)), against the inclusive/exclusive split;
  - Belle II $B^+\to K^+\nu\bar\nu$ as dark matter ([arXiv:2610.34880](https://arxiv.org/abs/2610.34880));
  - the LHCb $T_{c\bar c1}(4430)^-$ seen in open charm ([arXiv:2610.35239](https://arxiv.org/abs/2610.35239)), consistent with $\psi(2S)\pi^-$.
- Unverified claims to recheck: the pre-excited cavity's noise treatment ([arXiv:2610.31717](https://arxiv.org/abs/2610.31717)), and whether agent-derived results stay faithful in light of [arXiv:2610.33134](https://arxiv.org/abs/2610.33134).

## Recurring references

- [arXiv:2610.27105](https://arxiv.org/abs/2610.27105): LZ ER-tail audit
- [arXiv:2610.28731](https://arxiv.org/abs/2610.28731): Gaia/LMC halo tail
- [arXiv:2610.27270](https://arxiv.org/abs/2610.27270): mixing schemes prefer IO
- [arXiv:2610.27236](https://arxiv.org/abs/2610.27236), [arXiv:2610.31881](https://arxiv.org/abs/2610.31881): CDM vs SIDM perturbers
- [arXiv:2610.28742](https://arxiv.org/abs/2610.28742), [arXiv:2610.32947](https://arxiv.org/abs/2610.32947): $0\nu\beta\beta$ error budget
- [arXiv:2610.28505](https://arxiv.org/abs/2610.28505), [arXiv:2610.31745](https://arxiv.org/abs/2610.31745): AI-theory blueprint → FeynFacet
- [arXiv:2610.27106](https://arxiv.org/abs/2610.27106), [arXiv:2610.29439](https://arxiv.org/abs/2610.29439): tagger compression
- [arXiv:2610.28400](https://arxiv.org/abs/2610.28400): cancelled eEDM leaves timelike τ dipole (echoed by [arXiv:2610.28790](https://arxiv.org/abs/2610.28790))
- [arXiv:2610.25423](https://arxiv.org/abs/2610.25423): dark-Higgs LZ+GCE model, reappeared 10-27
