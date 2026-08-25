# The Cross Section — Rolling Synthesis, week ending 2026-08-25

A collider-heavy week whose spine was CMS: the standout was the confirmation of a $t\bar t$-threshold excess in single leptons at 6.1σ, turning "toponium" from a dilepton curiosity into a two-channel result. Around it, several methodological currents kept compounding — quantum information at colliders pushing past entanglement, SMEFT hardening into the default language for top and diboson data, and an autodiff/ML-tooling wave spreading from analysis into simulation and cosmology. Precision nulls (flavor, LFV) held the line, while a lattice nEDM calculation reaffirmed strong-CP as a real problem. Dark-matter *detection methodology* — not results — dominated the DM conversation.

## Running themes

**Collider quantum information — heating.** The season-long thread accelerated and diversified. Entanglement work spanned gluon-pair Bell states ([arXiv:2608.17685](https://arxiv.org/abs/2608.17685)), GHZ/W states in Bethe–Heitler ([arXiv:2608.18030](https://arxiv.org/abs/2608.18030)), and a third graviton-squeezing no-go ([arXiv:2608.17015](https://arxiv.org/abs/2608.17015), after Bao et al. and Miyauchi et al. — the quantum-gravity wall keeps holding). It then moved *beyond* entanglement: "quantum magic"/nonstabilizerness in electroweak scattering, with the weak mixing angle again near a magic-minimizing value ([arXiv:2608.19095](https://arxiv.org/abs/2608.19095)), and tripartite entanglement as a selector of gauge/diffeomorphism invariance ([arXiv:2608.18732](https://arxiv.org/abs/2608.18732)).

**EFT as default collider language — heating.** A clear drift: CMS's most stringent aTGC bounds from merged-jet WW/WZ ([arXiv:2608.18245](https://arxiv.org/abs/2608.18245)), the first global top-FCNC fit over all 24 SMEFT operators ([arXiv:2608.19547](https://arxiv.org/abs/2608.19547)), basis-independent two-loop four-fermion running as tooling backbone ([arXiv:2608.19316](https://arxiv.org/abs/2608.19316)), and — newly — SMEFT used *diagnostically*: Englert et al. ([arXiv:2608.21510](https://arxiv.org/abs/2608.21510)) show single-top/$tH$ rate shifts fit a top-dipole-plus-TGC pattern no minimal UV multiplet reproduces.

**Dark-matter detection methodology — heating.** The week's DM weight was on new apparatus, not limits: quantum-dot "barcodes" for DM-electron operators ([arXiv:2608.18204](https://arxiv.org/abs/2608.18204)), JUNO Migdal sensitivity, X-ray-binary axion probes, then POLONAISE's levitated-ferromagnet ultraheavy search ([arXiv:2608.20464](https://arxiv.org/abs/2608.20464)), qubit-sensing field-building ([arXiv:2608.20745](https://arxiv.org/abs/2608.20745)), and an order-of-magnitude HFIR $n\to n'$ improvement ([arXiv:2608.21120](https://arxiv.org/abs/2608.21120), the recurring mirror-neutron channel).

**Autodiff / ML tooling wave — heating.** Differentiable methods spread outward: GW $H_0$ inference ([arXiv:2608.18281](https://arxiv.org/abs/2608.18281)), GPU-resident event generation with flow proposals ([arXiv:2608.21338](https://arxiv.org/abs/2608.21338)), calibrated-uncertainty flows and differentiable Parnassus ([arXiv:2608.21509](https://arxiv.org/abs/2608.21509), [arXiv:2608.22873](https://arxiv.org/abs/2608.22873)), and neural Boltzmann solvers reaching early-universe cosmology ([arXiv:2608.23022](https://arxiv.org/abs/2608.23022)). PHYSTAT opened a statistical-standards series for ML ([arXiv:2608.17724](https://arxiv.org/abs/2608.17724)).

**Flavor nulls consolidating — steady.** No new tension: LHCb's first $\Lambda_b\to\Lambda(1520)\mu\mu$ angular analysis is SM-consistent ([arXiv:2608.21082](https://arxiv.org/abs/2608.21082)), the baryonic complement to a $b\to s\ell\ell$ picture that has *consolidated* rather than tensioned since a mid-month $C_9$ flare. Belle II's $\tau\to\mu\gamma<9.5\times10^{-8}$ ([arXiv:2608.23009](https://arxiv.org/abs/2608.23009)) tightens the flagship LFV channel.

## Turning points

- **Toponium, now two channels** ([arXiv:2608.19546](https://arxiv.org/abs/2608.19546)): CMS's 6.1σ single-lepton confirmation of the $t\bar t$-threshold excess (5.1±0.9 pb, color-singlet pseudoscalar) independently corroborated the dilepton result — the week's clearest conversation-changer.
- **Deconfinement in a small system** ([arXiv:2608.18256](https://arxiv.org/abs/2608.18256)): CMS's first observation of $\Lambda/K^0_S$ baryon-to-meson enhancement in O-O, the payoff of the season's small-system flow program.
- **Strong-CP confirmed on the lattice** ([arXiv:2608.22587](https://arxiv.org/abs/2608.22587)): Blum et al.'s Feynman–Hellmann nEDM extraction ($|\bar\theta|\lesssim10^{-11}$) closes off "maybe strong-CP isn't real" and offers a method extendable to other CP-odd operators.

## Open questions

- **What is the toponium bump?** Simplified NRQCD pseudoscalar ([arXiv:2608.19546](https://arxiv.org/abs/2608.19546)) vs. top-philic 2HDM CP-odd Higgs ([arXiv:2608.19651](https://arxiv.org/abs/2608.19651), which found no viable baryogenesis branch). Watch further channels.
- **Two LHC excesses awaiting follow-up:** the 13.6-GeV CMS diphoton excess fit by a 10-GeV ALP ([arXiv:2608.18506](https://arxiv.org/abs/2608.18506)), and the 146-GeV $e\mu$ excess with proposed $H\gamma/Hj$ discriminators ([arXiv:2608.18738](https://arxiv.org/abs/2608.18738)).
- **Charm CPV still unexplained** ([arXiv:2608.21212](https://arxiv.org/abs/2608.21212)): Pich et al.'s tightened rescattering treatment concludes the SM still falls short — anomaly persists, not resolved.
- **$g_A$ radiative corrections:** Tomalak et al.'s $\Delta(1232)$ contribution nulls the radiative shift ([arXiv:2608.22845](https://arxiv.org/abs/2608.22845)), extending the neutron-decay $g_A$ thread (Gialidi et al., 08-18) — relevant to the lattice-vs-experiment debate.
- **EoS uncertainty quantification:** diffusion-model reconstruction ([arXiv:2608.17457](https://arxiv.org/abs/2608.17457)) vs. the caution that point-estimate MLPs understate high-density uncertainty ([arXiv:2608.19019](https://arxiv.org/abs/2608.19019)).

## Recurring references

- **[arXiv:2608.19546](https://arxiv.org/abs/2608.19546)** — CMS single-lepton toponium; the week's anchor result.
- **[arXiv:2608.18256](https://arxiv.org/abs/2608.18256)** — CMS O-O baryon-to-meson enhancement.
- **[arXiv:2608.22587](https://arxiv.org/abs/2608.22587)** — Lattice nEDM / strong-CP confirmation.
- **[arXiv:2608.19547](https://arxiv.org/abs/2608.19547)**, **[arXiv:2608.19316](https://arxiv.org/abs/2608.19316)**, **[arXiv:2608.21510](https://arxiv.org/abs/2608.21510)** — the top/EFT cluster (fit, tooling, diagnostic use).
- **[arXiv:2608.19095](https://arxiv.org/abs/2608.19095)** — quantum "magic" and the weak mixing angle.
- **[arXiv:2608.20464](https://arxiv.org/abs/2608.20464)** — POLONAISE levitated-magnet DM search.
- **[arXiv:2608.17457](https://arxiv.org/abs/2608.17457)** / **[arXiv:2608.19019](https://arxiv.org/abs/2608.19019)** — the paired EoS-uncertainty debate.
