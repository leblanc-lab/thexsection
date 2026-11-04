# The Cross Section: rolling synthesis, week ending 2026-11-03

Three digests (10-28, 11-02, 11-03) fed this week. Two threads gained momentum. Oxygen collisions began producing *discriminating* collectivity measurements, and the field turned its error-budget scrutiny from physics inputs to the machinery itself: fitters, loop orders and phase-transition dynamics. The lensing case against CDM-density subhalos strengthened into a population-level result. In flavor, the cleanest channels kept landing on the SM while $C_9$ and $|V_{cb}|$ stayed open. Tagger work moved from "can it shrink" to "what survives quantization." The 248 keV LZ event got its first model after two quiet days.

## Running themes

- **Small systems, partonic (heating).** ALICE's φ $v_2$ in O–O ([arXiv:2610.36237](https://arxiv.org/abs/2610.36237)) tracks the $K^0_S$, not the near-equal-mass Λ. That favors recombination from a flowing partonic medium over mass ordering, and it is sharper than the CMS O–O baryon/meson anchor ([arXiv:2608.18256](https://arxiv.org/abs/2608.18256)). Mallick et al. ([arXiv:2610.36922](https://arxiv.org/abs/2610.36922)) supply the needed nonflow control by validating on flow-free Angantyr. Ne–Ne geometry tagging ([arXiv:2610.40724](https://arxiv.org/abs/2610.40724)) signals the program moving past oxygen.
- **Error budgets in the machinery (heating, broadening).** The thread started with fits:
  - BFGS beats Migrad by ~10× ([arXiv:2610.35927](https://arxiv.org/abs/2610.35927)).
  - NTK modes in PDF fits ([arXiv:2610.36034](https://arxiv.org/abs/2610.36034)).
  - SIGMA ([arXiv:2610.37398](https://arxiv.org/abs/2610.37398)).
  - Hessian-missed nPDF minima ([arXiv:2610.37254](https://arxiv.org/abs/2610.37254)).

  It then jumped to GW forecasts. Three papers drop idealizations: gravity couplings, sound-wave leakage and non-spherical bubbles ([arXiv:2610.40775](https://arxiv.org/abs/2610.40775), [arXiv:2610.40781](https://arxiv.org/abs/2610.40781), [arXiv:2610.41504](https://arxiv.org/abs/2610.41504)). Chiang ([arXiv:2611.01634](https://arxiv.org/abs/2611.01634)) shows the $v_c/T_c>1$ criterion flags transitions that never complete. The ones that do complete are weak and far below LISA. The common message is that a prediction is only as good as its least-examined step.
- **Loop order decides (new, likely to recur).** Allwicher et al. ([arXiv:2610.40821](https://arxiv.org/abs/2610.40821)) find that Tera-$Z$ precision makes higher-loop running decisive. Kühler et al.'s full one-loop SM in BMHV ([arXiv:2611.00141](https://arxiv.org/abs/2611.00141)) is groundwork for the multi-loop EW precision this demands.
- **Taggers: compression → diagnosis → quantization (steady, maturing).**
  - CoReNet matches a 100× larger transformer with 1508 parameters ([arXiv:2610.40749](https://arxiv.org/abs/2610.40749)) and is already used in CMS searches.
  - Model stitching locates the Lund-plane deficit ([arXiv:2610.37137](https://arxiv.org/abs/2610.37137)).
  - SCRAMJet's "virtual channels" ([arXiv:2611.00086](https://arxiv.org/abs/2611.00086)): attention channels vanish from the compiled circuit while still carrying signal in training. This is a concrete pitfall for HGQ-style training.
- **SIDM vs CDM in lensing (heating).** Gilman et al.'s 29-quad population ([arXiv:2610.40766](https://arxiv.org/abs/2610.40766)) favors core collapse and attaches a particle model. That model is 20–80 GeV DM with an MeV mediator, pushed toward a neutrinophilic scalar. It is the third result in two weeks against CDM-density subhalos (after Zhang et al. and Tekverk et al.), though the authors still say "hints."
- **Flavor split (steady).** LHCb Upgrade I's first rare-decay results ([arXiv:2611.00230](https://arxiv.org/abs/2611.00230)) are SM-consistent. CMS's $|V_{cb}|$ from $t\bar t$ ([arXiv:2611.01274](https://arxiv.org/abs/2611.01274)) is free of hadronic inputs but carries ~19% uncertainty, too large to arbitrate yet.

## Turning points

- **φ $v_2$ in O–O:** the cleanest mass-ordering vs recombination test lands on recombination.
- **Minimal SUSY SU(5) flips with loop order:** two loops point to PeV SUSY, while three loops appear to exclude the model. This is now the reference example for "precision demands higher loops."
- **CONUS+ reaches 10.2σ** ([arXiv:2610.37318](https://arxiv.org/abs/2610.37318), [arXiv:2610.37345](https://arxiv.org/abs/2610.37345)). Reactor CEνNS is now precision physics: $N_s/N_{\rm SM}=0.91\pm0.14$, with $\sin^2\theta_W=0.225\pm0.022$ at ~10 MeV.
- **Lensing goes population-level:** this upgrades the SIDM case from per-perturber anecdotes.
- **Upgrade I delivers physics:** first single-experiment evidence for $B^0\to\mu^+\mu^-$.

## Open questions

- **LZ 248 keV event.** Roy et al. ([arXiv:2611.01158](https://arxiv.org/abs/2611.01158)) give the first model: an exothermic Higgs-portal relic needing no high-velocity tail. It predicts a sub-MeV photon continuum for COSI. Watch for competing models and experimental follow-up.
- **Negative $\sum m_\nu$ preference.** Two papers pull in opposite directions:
  - Late reheating ([arXiv:2610.36062](https://arxiv.org/abs/2610.36062)) could lower the cosmological ν density by up to 5×.
  - Thermal Festina Lente ([arXiv:2611.02559](https://arxiv.org/abs/2611.02559)) requires $m_{\nu,\rm lightest}>10$–43 meV, in tension with DESI DR2.
- **$|V_{cb}|$ inclusive/exclusive and $C_9$.** These remain live. The $B^0/B_s$ ratio numbers from LHCb were not in the abstract, so check them.
- **Small-$x$ non-planar $\zeta_2$ violations** in the 3- and 4-loop splitting functions. Adelaja et al. ([arXiv:2610.40823](https://arxiv.org/abs/2610.40823)) propose a soft-gluon origin with five-loop predictions, which makes it testable.
- **SIDM model viability.** The required $\sigma/m\sim10^2$–$10^4$ cm²/g and the mediator constraints need independent checks.
- **UHECR claim.** Suliga et al. ([arXiv:2611.00205](https://arxiv.org/abs/2611.00205)) claim ≥7.2σ for two light-nucleus populations, pointing to neutron-star-merger origins. The model dependence is unexamined, so flag any rebuttals.
- **Agents and provenance.** Gao et al. ([arXiv:2611.03373](https://arxiv.org/abs/2611.03373)) had an agent reproduce a CEPC analysis to ~2% without targets. CELEBI ([arXiv:2611.01788](https://arxiv.org/abs/2611.01788)) pins results to immutable analysis states. Watch whether provenance tooling spreads after QFT-Bench's unfaithful-reasoning finding (10-27).

## Recurring references

- [arXiv:2610.36237](https://arxiv.org/abs/2610.36237): φ $v_2$, O–O. Anchor for small-system partonic collectivity.
- [arXiv:2608.18256](https://arxiv.org/abs/2608.18256): CMS O–O baryon/meson enhancement, the year's earlier small-system anchor.
- [arXiv:2610.40766](https://arxiv.org/abs/2610.40766): 29-lens core-collapse population. Anchor for the SIDM-vs-CDM thread.
- [arXiv:2610.40821](https://arxiv.org/abs/2610.40821): the SU(5) loop-order flip.
- [arXiv:2610.37318](https://arxiv.org/abs/2610.37318): CONUS+ precision CEνNS.
- [arXiv:2611.00230](https://arxiv.org/abs/2611.00230): LHCb Upgrade I $B_{(s)}\to\mu\mu$.
- [arXiv:2611.01274](https://arxiv.org/abs/2611.01274): CMS $|V_{cb}|$ from top decays.
- [arXiv:2611.00086](https://arxiv.org/abs/2611.00086): SCRAMJet, "virtual channels" in quantization-aware training.
- [arXiv:2610.40749](https://arxiv.org/abs/2610.40749): CoReNet, structure over size.
- [arXiv:2611.01634](https://arxiv.org/abs/2611.01634): which phase transitions actually complete.
- [arXiv:2611.01158](https://arxiv.org/abs/2611.01158): first model for the LZ 248 keV event.
