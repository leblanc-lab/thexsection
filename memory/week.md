# The Cross Section — Weekly synthesis, week ending 2026-10-05

The week had two firm experimental anchors. JUNO gave the first reactor-plus-accelerator indication of normal ordering, and Super-K made its first reactor-antineutrino observation, which immediately disagrees with JUNO on $\Delta m^2_{21}$. Around them, three theory trajectories moved. Interpretation of the LZ recoil narrowed from broad model-building to a heavy-Higgsino survivor that depends on the LMC tail. Precision QCD advanced quickly, with four-loop splitting functions completed and jet-vetoed Higgs production reaching third order. LLM agents moved from writing about calculations to performing them. A quieter but recurring pattern was that "footnote" corrections turned out to be as large as the quoted uncertainties.

## Running themes

**LZ recoil: consolidating, volume fading.** The daily paper count fell from seven (09-29) to five (09-30), three (10-02) and one (10-05).
- **Halo.** The thread opened by asking whether the halo model changes the reading. Oliveira showed that excited-state fractions reshape the inference. Das et al., then Bozorgnia et al., showed that a Gaia-like halo hurts endothermic fits, while the LMC tail pushes them to larger splittings.
- **Solar capture.** Luengas et al. then used IceCube to require $\delta\gtrsim350$ keV, which kills most thermal multiplets under the Standard Halo Model. The LMC tail became the escape route.
- **Survivor.** By 10-05, Freese et al. found the thermal 1.1 TeV Higgsino only marginal, with 2 TeV to hundreds of TeV at δ≈350–525 keV comfortable. Hor et al. turned that region into a $p\to K^+\bar\nu$ prediction.
- **Testable side-routes.** These include a COSI line (Dutra), an argon line (Jho), atomic DM (Chanda) and straight-track multiple recoils (Meissner).

**Precision QCD and resummation: heating up.**
- **Splitting functions.** The four-loop non-singlet (Moch) and pure-singlet $P_{qq}$ (Gehrmann) results landed on consecutive days, completing the quark-to-quark splitting function.
- **Jet-vetoed Higgs.** It got its first NLL non-global treatment (Becher, 09-30) and then N³LO+N³LL at ~3% (Abreu, 10-05).
- **Other fronts.**
  - Resummation-scale uncertainty entered PDF fits (Abdolmaleki, followed by Giuli).
  - Drell-Yan reached N³LO with a lattice Collins–Soper kernel and positive weights (Assi).
  - Schalch's super-leading-log Monte Carlo opens a route to putting Glauber exchange into parton showers.

