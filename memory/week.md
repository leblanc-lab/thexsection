# Rolling synthesis — week ending 2026-07-27

This week the field split its attention between clean experimental firsts and a steady tightening of theory/method infrastructure. NA62's golden-mode kaon measurement opened the week and cast a shadow across it, spawning a KOTO II phenomenology sequel and a lattice benchmark by Friday. Cosmology's tension-solvers hit two new walls. The exotic-hadron drumbeat (Reggeon, hybrid, glueball) continued from multiple facilities, dark-matter detection kept diversifying into new thresholds and channels, and the automation thread graduated from LLM agents *checking* work to *orchestrating* whole pipelines. Two anomalies — the UHE-neutrino puzzle and the cosmic-ray muon puzzle — got sharpened into concrete numbers rather than resolved.

## Running themes

- **Rare kaons → LFU precision (heating).** NA62's $K^+\to\pi^+\nu\bar\nu$ at 20% precision ([arXiv:2607.16413](https://arxiv.org/abs/2607.16413)) anchored the week: Blanke et al. ([arXiv:2607.19055](https://arxiv.org/abs/2607.19055)) showed $K_L\to\pi^0\nu\bar\nu$ can still be enhanced 10× for KOTO II, and Boyle et al. ([arXiv:2607.22358](https://arxiv.org/abs/2607.22358)) delivered the first lattice QCD+QED $R_{e/\mu}$ radiative correction — the SM input NA62/PIONEER will quote.

