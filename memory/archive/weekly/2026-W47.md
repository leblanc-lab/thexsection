# The Cross Section — Rolling synthesis, week ending 2026-11-19

The week's dominant mood was **auditing**: what quoted limits, error bars, priors and proofs actually mean. The field's own results were the main target. Two physics threads kept pace with the audits. The first was steady model-building around the 248 keV LZ event, now centered on solar capture. The second was the gravitational-wave phase-transition program. Its weak links moved this week: away from the nucleation rate, and toward wall hydrodynamics and astrophysical priors. Superallowed $V_{ud}$ became a new nuclear-theory front. A fresh 3.5σ ATLAS excess arrived the day before a paper questioning how ATLAS builds its expected limits.

## Running themes

- **LZ 248 keV event (steady, maturing).**
  - Models now get judged by whether they survive solar capture.
  - Bera et al. broke the all-inelastic pattern with an elastic anapole Majorana fermion: ~300 GeV, relic density matched, more events predicted at low energy. The abstract doesn't address solar capture.
  - Lin et al. recomputed capture with a transport equation. When nuclear scattering is rare, annihilation drops by orders of magnitude. For the inelastic higgsino, the splitting bound tightens by tens of keV.
  - Buttazzo et al. (composite Higgs, few TeV, ~300 keV splitting) is the first in this run to claim solar capture, the high-energy sideband and gamma rays together.
  - Leng et al. (radion portal) used only a solar-neutrino proxy.
  - Dai et al. added the first three-bin likelihood fit.
- **GW phase-transition forecasts (heating).**
  - 11-13 to 11-16: forecasts are only as good as the transition dynamics. Zhang et al. showed homogeneity fails near the completion boundary. Barni et al. showed $(\xi_w,\alpha_N)$ need not fix a unique wall flow.
  - 11-17: Zhou et al.'s lattice nucleation rate sits only ~8% from one loop, and Gil et al. found modest higher-dimension-operator corrections. The rate itself looks robust.
  - 11-19: the same fragility appeared on the data side. Bringmann et al. cut the PTA preference for a phase transition from 2.8σ to 1.5σ with a realistic SMBHB population. AbdusSalam et al. found LVK constraints are prior-dominated.
- **Self-audit of limits and inputs (heating).**
  - Bounds loosened first: Suezaki's supernova core-heating recount (~50× weaker Fornax limit) and Cappiello's resonant trapping.
  - Windows then closed: Blinov's pion chimney and Fiorillo's SN 1987A neutrino dipole bound.
  - Inputs were audited too: HERA systematics treated as uncertain (Canonero), adaptive-integrator NLL artifacts (Zhu), and a gap found and closed in a published proof using Lean 4 (Chen).
  - 11-19: Şahin et al. found ATLAS places 99.2% of observed limits inside its 2σ band, against CMS's nominal 95.3%.
- **Superallowed $V_{ud}$ (new, heating).**
  - Novario et al. (coupled-cluster EFT, 12 transitions) leave a floor of $\delta V_{ud}\simeq6\times10^{-4}$ from a contact-term combination that is correlated with $V_{ud}$ itself.
  - Chambers-Wall et al. (QMC) find three-nucleon $\mathcal{O}(\alpha^2)$ terms that move $V_{ud}$ at the 10⁻⁴ level.
- **Loop counts (steady).**
  - Six-loop QED (Li), with six-loop QCD flagged as next.
  - Three-loop $V$+jet (Gehrmann).
  - Same-day N³LO pieces for $B\to\gamma\ell\nu$ from three groups (Huang, Liu, Ji), aimed at $\lambda_B$.
- **Superradiance clouds shrinking (emerging).**
  - Foster et al.'s gravitational Auger effect and Bottaro et al.'s self-interaction cap reach the same conclusion by different mechanisms: black-hole spin bounds on axions need revisiting.

## Turning points

