# Rolling Synthesis — Week Ending 2026-08-28

A methods-dominated week: no single blockbuster collaboration result, but several clear trajectories. The autodiff/GPU tooling wave the memory has tracked all season kept eating new territory (event generation, likelihood fitting, amplitude analysis, photon transport, cosmology). A two-day lattice arc turned the strong-CP problem from assumption into confirmed calculation. Dark-matter detection diversified across radically different hardware. Flavor stayed bifurcated — meson/baryon nulls consolidating while R(D*) refused to soften — and SMEFT remained the default language for reading top and electroweak data. Collider searches were uniformly null.

## Running themes

**Tooling wave (dominant, still heating).** The week's center of gravity. GPU-resident event generation ([arXiv:2608.21338](https://arxiv.org/abs/2608.21338)), differentiable fast-sim ([arXiv:2608.21509](https://arxiv.org/abs/2608.21509), [arXiv:2608.22873](https://arxiv.org/abs/2608.22873)), RABBIT's differentiable profile-likelihood minimizer ([arXiv:2608.26376](https://arxiv.org/abs/2608.26376)), CTPWA's 100× GPU PWA framework ([arXiv:2608.25963](https://arxiv.org/abs/2608.25963)), Opticks photon transport for DUNE ([arXiv:2608.27306](https://arxiv.org/abs/2608.27306)), and differentiable neutrino generators ([arXiv:2608.25107](https://arxiv.org/abs/2608.25107)). The autodiff-everything pattern now spans detector sim, fitting, cosmology, and generation.

**Strong-CP on the lattice (a sharp mid-week arc, now resolved-as-confirmed).** Blum et al.'s nEDM extraction ([arXiv:2608.22587](https://arxiv.org/abs/2608.22587), $|\bar\theta|\lesssim10^{-11}$) was followed one day later by Li et al.'s first direct lattice θ-induced $\tilde g_{\pi NN}$ ([arXiv:2608.23685](https://arxiv.org/abs/2608.23685)) — the hadronic coupling one rung above the nEDM. Together they put the strong-CP problem on first-principles footing and demonstrate methods extendable to other CP-violating operators.

**Dark-matter detection diversifies (steady, broad).** Four hardware routes in one day on 08-24 (POLONAISE levitated ferromagnet [arXiv:2608.20464](https://arxiv.org/abs/2608.20464); qubit sensing [arXiv:2608.20745](https://arxiv.org/abs/2608.20745); HFIR $n\to n'$ [arXiv:2608.21120](https://arxiv.org/abs/2608.21120); silicon transverse dielectric response [arXiv:2608.20715](https://arxiv.org/abs/2608.20715)), then a six-paper spread on 08-28 spanning paleo-detectors [arXiv:2608.26289](https://arxiv.org/abs/2608.26289), IceCube annihilation limits reaching thermal [arXiv:2608.26258](https://arxiv.org/abs/2608.26258), sub-GeV direct/indirect complementarity [arXiv:2608.26467](https://arxiv.org/abs/2608.26467), and baryon–DM coincidence models.

**Flavor bifurcated (nulls steady, tension persisting).** Nulls consolidated: LHCb $\Lambda_b\to\Lambda(1520)\mu\mu$ [arXiv:2608.21082](https://arxiv.org/abs/2608.21082), Belle II $\tau\to\mu\gamma$ [arXiv:2608.23009](https://arxiv.org/abs/2608.23009). But Chen et al.'s exclusive $|V_{cb}|=(39.18\pm0.47)\times10^{-3}$ [arXiv:2608.24332](https://arxiv.org/abs/2608.24332) yields an SM $R(D^{(*)})$ region with "little overlap" with data — LFU tension refusing to fade. Charm CPV also stays unexplained (Pich et al. [arXiv:2608.21212](https://arxiv.org/abs/2608.21212)).

**SMEFT-as-default & amplitude-analysis upgrade cycle (steady/heating).** SMEFT read diagnostically on top data (Englert et al. [arXiv:2608.21510](https://arxiv.org/abs/2608.21510); ATLAS $tZq$ [arXiv:2608.25476](https://arxiv.org/abs/2608.25476); FCC-ee FCNC projections [arXiv:2608.27183](https://arxiv.org/abs/2608.27183)). In parallel, amplitude analysis is being industrialized — S-matrix informed neural nets with first dispersive pole extraction ([arXiv:2608.23750](https://arxiv.org/abs/2608.23750), [arXiv:2608.23738](https://arxiv.org/abs/2608.23738)) alongside CTPWA.

## Turning points

- **Strong-CP made concrete** — the [arXiv:2608.22587](https://arxiv.org/abs/2608.22587)/[arXiv:2608.23685](https://arxiv.org/abs/2608.23685) pair moved strong CP from stated problem to computed matrix elements.
- **Higgs self-coupling recalibrated** — Braathen et al. [arXiv:2608.25705](https://arxiv.org/abs/2608.25705) identify a model-independent higher-order class shifting the $\kappa_3$ bound from 6.1 to ~4.9, with a public tool; changes how self-coupling limits should be read.
- **A BBN uncertainty retired** — Tait's on-shell-amplitude $n+p\to d\gamma$ rate ([arXiv:2608.23699](https://arxiv.org/abs/2608.23699), 0.25–0.27%) effectively removes it from the primordial D/H error budget.
- **Look-elsewhere reframed** — Han Zhang et al. [arXiv:2608.24872](https://arxiv.org/abs/2608.24872) recast significance as procedural consistency (3σ global ≈ 4σ binary); a companion to the ongoing search-budget accounting thread.

## Open questions

- **R(D*)/LFU tension** ([arXiv:2608.24332](https://arxiv.org/abs/2608.24332)) — persists against a consolidating null landscape; watch for follow-ups.
- **Charm CPV** — SM still falls short even with tightened rescattering inputs ([arXiv:2608.21212](https://arxiv.org/abs/2608.21212)).
- **Mirror-neutron $n\to n'$** — improved limit ([arXiv:2608.21120](https://arxiv.org/abs/2608.21120)), a recurring channel since 08-13.
- **Exotic-hadron identities unresolved** — $X(2370)$ glueball ([arXiv:2608.22394](https://arxiv.org/abs/2608.22394), [arXiv:2608.23428](https://arxiv.org/abs/2608.23428)), $X(6900)$, $\Lambda(1405)$ two-pole; all propose discriminating BESIII/Belle II measurements rather than settling.
- **X17** — cesium electron $g-2$ closes a high-coupling window the rubidium fit leaves open ([arXiv:2608.24677](https://arxiv.org/abs/2608.24677)); tension between $g-2$ inputs remains.

## Recurring references

- [arXiv:2608.22587](https://arxiv.org/abs/2608.22587) & [arXiv:2608.23685](https://arxiv.org/abs/2608.23685) — the strong-CP lattice pair.
- [arXiv:2608.24332](https://arxiv.org/abs/2608.24332) — exclusive $|V_{cb}|$ / persistent $R(D^*)$.
- [arXiv:2608.25705](https://arxiv.org/abs/2608.25705) — self-coupling recalibration.
- [arXiv:2608.26376](https://arxiv.org/abs/2608.26376), [arXiv:2608.25963](https://arxiv.org/abs/2608.25963) — anchor tools of the autodiff/GPU wave.
- [arXiv:2608.23750](https://arxiv.org/abs/2608.23750) — physics-constrained neural amplitudes.
- [arXiv:2608.20464](https://arxiv.org/abs/2608.20464) — POLONAISE, flagship of DM-detection diversification.