- **Phase transitions, GW, and the resummation debate (steady/contested).** The July systematics drumbeat continued: daisy resummation was declared disfavored for supercooled transitions ([arXiv:2607.18233](https://arxiv.org/abs/2607.18233)), then Klose ([arXiv:2607.21252](https://arxiv.org/abs/2607.21252)) offered the constructive 2PI counterpart. Wall-velocity benchmarking ([arXiv:2607.18207](https://arxiv.org/abs/2607.18207)) and a lattice verdict against immediate post-transition matter domination ([arXiv:2607.19469](https://arxiv.org/abs/2607.19469)) fed the same message: GW spectra hinge on poorly controlled non-equilibrium inputs. Defect-network GW work ([arXiv:2607.21701](https://arxiv.org/abs/2607.21701), [arXiv:2607.22481](https://arxiv.org/abs/2607.22481)) rounds it out.

- **Exotic hadrons — hybrids, glueballs, spin-exotics (heating).** COMPASS/JPAC's first exotic Reggeon ([arXiv:2607.17850](https://arxiv.org/abs/2607.17850), tied to $\pi_1(1600)$) was extended to strangeness as a $K(1690)$ hybrid ([arXiv:2607.20825](https://arxiv.org/abs/2607.20825)); BESIII argued $X(2370)$ is the lightest $0^{-+}$ glueball ([arXiv:2607.20366](https://arxiv.org/abs/2607.20366)), building on the $N_f=1$ glueball–$s\bar s$ mixing result ([arXiv:2607.17294](https://arxiv.org/abs/2607.17294)). Heavy-flavor spectroscopy consolidated ($\Sigma_c$ assignments [arXiv:2607.17923](https://arxiv.org/abs/2607.17923); $T_{cc}^+$ lattice [arXiv:2607.19009](https://arxiv.org/abs/2607.19009)).

- **Dark-matter detection diversifying (steady).** New thresholds and channels: QUALIPHIDE's 13 meV MKID array ([arXiv:2607.19319](https://arxiv.org/abs/2607.19319)), RES-NOVA archaeological-lead bolometers repurposed from inelastic DM ([arXiv:2607.18378](https://arxiv.org/abs/2607.18378)) to solar axions ([arXiv:2607.21363](https://arxiv.org/abs/2607.21363)), and the Earth-transducer review ([arXiv:2607.16342](https://arxiv.org/abs/2607.16342)).

- **Agents at the console (heating).** Past LQCDMaster: Gu et al. treat amplitudes as self-evolving programs ([arXiv:2607.21629](https://arxiv.org/abs/2607.21629), 805× speed-up), and SMEFT-Pheno-Agent ([arXiv:2607.22331](https://arxiv.org/abs/2607.22331)) wraps the full MadGraph/Pythia/Delphes chain in a natural-language agent — reproducibility as the selling point. EFT recasts ([arXiv:2607.21711](https://arxiv.org/abs/2607.21711), [arXiv:2607.21712](https://arxiv.org/abs/2607.21712), [arXiv:2607.22390](https://arxiv.org/abs/2607.22390)) are now the default interpretation language.

## Turning points

- **Two new walls against the Hubble tension.** Poulin et al. ([arXiv:2607.20635](https://arxiv.org/abs/2607.20635)) find a BBN-deuterium discrepancy that *worsens* under EDE; Sabogal et al. ([arXiv:2607.21244](https://arxiv.org/abs/2607.21244)) cap late-time $E(z)$ fixes at ~2% against a required ~8%. The referees are now dismantling the "$H_0$ World Cup" winners.
- **The UHE-neutrino anomaly got a number.** Chattopadhyay et al. ([arXiv:2607.19487](https://arxiv.org/abs/2607.19487)) quantified the ANITA/KM3NeT/IceCube tension at 7.5σ (diffuse), 5.9σ (transients); Cheek et al. ([arXiv:2607.20608](https://arxiv.org/abs/2607.20608)) added an Earth-rotation timing test disfavoring ($p\simeq0.13$) a DM-decay origin for KM3-230213A.
- **BESIII polarimetry method.** Secondary-scattering polarimetry turned a general spectrometer into a large-acceptance polarimeter ([arXiv:2607.19927](https://arxiv.org/abs/2607.19927)/[arXiv:2607.19948](https://arxiv.org/abs/2607.19948)) — reusable across facilities.
- **LHCb 32 Tbps real-time processing** ([arXiv:2607.21492](https://arxiv.org/abs/2607.21492)) — a new throughput standard, the production endpoint of the month's real-time-reconstruction wave.
- **Collider polarization program advanced:** ATLAS longitudinal $Z$ in $WZjj$-EW at 4.0σ ([arXiv:2607.20246](https://arxiv.org/abs/2607.20246)), continuing the $ZZ$ milestone.

## Open questions

- **KOTO II room:** how large can $K_L\to\pi^0\nu\bar\nu$ actually go given SM-like $K^+$ and $\varepsilon_K$? ([arXiv:2607.19055](https://arxiv.org/abs/2607.19055))
- **UHE-neutrino origin:** what population survives the 7.5σ tension? Watch for follow-ups on transients and exotic sources.
- **Muon puzzle quantified:** Auger ([arXiv:2607.22323](https://arxiv.org/abs/2607.22323)) demands a 2.8–4.6× hadronic-energy-fraction amplification at $\sqrt{s}\simeq100$ TeV — a concrete target for interaction models.
- **Direct-detection blind spot:** NLO cancellations push Higgsino–nucleon scattering below the neutrino floor ([arXiv:2607.20588](https://arxiv.org/abs/2607.20588)).
- **Daisy resummation:** which scheme is trustworthy for very strong transitions — bridging [arXiv:2607.18233](https://arxiv.org/abs/2607.18233) and [arXiv:2607.21252](https://arxiv.org/abs/2607.21252).
- **X17 revisited:** E141 recast ([arXiv:2607.22102](https://arxiv.org/abs/2607.22102)) tightens tension with ATOMKI's preliminary lifetime.

## Recurring references

- **[arXiv:2607.16413](https://arxiv.org/abs/2607.16413)** — NA62 golden mode; the week's anchor (cited 21, 22, 27).
- **[arXiv:2607.17850](https://arxiv.org/abs/2607.17850)** — COMPASS/JPAC exotic Reggeon; extended by [arXiv:2607.20825](https://arxiv.org/abs/2607.20825).
- **[arXiv:2607.18378](https://arxiv.org/abs/2607.18378)** — RES-NOVA bolometers; repurposed in [arXiv:2607.21363](https://arxiv.org/abs/2607.21363).
- **[arXiv:2607.19487](https://arxiv.org/abs/2607.19487)** — UHE-neutrino tension fit; followed by [arXiv:2607.20608](https://arxiv.org/abs/2607.20608).
- **[arXiv:2607.18233](https://arxiv.org/abs/2607.18233)** ↔ **[arXiv:2607.21252](https://arxiv.org/abs/2607.21252)** — the daisy-resummation debate.
- **[arXiv:2607.20246](https://arxiv.org/abs/2607.20246)** — collider polarization program (sequel to prior-week $ZZ$).
- **[arXiv:2607.21492](https://arxiv.org/abs/2607.21492)** — LHCb real-time throughput benchmark.
