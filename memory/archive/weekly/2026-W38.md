# The Cross Section — Rolling Synthesis, week ending 2026-09-18

The week that began still orbiting a single LZ xenon recoil ended firmly in precision QCD. The month-long dark-matter spectacle completed its full arc — from global fits, to falsifiability tests, to cosmological escape routes — and by week's end had thinned to a trickle, its front-page grip broken. In its place a dense nucleon-structure and fixed-order QCD program became the field's center of gravity, anchored by a four-loop landmark and a GPD revival. Running underneath: the season's autodiff/ML wave matured from detector plumbing into the statistics layer, hadron spectroscopy converged on several states from independent directions, and a sharp cosmic-muon result put the 17 MeV Atomki boson back on the defensive.

## Running themes

**The LZ higgsino/inelastic-DM saga — fading, arc complete.** The dominant multi-week thread ran its full course this week. It moved from Athron et al.'s collider counterweight ([arXiv:2609.12914](https://arxiv.org/abs/2609.12914)), to Ghosh et al. closing the astrophysical escape hatch ([arXiv:2609.15321](https://arxiv.org/abs/2609.15321)), to a falsifiability pivot (discriminators over models), and finally to purely cosmological survival strategies — early-universe conversion fixing endo/exo (An et al. [arXiv:2609.17412](https://arxiv.org/abs/2609.17412)) and asymmetric DM removing the IceCube bound by construction (Nagata et al. [arXiv:2609.18564](https://arxiv.org/abs/2609.18564)). By 09-18 it was a single follow-up. Watch for whether it revives on an experimental result or stays dormant.

**Precision QCD & nucleon structure — heating, now the center.** Emerged mid-week and dominated the back half. Gehrmann et al.'s complete four-loop non-singlet splitting functions ([arXiv:2609.17267](https://arxiv.org/abs/2609.17267)) anchored a broad DIS/structure program, followed by Guo et al.'s first GPD review in two decades ([arXiv:2609.19544](https://arxiv.org/abs/2609.19544)) and Su et al. extending lattice GPD computability into the $x\sim\pm\xi$ region ([arXiv:2609.20545](https://arxiv.org/abs/2609.20545)). Much of it is EIC/FCC-facing. This thread shows no sign of cooling.

**Statistical & ML tooling — steady, maturing upward.** The autodiff wave colonized successive layers: plumbing (FPGA trigger distillation, calibration) → reconstruction (VyPER, PSICHE, self-supervised pretraining) → the inference layer itself, surfacing as RooFit-AD, JAX interop, and HS3 in the IRIS-HEP blueprint ([arXiv:2609.19992](https://arxiv.org/abs/2609.19992)). Dorigo's demonstration that a covariance matrix can flip likelihood-ratio *ordering* ([arXiv:2609.20007](https://arxiv.org/abs/2609.20007)) was the conceptual standout.

**Hadron spectroscopy — converging.** Independent methods triangulating single states: f0(980) read as scale-dependent ($s\bar s$ at high energy, molecular at low) from BESIII $D_s\to f_0$, fragmentation (Kumano), and flow response (Lacey). BESIII's double-$s\bar s$ production ([arXiv:2609.20154](https://arxiv.org/abs/2609.20154)) echoed the double-charm puzzle; molecular readings of pentaquarks/exotics recurred.

**Precision flavor — steady, consolidating nulls.** BESIII and LHCb kept delivering firsts (LFU intact in $D_s\to f_0\mu\nu$; $\Xi_b^0\to\Xi^0 J/\psi$). The $C_9$ anomaly stayed alive via $Z'$ fits ([arXiv:2609.15026](https://arxiv.org/abs/2609.15026)); charm CPV narrowed toward experiment ([arXiv:2609.16219](https://arxiv.org/abs/2609.16219)).

## Turning points

- **[arXiv:2609.15321](https://arxiv.org/abs/2609.15321)** (Ghosh et al.) closed the halo-modeling escape for the thermal higgsino, forcing the whole DM conversation into either target-based tests or cosmological model-building.
- **[arXiv:2609.17267](https://arxiv.org/abs/2609.17267)** (Gehrmann et al.) — four-loop non-singlet splitting functions completed; a durable reference that helped shift the week's weight into QCD.
- **[arXiv:2609.18383](https://arxiv.org/abs/2609.18383)** (Benmansour et al.) — Geant4 shows cosmic muons reproduce the Atomki opening-angle peaks (cosmic-to-signal ratio above unity), reopening the 17 MeV boson question and shifting the burden to beam-off studies.
- **[arXiv:2609.19948](https://arxiv.org/abs/2609.19948)** (ATLAS) — direct, coupling-independent $\Gamma_H<307$ MeV from on-shell $H\to\gamma\gamma$ interference, a complementary handle to the off-shell width method.

## Open questions

- **17 MeV boson**: does the beam-off dataset survive the cosmic-muon background reinterpretation? ([arXiv:2609.18383](https://arxiv.org/abs/2609.18383))
- **Endo vs exo LZ direction**: now theoretically argued to be dynamically selected ([arXiv:2609.17412](https://arxiv.org/abs/2609.17412)), but the clean experimental test — argon's 336 keV line at DEAP-3600 ([arXiv:2609.15782](https://arxiv.org/abs/2609.15782)) — remains unreported. Watch for a result.
- **Strangeness asymmetry / dimuon-vs-LHC tension**: W+charm favors zero asymmetry ([arXiv:2609.12800](https://arxiv.org/abs/2609.12800)); NNLO dimuon suppression may ease it ([arXiv:2609.17120](https://arxiv.org/abs/2609.17120)). Unresolved.
- **$C_9$ and charm CPV**: both threads still live and narrowing ([arXiv:2609.15026](https://arxiv.org/abs/2609.15026), [arXiv:2609.16219](https://arxiv.org/abs/2609.16219)).
- **Cosmological-tension dark sectors**: dark-QCD Hubble fits ([arXiv:2609.16120](https://arxiv.org/abs/2609.16120)) and DESI equivalence-principle violation both land at residual ~3σ — speculative, watch for pushback.

## Recurring references

- [arXiv:2609.12914](https://arxiv.org/abs/2609.12914) — Athron et al., Run 2 electroweakino global fit (collider anchor for the DM thread)
- [arXiv:2609.15321](https://arxiv.org/abs/2609.15321) — Ghosh et al., solar-capture closure of the higgsino
- [arXiv:2609.15782](https://arxiv.org/abs/2609.15782) — Baer et al., argon as the clean endo/exo test (pending)
- [arXiv:2609.17412](https://arxiv.org/abs/2609.17412) — An et al., cosmological selection of endo/exo
- [arXiv:2609.16529](https://arxiv.org/abs/2609.16529) — Ge et al., relativistic inelastic Xe response functions (cited across three days)
- [arXiv:2609.17267](https://arxiv.org/abs/2609.17267) — Gehrmann et al., four-loop splitting functions
- [arXiv:2609.19544](https://arxiv.org/abs/2609.19544) — Guo et al., GPD review
- [arXiv:2609.20545](https://arxiv.org/abs/2609.20545) — Su et al., lattice GPDs near $x=\pm\xi$
- [arXiv:2609.19992](https://arxiv.org/abs/2609.19992) — IRIS-HEP statistical blueprint
- [arXiv:2609.18383](https://arxiv.org/abs/2609.18383) — Benmansour et al., Atomki cosmic-muon reinterpretation
