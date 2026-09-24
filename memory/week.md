# The Cross Section: rolling synthesis, week ending 2026-09-24

This week the experiments led the conversation. A run of hadron-spectroscopy discoveries (LHCb's $\Omega_{cc}^+$, then a light, narrow beauty-strange state, plus BESIII's η(2600) and double-$s\bar s$) was the dominant experimental story. Belle II's $R(D^{(*)})$ eased the flavor tension rather than feeding it. The LZ 248 keV recoil kept producing theory, but it changed modes almost daily: bounds, then confining dark sectors, then elastic form factors, then models engineered around solar capture. The statistics and tooling thread matured from infrastructure into physics use, culminating in a simulation-based-inference (SBI) reanalysis that cut the MiniBooNE+MicroBooNE sterile-neutrino preference to 2.7σ. Precision multiloop QCD ran steadily underneath. Nucleon structure, which led early in the week, faded after 09-18.

## Running themes

- **LZ recoil interpretation: steady in volume, changing in character.** On 09-21 the papers were constraint and complementarity work: solar capture at IceCube/Super-K ruled out weak-scale elastic operators ([arXiv:2609.21823](https://arxiv.org/abs/2609.21823)), and halo co-rotation does not rescue the high-velocity tail ([arXiv:2609.21444](https://arxiv.org/abs/2609.21444)).
  - 09-22 brought composite inelastic dark-QCD readings ([arXiv:2609.24988](https://arxiv.org/abs/2609.24988), [arXiv:2609.23477](https://arxiv.org/abs/2609.23477)).
  - 09-23 brought elastic composite form-factor readings ([arXiv:2609.25723](https://arxiv.org/abs/2609.25723)).
  - 09-24 brought models designed around solar capture, one admitting severe fine-tuning ([arXiv:2609.28129](https://arxiv.org/abs/2609.28129)).
  - Maier et al. place thermal electroweak multiplets beyond HL-LHC reach ([arXiv:2609.26870](https://arxiv.org/abs/2609.26870)). The trend is more model-building under tightening constraints.
- **Heavy-flavor spectroscopy: heating up.**
  - LHCb observed $\Omega_{cc}^+$ at 8.7σ ([arXiv:2609.21921](https://arxiv.org/abs/2609.21921)) and a >7σ beauty-strange state with a quark-model mass deficit ([arXiv:2609.25178](https://arxiv.org/abs/2609.25178)).
  - BESIII added η(2600) ([arXiv:2609.25158](https://arxiv.org/abs/2609.25158)) and the $\Omega_b^-$ lifetime ([arXiv:2609.25370](https://arxiv.org/abs/2609.25370)).
  - Earlier, BESIII's double-$s\bar s$ result at 40% of the inclusive φ rate ([arXiv:2609.20154](https://arxiv.org/abs/2609.20154)) echoed the double-charm puzzle.
  - The digests read the pace as experiments filling in, and now breaking out of, the conventional spectrum.
- **Statistics and inference tooling: steady, now reaching physics.**
  - Infrastructure on 09-18: IRIS-HEP blueprint ([arXiv:2609.19992](https://arxiv.org/abs/2609.19992)), RooFit→autodiff/JAX/HS3 ([arXiv:2609.19761](https://arxiv.org/abs/2609.19761)), Combine in PyHEP ([arXiv:2609.19753](https://arxiv.org/abs/2609.19753)).
  - Conceptual turn: Dorigo shows ordering can fail even under exact calibration ([arXiv:2609.20007](https://arxiv.org/abs/2609.20007)).
  - Physics application on 09-24 via the SBI sterile-neutrino fit ([arXiv:2609.26965](https://arxiv.org/abs/2609.26965)).
  - AutoTherm ([arXiv:2609.20936](https://arxiv.org/abs/2609.20936)) carried the automation ethos into thermal field theory.
- **Precision multiloop QCD: steady.** Blümlein et al. completed the gluonic three-loop massive form factors ([arXiv:2609.22034](https://arxiv.org/abs/2609.22034), with methods in [arXiv:2609.24279](https://arxiv.org/abs/2609.24279)). Kidonakis pushed the four-loop massive cusp anomalous dimension ([arXiv:2609.23247](https://arxiv.org/abs/2609.23247)). Klann et al. flagged up-to-20% errors in DIS heavy-quark parametrisations ([arXiv:2609.23452](https://arxiv.org/abs/2609.23452)).
- **Trigger ML and HL-LHC tracking: heating up.** CMS converged on a heterogeneous mkFit+Patatrack+LST tracking baseline ([arXiv:2609.26695](https://arxiv.org/abs/2609.26695)). The FPGA ML papers were a foundation-model distillation ([arXiv:2609.26899](https://arxiv.org/abs/2609.26899)) and INT8 GraphSAGE at 53 ns ([arXiv:2609.28144](https://arxiv.org/abs/2609.28144)). Both extend the CMS L1 distillation work from 09-15.
- **Nucleon structure and GPDs: fading.** This thread peaked 09-18 with the first comprehensive GPD review in two decades ([arXiv:2609.19544](https://arxiv.org/abs/2609.19544)). The same day, Su et al. opened the lattice $x\sim\pm\xi$ region ([arXiv:2609.20545](https://arxiv.org/abs/2609.20545)). It had little presence afterward.

## Turning points

- **Belle II $R(D^*)=0.242\pm0.019\pm0.016$** ([arXiv:2609.21947](https://arxiv.org/abs/2609.21947)). The central value sits slightly below the SM, a notable data point against the long-flagged LFU tension.
- **ATLAS direct $\Gamma_H<307$ MeV** from on-shell γγ interference ([arXiv:2609.19948](https://arxiv.org/abs/2609.19948)). It needs no coupling assumptions and complements off-shell bounds.
- **Lattice $\mathcal{C}_{\rm QCD}=1.965(35)$** ([arXiv:2609.22698](https://arxiv.org/abs/2609.22698)). This resolves a ChPT discrepancy and gives axion searches a benchmark.
- **ATLAS top-philic $Z'$ excluded below 1150 GeV** ([arXiv:2609.24950](https://arxiv.org/abs/2609.24950)). It constrains the vector side of the toponium debate. Toponium production prospects look poor at muon colliders and in UPCs ([arXiv:2609.23576](https://arxiv.org/abs/2609.23576)), and feasible in ultraperipheral pp only at FCC-hh ([arXiv:2609.28223](https://arxiv.org/abs/2609.28223)).
- **MiniBooNE+MicroBooNE 3+1 preference drops to 2.7σ** ([arXiv:2609.26965](https://arxiv.org/abs/2609.26965)), with ≥2.5σ internal disagreement between the two experiments.

## Open questions

- **LZ recoil:** will the decisive 271–800 keV sideband search ([arXiv:2609.26698](https://arxiv.org/abs/2609.26698)) arrive? Watch whether fine-tuning pressure from solar capture thins the model zoo. Nuclear form-factor uncertainties also sit under every limit ([arXiv:2609.24764](https://arxiv.org/abs/2609.24764)).
- **Nature of the LHCb beauty-strange state** ([arXiv:2609.25178](https://arxiv.org/abs/2609.25178)): watch for theory interpretations, molecular or otherwise, and whether it is a first open-beauty counterpart to the charm exotics.
- **LFU after Belle II:** does the tension survive the next combination?
- **Short-baseline anomaly:** can the MiniBooNE–MicroBooNE internal tension be resolved within 3+1?
- **Hadronization:** the double-$s\bar s$ and double-$c\bar c$ rates remain unexplained.
- **Baryogenesis timing as a gravitational-wave observable:** BBN deuterium disfavors NANOGrav-compatible supercooled transitions if the asymmetry came first ([arXiv:2609.28348](https://arxiv.org/abs/2609.28348), [arXiv:2609.27978](https://arxiv.org/abs/2609.27978)). This thread is new on 09-24. Related: Co et al.'s rotating-axion link between CMB birefringence and the baryon asymmetry ([arXiv:2609.25202](https://arxiv.org/abs/2609.25202)).
- **Collider quantum information:** the NAQC certification proposal for τ pairs ([arXiv:2609.25214](https://arxiv.org/abs/2609.25214)) is in tension with tomography positivity failures at NLO ([arXiv:2609.25217](https://arxiv.org/abs/2609.25217)).

## Recurring references

- [arXiv:2609.21947](https://arxiv.org/abs/2609.21947): Belle II $R(D^{(*)})$
- [arXiv:2609.25178](https://arxiv.org/abs/2609.25178): LHCb beauty-strange state
- [arXiv:2609.21921](https://arxiv.org/abs/2609.21921): LHCb $\Omega_{cc}^+$
- [arXiv:2609.22034](https://arxiv.org/abs/2609.22034) and [arXiv:2609.24279](https://arxiv.org/abs/2609.24279): three-loop gluonic form factors
- [arXiv:2609.20007](https://arxiv.org/abs/2609.20007): Dorigo, coverage vs. ordering
- [arXiv:2609.26965](https://arxiv.org/abs/2609.26965): SBI sterile-neutrino fit
- [arXiv:2609.21823](https://arxiv.org/abs/2609.21823): LZ solar-capture constraint
- [arXiv:2609.24988](https://arxiv.org/abs/2609.24988): dark-QCD LZ reading
- [arXiv:2609.22698](https://arxiv.org/abs/2609.22698): lattice axion-photon coupling
