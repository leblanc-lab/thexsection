# Rolling synthesis — week ending 2026-08-27

The week's spine was infrastructure and precision, not discovery. One genuine turning point stands out — CMS's 6.1σ single-lepton confirmation of the $t\bar t$-threshold (toponium) excess — but most days ran method-heavy: a sustained ML/autodiff/GPU tooling wave now reaching event generation and amplitude analysis, a two-day strong-CP lattice arc, and the steady consolidation of the top sector into SMEFT language. Flavor mostly delivered nulls, with one stubborn exception: the $R(D^*)$/$|V_{cb}|$ tension refused to soften. Dark-matter detection hardware had a strong single day.

## Running themes

**ML/autodiff/GPU tooling (heating, dominant).** The clearest through-line of the week. GPU-resident event generation ([arXiv:2608.21338](https://arxiv.org/abs/2608.21338)), calibrated-uncertainty normalizing flows and differentiable Parnassus ([arXiv:2608.21509](https://arxiv.org/abs/2608.21509), [arXiv:2608.22873](https://arxiv.org/abs/2608.22873)), neural Boltzmann solvers reaching cosmology ([arXiv:2608.23022](https://arxiv.org/abs/2608.23022)), a differentiable neutrino generator ADoNIS ([arXiv:2608.25107](https://arxiv.org/abs/2608.25107)), and a large cut in QCD quantum-simulation cost ([arXiv:2608.21258](https://arxiv.org/abs/2608.21258)). By week's end this converged on **amplitude analysis specifically**: S-matrix-informed neural networks for $\pi\pi$ with dispersive pole extraction ([arXiv:2608.23750](https://arxiv.org/abs/2608.23750), [arXiv:2608.23738](https://arxiv.org/abs/2608.23738)) followed immediately by the GPU covariant-tensor PWA framework CTPWA ([arXiv:2608.25963](https://arxiv.org/abs/2608.25963)). The toolchain is in an active upgrade cycle.

**EFT-as-default in the top/EW sector (steady).** The default reading of collider data all week. First global top-FCNC fit over all 24 SMEFT operators ([arXiv:2608.19547](https://arxiv.org/abs/2608.19547)); Englert et al. using SMEFT diagnostically on single-top/$tH$ shifts, finding no minimal UV multiplet matches ([arXiv:2608.21510](https://arxiv.org/abs/2608.21510)); ATLAS $tZq$ folding differential spectra and a spin asymmetry into dim-6 limits ([arXiv:2608.25476](https://arxiv.org/abs/2608.25476)). Backed by tooling — universal two-loop four-fermion running ([arXiv:2608.19316](https://arxiv.org/abs/2608.19316)).

**Strong-CP on the lattice (arc completed, then fading).** A two-day set piece: Blum et al.'s nEDM extraction from topological-charge density confirming strong-CP is real ([arXiv:2608.22587](https://arxiv.org/abs/2608.22587)), followed one rung up by the first direct lattice θ-induced $\tilde g_{\pi NN}$ coupling ([arXiv:2608.23685](https://arxiv.org/abs/2608.23685)). Together they pin both the neutron EDM and its hadronic coupling from first principles.

**Flavor: nulls consolidating, one tension holding (steady).** LHCb's baryonic $\Lambda_b\to\Lambda(1520)\mu\mu$ angular analysis landed on the SM ([arXiv:2608.21082](https://arxiv.org/abs/2608.21082)); Belle II tightened $\tau\to\mu\gamma$ ([arXiv:2608.23009](https://arxiv.org/abs/2608.23009)). Against that quiet front, exclusive $|V_{cb}|=(39.18\pm0.47)\times10^{-3}$ with SM $R(D^{(*)})$ barely overlapping data kept the LFU tension alive ([arXiv:2608.24332](https://arxiv.org/abs/2608.24332)).

**Dark-matter detection hardware (spiked 08-24, then quiet).** Four hardware routes in one day: POLONAISE's levitated-ferromagnet ultraheavy search ([arXiv:2608.20464](https://arxiv.org/abs/2608.20464)), HFIR cold-neutron $n\to n'$ ([arXiv:2608.21120](https://arxiv.org/abs/2608.21120)), qubit-sensing review ([arXiv:2608.20745](https://arxiv.org/abs/2608.20745)), plus the silicon transverse-dielectric calculation justifying the standard light-DM approximation ([arXiv:2608.20715](https://arxiv.org/abs/2608.20715)).

## Turning points

- **CMS single-lepton toponium confirmation ([arXiv:2608.19546](https://arxiv.org/abs/2608.19546))** — a statistically independent 6.1σ channel promotes the $t\bar t$-threshold excess from one-channel curiosity to a two-channel result; theory reads followed ([arXiv:2608.19651](https://arxiv.org/abs/2608.19651)).
- **Braathen et al. on Higgs self-coupling ([arXiv:2608.25705](https://arxiv.org/abs/2608.25705))** — a model-independent higher-order class shifts the $\kappa_3$ bound from 6.1 to ~4.9, a genuine correction to how self-coupling limits should be read, with a public tool.
- **Strong-CP confirmed on the lattice ([arXiv:2608.22587](https://arxiv.org/abs/2608.22587))** — moves the strong-CP problem from indirect to direct footing.
- **Charm CPV stays SM-unreachable ([arXiv:2608.21212](https://arxiv.org/abs/2608.21212))** — Pich et al. tighten the rescattering treatment and confirm the SM still falls short; the anomaly is unexplained, not resolved.

## Open questions

- **Toponium interpretation.** NRQCD pseudoscalar vs elementary 2HDM CP-odd Higgs ([arXiv:2608.19651](https://arxiv.org/abs/2608.19651)) — watch for more channels and any baryogenesis link.
- **$R(D^*)$/$|V_{cb}|$ ([arXiv:2608.24332](https://arxiv.org/abs/2608.24332)).** The month's outstanding flavor tension; follow updated form factors and Belle II statistics.
- **Charm CPV ([arXiv:2608.21212](https://arxiv.org/abs/2608.21212)).** Left unexplained.
- **Neutron $g_A$ radiative shift.** Tomalak et al.'s $\Delta(1232)$ contribution nulls the shift and restores power counting ([arXiv:2608.22845](https://arxiv.org/abs/2608.22845)), feeding the lattice-vs-experiment $g_A$ debate.
- **What a "5σ" buys.** A statistical-rigor thread — Reisch et al.'s search-budget accounting ([arXiv:2608.19764](https://arxiv.org/abs/2608.19764)) and the look-elsewhere reframing ([arXiv:2608.24872](https://arxiv.org/abs/2608.24872)) — worth tracking as it touches how future claims are read.

## Recurring references

- [arXiv:2608.19546](https://arxiv.org/abs/2608.19546) — CMS single-lepton toponium excess (6.1σ); the week's anchor result.
- [arXiv:2608.22587](https://arxiv.org/abs/2608.22587) — Blum et al. lattice nEDM; strong-CP confirmation.
- [arXiv:2608.23685](https://arxiv.org/abs/2608.23685) — first direct lattice $\tilde g_{\pi NN}$; hadronic coupling side.
- [arXiv:2608.24332](https://arxiv.org/abs/2608.24332) — exclusive $|V_{cb}|$; the persistent $R(D^*)$ tension.
- [arXiv:2608.23750](https://arxiv.org/abs/2608.23750) / [arXiv:2608.23738](https://arxiv.org/abs/2608.23738) — S-matrix-informed neural amplitudes; and [arXiv:2608.25963](https://arxiv.org/abs/2608.25963) (CTPWA) — the amplitude-analysis upgrade cycle.
- [arXiv:2608.25476](https://arxiv.org/abs/2608.25476) — ATLAS $tZq$; and [arXiv:2608.21510](https://arxiv.org/abs/2608.21510) (Englert SMEFT) — EFT-as-default anchors.
- [arXiv:2608.25705](https://arxiv.org/abs/2608.25705) — Braathen et al. self-coupling correction.
