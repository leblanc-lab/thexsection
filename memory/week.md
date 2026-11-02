# The Cross Section: Rolling Synthesis, week ending 2026-11-02

This week the oxygen-run heavy-ion program moved from showing that collective effects exist to measurements that discriminate between explanations. The φ meson's flow came out on the recombination side. Strong-lensing evidence against CDM-density subhalos reached a population-level result with a particle model attached. Precision theory produced a sharp flip: adding one loop order appears to exclude minimal SUSY SU(5). A broader "error-budget" mood ran from fitter benchmarks to gravitational-wave forecasts from phase transitions. Neutrino physics delivered a first 2.6σ hint of relic supernova neutrinos and a precision reactor CEνNS result. The 248 keV LZ event is going quiet.

## Running themes

- **Small-system QGP in O–O and beyond (heating).**
  - The first O–O $I_{AA}$ ([arXiv:2610.35331](https://arxiv.org/abs/2610.35331)) shows away-side suppression weaker than in central Pb–Pb.
  - The first φ $v_2$ in a small system ([arXiv:2610.36237](https://arxiv.org/abs/2610.36237)) tracks the $K^0_S$ rather than the Λ.
  - A validated nonflow subtraction ([arXiv:2610.36922](https://arxiv.org/abs/2610.36922)) supplies the control these low-multiplicity observables need.
  - Ne–Ne geometry tagging ([arXiv:2610.40724](https://arxiv.org/abs/2610.40724)) signals the program moving past oxygen.
  - The year's anchor remains CMS's O–O baryon-to-meson enhancement ([arXiv:2608.18256](https://arxiv.org/abs/2608.18256)).
- **SIDM vs CDM in strong lensing (heating).** Gilman et al. ([arXiv:2610.40766](https://arxiv.org/abs/2610.40766)) use 29 quad lenses and find halo densities consistent with gravothermal core collapse. Their favored model is 20–80 GeV DM with MeV mediators, pushed toward an invisibly decaying neutrinophilic scalar. It is the third result in two weeks after Zhang et al. and Tekverk et al., though the authors still say "hints."
- **Error budgets in the statistical machinery (steady, spreading).**
  - **Fitters:** BFGS variants run about 10× faster than Migrad at equal precision ([arXiv:2610.35927](https://arxiv.org/abs/2610.35927)).
  - **PDF training dynamics:** NTK analysis of PDF fits ([arXiv:2610.36034](https://arxiv.org/abs/2610.36034)) finds the data noise sits in late-learned modes.
  - **Generative-model fits:** SIGMA ([arXiv:2610.37398](https://arxiv.org/abs/2610.37398)) profiles fit uncertainty inside the goodness-of-fit test.
  - **nPDFs:** lead nPDFs have secondary minima that the Hessian method misses ([arXiv:2610.37254](https://arxiv.org/abs/2610.37254)).
  - **GW forecasts:** by 11-02 the same mood reached phase transitions, with three papers each dropping an idealization ([arXiv:2610.40775](https://arxiv.org/abs/2610.40775), [arXiv:2610.40781](https://arxiv.org/abs/2610.40781), [arXiv:2610.41504](https://arxiv.org/abs/2610.41504)).
- **Loop order as decider (steady).**
  - Minimal SU(5) needs PeV SUSY at two loops but appears excluded at three ([arXiv:2610.40821](https://arxiv.org/abs/2610.40821)).
  - A soft-gluon mechanism is proposed for September's non-planar $\zeta_2$ violations ([arXiv:2610.40823](https://arxiv.org/abs/2610.40823)).
  - Leading-colour two-loop $t\bar t\gamma$ integrals are now complete ([arXiv:2610.42062](https://arxiv.org/abs/2610.42062)).
  - A four-loop $\overline{\rm MS}$-pole mass relation with two masses appeared ([arXiv:2610.33164](https://arxiv.org/abs/2610.33164)).
  - Linear IR terms cancel through NNLO with a short-distance mass ([arXiv:2610.36065](https://arxiv.org/abs/2610.36065)), which bears on the top-mass threads.
- **ML: structure and diagnosis over scale (steady).**
  - Model stitching locates the Lund-plane tagger's deficit relative to ParT ([arXiv:2610.37137](https://arxiv.org/abs/2610.37137)).
  - CoReNet ([arXiv:2610.40749](https://arxiv.org/abs/2610.40749)) matches a transformer over 100× larger with 1508 parameters and is already used in several CMS searches.
  - An information ladder for calorimeters ([arXiv:2610.41894](https://arxiv.org/abs/2610.41894)) assigns a measured value to each readout dimension.
  - Agentic and LLM work continues: QFT-Bench ([arXiv:2610.33134](https://arxiv.org/abs/2610.33134)) and proton_agent ([arXiv:2610.33593](https://arxiv.org/abs/2610.33593)).
- **248 keV LZ event (fading).** The inelastic-kinematics spillover came on 10-27: the neutrino fog for inelastic scattering ([arXiv:2610.35789](https://arxiv.org/abs/2610.35789)) and the 10-20 dark-Higgs model resurfacing in that day's listing ([arXiv:2610.25423](https://arxiv.org/abs/2610.25423)). The event itself drew no papers on 10-28 or 11-02.

## Turning points

- **φ flow favors recombination.** The near-Λ-mass φ shows meson-like $v_2$, which disfavors a purely mass-driven pattern in O–O ([arXiv:2610.36237](https://arxiv.org/abs/2610.36237)).
- **Antideuteron interpretation shifts.** The antideuteron–net-Λ correlation matches Thermal-FIST in Pb–Pb ([arXiv:2610.36307](https://arxiv.org/abs/2610.36307)). The earlier antideuteron–antiproton discrepancy therefore looks like a nucleosynthesis effect, not a hadronization one.
- **Minimal SUSY SU(5) at three loops.** Going from two to three loops flips the model from viable to apparently excluded under Tera-$Z$ precision ([arXiv:2610.40821](https://arxiv.org/abs/2610.40821)).
- **Reactor CEνNS goes precision.**
  - CONUS+ reports a 10.2σ blind result with $N_s/N_{\rm SM}=0.91\pm0.14$ ([arXiv:2610.37318](https://arxiv.org/abs/2610.37318), [arXiv:2610.37345](https://arxiv.org/abs/2610.37345)).
  - Its $\sin^2\theta_W=0.225\pm0.022$ is a single-experiment point. It sits beside the prior week's combined CEνNS+ν–e value of $0.233^{+0.007}_{-0.006}$.
- **First DSNB hint.** Super-K sees $\bar\nu_e$ from the diffuse supernova background at 2.6σ ([arXiv:2610.35619](https://arxiv.org/abs/2610.35619)), the first indication after a history of limits.
- **Hidden-charm state confirmed in open charm.** The $T_{c\bar c1}(4430)^-$ shows up at >5σ in an open-charm channel ([arXiv:2610.35239](https://arxiv.org/abs/2610.35239)), consistent with the $\psi(2S)\pi^-$ measurement.

## Open questions

- **DSNB significance.** How much of the 2.6σ comes from improved atmospheric-background rejection versus the spectral fit ([arXiv:2610.35619](https://arxiv.org/abs/2610.35619))? Watch for an independent check.
- **Negative $\sum m_\nu$ preference persists.**
  - Dark-sector interactions do not rescue positive masses ([arXiv:2610.33729](https://arxiv.org/abs/2610.33729)).
  - Late reheating could cut the cosmological mass density by up to 5× ([arXiv:2610.36062](https://arxiv.org/abs/2610.36062)).
- **SIDM lensing.** Can the neutrinophilic-mediator corner survive dedicated bounds, and will per-perturber and population analyses converge ([arXiv:2610.40766](https://arxiv.org/abs/2610.40766))?
- **$|V_{cb}|$ split.** Low-scale Pati–Salam predicts $|V_{cb}|=0.042\pm0.002$ ([arXiv:2610.33152](https://arxiv.org/abs/2610.33152)) against the unresolved inclusive/exclusive tension. Related texture work favors inverted ordering ([arXiv:2610.35587](https://arxiv.org/abs/2610.35587)), echoing Gluza et al.
- **Five-loop $\zeta_2$ prediction.** It awaits a test ([arXiv:2610.40823](https://arxiv.org/abs/2610.40823)).
- **O–O $I_{AA}$ caveats.** Selection biases and cold-nuclear-matter effects remain open ([arXiv:2610.35331](https://arxiv.org/abs/2610.35331)).
- **Belle II $B^+\to K^+\nu\bar\nu$ excess.** It is still drawing DM interpretations constrained by $B^0\to K^{*0}+$inv ([arXiv:2610.34880](https://arxiv.org/abs/2610.34880)).
- **Unfaithful LLM reasoning.** Frontier models exceed 95% on QFT-Bench but often fail to justify their correct answers ([arXiv:2610.33134](https://arxiv.org/abs/2610.33134)). This matters for anyone handing derivations to agents.

## Recurring references

- [arXiv:2608.18256](https://arxiv.org/abs/2608.18256): CMS O–O baryon/meson enhancement, the small-system anchor.
- [arXiv:2610.36237](https://arxiv.org/abs/2610.36237): ALICE φ $v_2$ in O–O.
- [arXiv:2610.40766](https://arxiv.org/abs/2610.40766): 29-lens core-collapse SIDM.
- [arXiv:2610.40821](https://arxiv.org/abs/2610.40821): three-loop SU(5) exclusion.
- [arXiv:2610.37318](https://arxiv.org/abs/2610.37318): CONUS+ CEνNS.
- [arXiv:2610.35619](https://arxiv.org/abs/2610.35619): Super-K DSNB hint.
- [arXiv:2610.25423](https://arxiv.org/abs/2610.25423): dark-Higgs model for the LZ event and the GCE, first covered 10-20.
- [arXiv:2610.40749](https://arxiv.org/abs/2610.40749): CoReNet.
