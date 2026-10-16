# The Cross Section — Weekly Synthesis, week ending 2026-10-16

*Sources: daily digests for 10-12, 10-14, 10-15 and 10-16.*

The week's dominant mood was **anomalies meeting their inputs**. Several long-running puzzles moved toward the SM or toward conventional explanations:

- IceCube found no decoherence.
- The gallium anomaly dissolved against solar calibration.
- The di-$J/\psi$ spectrum was fit with no exotics.
- A global PDF fit shrank the $t\bar t$ threshold excess to about 2σ.

Flavor went the other way. $R(D^{(*)})$, $C_9$ and now SU(3)$_F$ breaking in $B\to DP$ all held or sharpened. LZ 248 keV model-building peaked at five papers on 10-14. Its argument then migrated from the solar-neutrino bound to the dark-matter halo tail. Precision theory kept showing that the next order mainly reveals the true error budget. ML tools crossed from demos into defaults.

## Running themes

**1. LZ event model-building: steady volume, argument shifting.**
- Paper counts were 1, 5, 1 and 1 on the four days.
- The solar-neutrino capture bound went from something models ignored, to a design constraint (Lee et al. [arXiv:2610.13930](https://arxiv.org/abs/2610.13930), Dirac bino), to a proposed test (Di Mauro [arXiv:2610.14188](https://arxiv.org/abs/2610.14188), $U(1)_B$ plus an IceCube solar-capture analysis).
- Graham et al. [arXiv:2610.21041](https://arxiv.org/abs/2610.21041) then showed that the thermal Higgsino survives only with a non-standard high-velocity halo tail. That moves the fight to halo simulations, echoing the 10-06 halo-marginalization point.
- Holdouts that ignore solar capture persist ([arXiv:2610.15557](https://arxiv.org/abs/2610.15557), [arXiv:2610.18234](https://arxiv.org/abs/2610.18234)).

**2. Flavor tensions: heating.**
- **$R(D^{(*)})$.** The world-average tension survives September's "easing." Warburton [arXiv:2610.16617](https://arxiv.org/abs/2610.16617) finds new Belle/Belle II results individually SM-consistent, and Hu et al. [arXiv:2610.17289](https://arxiv.org/abs/2610.17289) put $R(D^*)$ 2.8σ from experiment.
- **$C_9$.** LHCb proceedings ([arXiv:2610.13165](https://arxiv.org/abs/2610.13165)) say the $K^{*0}\mu\mu$ tensions persist. The new differential $B^0\to K^+\pi^-\mu\mu$ measurement ([arXiv:2610.14156](https://arxiv.org/abs/2610.14156)) gives fresh input.
- **SU(3)$_F$.** The biggest jump of the week (see Turning points).
- **$|V_{cb}|$.** Marzocca [arXiv:2610.18961](https://arxiv.org/abs/2610.18961) offers a route with orthogonal systematics via $b$-tagged DIS, projecting ~0.8% at LHeC.

**3. Perturbation at its edges: steady.**
- Kärkkäinen et al. [arXiv:2610.13873](https://arxiv.org/abs/2610.13873) computed the N³LO pressure of cold QED, closing a 49-year-old open order. Their Bayesian missing-order estimate exceeds scale variation, repeating the prior week's jet-veto N³LL warning.
- Philcox's two-loop LSS ([arXiv:2610.13867](https://arxiv.org/abs/2610.13867)) gains reach in $k$ but not in $\sigma_8$.
- Gehrmann et al. [arXiv:2610.20820](https://arxiv.org/abs/2610.20820) supply the three-loop masters needed for N³LO $V$/$H$+jet.
- The emerging consensus: scale bands understate uncertainty.

**4. Thresholds versus exotics: heating.**
- BESIII sees a >10σ $\pi^0\pi^0$ threshold structure ($M=274.3$, $\Gamma=17.1$ MeV) that ChPT cannot reproduce ([arXiv:2610.13097](https://arxiv.org/abs/2610.13097)).
- Swanson [arXiv:2610.15248](https://arxiv.org/abs/2610.15248) fits di-$J/\psi$ with rescattering alone (χ²/ndf = 56/50). That challenges the prior week's bound $cc\bar c\bar c$ claim.
- Zhang et al. [arXiv:2610.19066](https://arxiv.org/abs/2610.19066) read the 10.513 GeV state as a molecular $X_b$.
- The same "threshold dynamics first" logic reached $t\bar t$ (see Turning points).

**5. ML/tools into production: steady.**
- MadNIS ([arXiv:2610.17177](https://arxiv.org/abs/2610.17177)) became MadGraph's LO default.
- Agent benchmarks matured: HEPTABench [arXiv:2610.18454](https://arxiv.org/abs/2610.18454) and SIDERIUS [arXiv:2610.14024](https://arxiv.org/abs/2610.14024).
- Physics-facing ML appeared across the chain: tokenizers [arXiv:2610.13876](https://arxiv.org/abs/2610.13876), CMS data-driven fake taus [arXiv:2610.13634](https://arxiv.org/abs/2610.13634), and a Particle Transformer in BESIII's $D^0\to\gamma\omega$ observation [arXiv:2610.21982](https://arxiv.org/abs/2610.21982).

## Turning points

- **IceCube decoherence null** ([arXiv:2610.14144](https://arxiv.org/abs/2610.14144)). It excludes natural Planck-suppressed decoherence for $0\le n\le3$, the first such exclusion at $n=3$. A class of quantum-gravity phenomenology is closed at its natural scale.
- **Gallium anomaly gone** ([arXiv:2610.22219](https://arxiv.org/abs/2610.22219)). The solar-source calibration gives 66.1±3.1 SNU against 67.5 expected. This removes a sterile-neutrino argument.
- **$t\bar t$ threshold deflated** (Ball et al. [arXiv:2610.21479](https://arxiv.org/abs/2610.21479)). The fit finds nothing at 8 TeV and about 2σ at 13 TeV, versus CMS's 6.1σ, with a strong $\Delta$–$m_t$ correlation. Threshold claims must now be quoted jointly with $m_t$.
- **SU(3)$_F$ breaking at ~60%** (Bhattacharya et al. [arXiv:2610.20611](https://arxiv.org/abs/2610.20611)). The $B\to DP$ discrepancy stays above 5σ once CP observables enter. It pairs with August's $B\to PP$ puzzle.
- **Lattice HVP consolidates** (ETMC [arXiv:2610.22224](https://arxiv.org/abs/2610.22224)). The ~1% result of 714.9(8.1) agrees with other lattice groups. A sum-rule cross-check ([arXiv:2610.20945](https://arxiv.org/abs/2610.20945)) lands on the lattice side as well.

## Open questions

- **LZ halo tail.** Will halo simulations support the high-velocity tail Graham et al. need? Watch also for the first dedicated IceCube solar-capture analysis.
- **$t\bar t$ threshold.** Is the residual excess toponium, a CP-odd scalar, or an $m_t$ artifact? Watch for experimental fits that include $m_t$ freedom.
- **SU(3)$_F$ breaking.** Is 60% breaking a failure of the amplitude parametrization or of the symmetry expansion itself?
- **$R(D^{(*)})$ and $C_9$.** Both remain open going into the next Belle II and LHCb updates.
- **The 274 MeV $\pi^0\pi^0$ structure.** The 10-12 digest expected theory papers interpreting it; none appeared in this week's later digests.
- **Di-$J/\psi$.** Can any tetraquark interpretation beat Swanson's no-exotics fit?
- **$\sigma_{\pi N}$.** Watch for the excited-state-suppressed value from [arXiv:2610.20362](https://arxiv.org/abs/2610.20362), which feeds the hedge in Bao et al.'s prior-week result.
- **NOvA–T2K NSI.** Xenon-detector solar-neutrino data already constrain part of the complex-NSI explanation ([arXiv:2610.18971](https://arxiv.org/abs/2610.18971)).

## Recurring references

These are the thread anchors future digests should link back to:

- **LZ:** [arXiv:2610.13930](https://arxiv.org/abs/2610.13930), [arXiv:2610.14188](https://arxiv.org/abs/2610.14188), [arXiv:2610.21041](https://arxiv.org/abs/2610.21041)
- **Flavor:** [arXiv:2610.20611](https://arxiv.org/abs/2610.20611), [arXiv:2610.16617](https://arxiv.org/abs/2610.16617), [arXiv:2610.17289](https://arxiv.org/abs/2610.17289), [arXiv:2610.13165](https://arxiv.org/abs/2610.13165), [arXiv:2610.18961](https://arxiv.org/abs/2610.18961)
- **Precision orders:** [arXiv:2610.13873](https://arxiv.org/abs/2610.13873), [arXiv:2610.13867](https://arxiv.org/abs/2610.13867), [arXiv:2610.20820](https://arxiv.org/abs/2610.20820)
- **Thresholds and exotics:** [arXiv:2610.13097](https://arxiv.org/abs/2610.13097), [arXiv:2610.15248](https://arxiv.org/abs/2610.15248), [arXiv:2610.21479](https://arxiv.org/abs/2610.21479)
- **SM-side resolutions:** [arXiv:2610.14144](https://arxiv.org/abs/2610.14144), [arXiv:2610.22219](https://arxiv.org/abs/2610.22219), [arXiv:2610.22224](https://arxiv.org/abs/2610.22224)
- **Tools:** [arXiv:2610.17177](https://arxiv.org/abs/2610.17177), [arXiv:2610.18454](https://arxiv.org/abs/2610.18454)