**LLMs inside calculations: new cluster, heating.**
- **Origin.** The cluster appeared on 09-30 with Camarda (agent-built NLO $V$+jet), He (LLM-designed IR subtraction) and Mikhasenko (agent-accessible Godfrey–Isgur).
- **Spread.** It then reached model space (hAIthem), retrieval (Kumar RAG) and a public bootstrap toolkit (Schwartz's BootLoops).
- **Background.** Thaler's stocktake, itself largely agent-written, framed HEPML as infrastructure. CMS's anomaly triggers and A-GHOST streaming back that view.

**Corrections the size of errors: emerged this week.**
- Žlebčík's helicity-convention fix moved the $\alpha$ tension by 0.8σ.
- Gaggero et al. found a −216 MeV shift in the top mass relation.
- Monahan et al. found an 11–13% shift in lattice gluon moments.
- Csanád et al. found a Neyman-χ² bias in histogram ratios.
- Zhong et al. found a >30% shift in NA62 dark-photon acceptance from the production model.
- Future digests should tag new instances as part of this pattern.

**Neutrino oscillation precision: heating.** JUNO gave ~1% precision on $\Delta m^2_{31}$ and the best solar parameters yet. Super-K's SK-Gd phase now adds an independent reactor measurement.

## Turning points

- **JUNO [arXiv:2609.37895](https://arxiv.org/abs/2609.37895).** Normal ordering is favored at ≥2.1σ for any CP phase, with a Bayes factor of 10.2. The collaboration calls this an indication, not a determination.
- **Luengas et al. [arXiv:2609.38316](https://arxiv.org/abs/2609.38316).** This became the reference solar-capture test for any heavy-multiplet LZ fit. Khan et al. explicitly conceded their GmSUGRA LZ branch to it.
- **Albaladejo et al. [arXiv:2609.38022](https://arxiv.org/abs/2609.38022).** A lattice-fixed prediction made with no LHCb input lands within 1.1–1.7σ of LHCb's beauty-strange state and effectively answers last week's mass-deficit question. It reads the state as a $\bar BK$ bound state and predicts a $1^+$ partner mass.
- **Dark Dimension graviton phenomenology.** It took two independent hits in three days:
  - Lee et al. showed KK-graviton decays are suppressed by $(q/m_n)^2$, ruling out existing cascade models.
  - Langhoff showed near-threshold decays are $d$-wave, excluding flat-dark-dimension graviton DM.
- **Žlebčík [arXiv:2609.31828](https://arxiv.org/abs/2609.31828).** The direct-versus-indirect $\alpha$ tension drops from 2.9σ to 2.1σ. Any isospin analysis built on a Dalitz fit now needs a convention check.

## Open questions

- **Solar–reactor $\Delta m^2_{21}$.** Super-K's value [arXiv:2610.03143](https://arxiv.org/abs/2610.03143) sits ~3σ above JUNO's and 1.9σ from SK's own solar data. Its $\sin^2\theta_{12}$ is still weakly constrained. Watch for updates with more SK-Gd exposure.
- **Robustness of the LZ solar bound.** Freese et al. flag that the bound depends on poorly known elastic Higgsino–nucleon scattering. Two experimental handles to watch:
  - Hyper-K/JUNO/DUNE reach on proton decay.
  - The argon and tungsten predictions from the side-routes.
- **What $X(2370)$ is.** Khemchandani et al. read it as $\phi h_1(1380)$ dynamics. Giacosa et al. read it as a pseudoscalar glueball coupled to fractional determinants, testable through $\eta\eta\eta$ and $\eta\eta\eta'$ rates.
- **Order of the chiral transition.** Pisarski's fractional-topology claim of a generically second-order transition awaits a 2+1-flavor lattice check and is likely to be contested.
- **$B^+\to K^+\nu\bar\nu$ enhancement.**
  - Belle II's WET reinterpretation prefers an enhanced vector contribution.
  - Baltà et al. tie the favored regions to $R(D^{(*)})$, where $b\to s\tau\tau$ could rise by orders of magnitude.
  - Jones-Pérez et al. find the standard-cosmology ALP reading marginal.
- **Smaller tensions to recheck.** MicroBooNE proton multiplicities, which no generator describes. The window-dependence of $D\pi$ femtoscopy fits. COMET muon yields ~30% above Geant4. The $\Xi_c\to\Xi$ lattice-versus-experiment puzzle.

## Recurring references

- [arXiv:2609.31828](https://arxiv.org/abs/2609.31828) — ρπ helicity convention; the anchor for "corrections the size of errors."
- [arXiv:2609.35650](https://arxiv.org/abs/2609.35650) — Oliveira: LZ intervals do not cover pseudo-Dirac halos.
- [arXiv:2609.36184](https://arxiv.org/abs/2609.36184) — Bozorgnia: the LMC tail, the escape route cited all week.
- [arXiv:2609.38316](https://arxiv.org/abs/2609.38316) — Luengas: the general-representation solar-capture bound.
- [arXiv:2610.03692](https://arxiv.org/abs/2610.03692) — Freese: the current state of the heavy-Higgsino LZ reading.
- [arXiv:2609.37895](https://arxiv.org/abs/2609.37895) — JUNO ordering and oscillation parameters.
- [arXiv:2610.03143](https://arxiv.org/abs/2610.03143) — Super-K's first reactor $\bar\nu_e$ observation.
- [arXiv:2609.34837](https://arxiv.org/abs/2609.34837) and [arXiv:2609.37563](https://arxiv.org/abs/2609.37563) — four-loop splitting functions (non-singlet and pure-singlet $P_{qq}$).
- [arXiv:2609.35972](https://arxiv.org/abs/2609.35972) and [arXiv:2610.03687](https://arxiv.org/abs/2610.03687) — jet-vetoed Higgs at NLL non-global, then at N³LO+N³LL.
- [arXiv:2609.37238](https://arxiv.org/abs/2609.37238) — agent-built NLO, the founding paper of the LLM-in-the-loop cluster.
- [arXiv:2609.36234](https://arxiv.org/abs/2609.36234) and [arXiv:2610.01825](https://arxiv.org/abs/2610.01825) — the two independent hits on the Dark Dimension program.
- [arXiv:2609.37146](https://arxiv.org/abs/2609.37146) — Belle II $K\nu\bar\nu$ WET reinterpretation.