- **Solar capture recomputed** (Lin et al.). It is now the yardstick for LZ models, and its verdict cuts both ways depending on the scattering regime.
- **Nucleation exonerated, hydrodynamics implicated.** The lattice result moves GW-forecast scrutiny downstream to walls. Barni et al.'s public code HydróDex is the tool to watch.
- **PTA phase-transition hint softened** to 1.5σ. It returns above 3σ only if binaries take more than ~6.5 Gyr to merge.
- **ATLAS limit coverage anomaly.** The leading explanation is expected limits computed after a fit to data, which is the default in common tools. This recasts how ATLAS excesses and limits should be read.
- **Method adoption:** ATLAS published the first unbinned, fully differential collider cross section (OmniFold Z+jets), released as reusable events with unfolded weights.

## Open questions

- **ATLAS instanton-like excess (3.5σ).** Is it local? Is the minimum-bias background modeling sound? It joins the 13.6 GeV diphoton and 146 GeV $e\mu$ excesses on the unclosed list.
- **Expected-limit method.** Which method did each ATLAS search use? Watch for responses to Şahin's disclosure recommendation.
- **LZ.** Do Bera's anapole model and Leng's radion model survive Lin's capture calculation? The full LZ run will test Bera's low-energy prediction and the sideband.
- **$V_{ud}$.** Neither abstract gives a first-row unitarity verdict. In ¹⁰C, coupled-cluster sits 30% below QMC. Which nuclear input breaks the contact-term degeneracy?
- **$B\to\gamma\ell\nu$.** The three groups' overlapping three-loop results have not yet been compared.
- **Chiral lattice fermions.** Liu proved that Craig's overlap measure and the Hsu/Witten continuum determinant agree for one SU(5) generation on $T^4$. This answers the comparison Witten's 11-05 note invited. Lu et al. then showed the overlap Weyl fermion is not reflection positive at finite spacing. How the two results fit together is unresolved.
- **Unreported numbers.** The NA62 $K^+\to\pi^+\nu\bar\nu$ central value is not in the abstract. Neither is which side of the inclusive/exclusive split Qu et al.'s $|V_{cb}|$ lands on.
- **Spectroscopy.** The glueball reading of X(2370) is weakening (Peng et al.; Kang's 11-10 sum-rule result). BESIII's $K_1^*(1870)$ $K\eta'$ channel sits awkwardly with the 3S–2D interpretation.

## Recurring references

- LZ: [arXiv:2611.16689](https://arxiv.org/abs/2611.16689) (solar capture), [arXiv:2611.15957](https://arxiv.org/abs/2611.15957) (anapole), [arXiv:2611.21737](https://arxiv.org/abs/2611.21737) (composite), [arXiv:2611.22890](https://arxiv.org/abs/2611.22890) (radion), [arXiv:2611.16553](https://arxiv.org/abs/2611.16553) (B−L fit)
- GW: [arXiv:2611.17402](https://arxiv.org/abs/2611.17402), [arXiv:2611.17411](https://arxiv.org/abs/2611.17411) (wall hydrodynamics), [arXiv:2611.18794](https://arxiv.org/abs/2611.18794) (lattice nucleation), [arXiv:2611.23371](https://arxiv.org/abs/2611.23371) (PTA priors), [arXiv:2611.24625](https://arxiv.org/abs/2611.24625) (LVK priors)
- $V_{ud}$: [arXiv:2611.18830](https://arxiv.org/abs/2611.18830), [arXiv:2611.18843](https://arxiv.org/abs/2611.18843), [arXiv:2611.24825](https://arxiv.org/abs/2611.24825)
- LHC statistics: [arXiv:2611.22092](https://arxiv.org/abs/2611.22092) (instanton excess), [arXiv:2611.24065](https://arxiv.org/abs/2611.24065) (limit coverage), [arXiv:2611.24270](https://arxiv.org/abs/2611.24270) (OmniFold)
- Superradiance: [arXiv:2611.18833](https://arxiv.org/abs/2611.18833), [arXiv:2611.23384](https://arxiv.org/abs/2611.23384)
- Chiral lattice: [arXiv:2611.16544](https://arxiv.org/abs/2611.16544), [arXiv:2611.20084](https://arxiv.org/abs/2611.20084)
- $B\to\gamma\ell\nu$: [arXiv:2611.18202](https://arxiv.org/abs/2611.18202), [arXiv:2611.18206](https://arxiv.org/abs/2611.18206), [arXiv:2611.18204](https://arxiv.org/abs/2611.18204)
