# The Cross Section: rolling synthesis, week ending 2026-11-23

This week the field kept auditing its own error bars, and the audits mostly made things worse. Phase-transition gravitational-wave forecasts lost robustness at every stage, from the data-side priors to the effective potential. Three independent mechanisms shrank axion superradiance clouds. A survey of LHC exclusion plots raised doubts about how ATLAS computes expected limits, landing the day after ATLAS posted a 3.5σ instanton-like excess. Default reference numbers were replaced: Higgs cross sections moved to Report 5 and the CKM angle γ was tightened. The week ended with a structural result on the $t\bar t$ threshold excess: toponium and a pseudoscalar must interfere, so fits that add them separately are wrong by construction. AI agents also crossed from reproducing known results to producing new, verifiable ones.

## Running themes

**GW phase-transition forecasts: heating up, and the weak link keeps moving.**
- **11-17, rate looks robust.** The nucleation rate held up: the lattice result is ~8% from one loop ([arXiv:2611.18794](https://arxiv.org/abs/2611.18794)), and EFT corrections to the bounce are modest ([arXiv:2611.20938](https://arxiv.org/abs/2611.20938)). Blame shifted to wall hydrodynamics.
- **11-19, data side is fragile.** Using a realistic SMBHB population drops the PTA phase-transition preference from 2.8σ to 1.5σ ([arXiv:2611.23371](https://arxiv.org/abs/2611.23371)). LVK constraints turn out to be prior-dominated ([arXiv:2611.24625](https://arxiv.org/abs/2611.24625)).
- **11-20, potential itself in question.** Thermal-resummation prescriptions differ by up to nine orders of magnitude in GW peak amplitude ([arXiv:2611.26417](https://arxiv.org/abs/2611.26417)). An improved partial-dressing scheme followed ([arXiv:2611.26303](https://arxiv.org/abs/2611.26303)).

**Superradiance clouds: converging, three hits in four days.**
- **11-17:** a gravitational Auger effect ([arXiv:2611.18833](https://arxiv.org/abs/2611.18833)).
- **11-19:** self-interaction feeding of the ground state caps the 211 cloud, with the cap scaling as $f_a^2$ ([arXiv:2611.23384](https://arxiv.org/abs/2611.23384)).
- **11-20:** self-gravity depletes clouds by orders of magnitude ([arXiv:2611.26541](https://arxiv.org/abs/2611.26541)).
- **Consensus:** free-field cloud models are never realized, so black-hole spin bounds on axions need revising. Binary environments are a new wrinkle that can partly offset the depletion.

**Statistical self-audit: steady.**
- **Fit artifacts:** adaptive-integrator normalization jumps produce artificially low NLLs ([arXiv:2611.19355](https://arxiv.org/abs/2611.19355)).
- **HERA:** treating HERA systematics as uncertain absorbs much of the data–theory tension ([arXiv:2611.22891](https://arxiv.org/abs/2611.22891)).
- **ATLAS coverage:** ATLAS puts 99.2% of observed limits inside its 2σ bands, while CMS matches nominal coverage ([arXiv:2611.24065](https://arxiv.org/abs/2611.24065)). A leading explanation is expected limits computed after a fit to data.
- **Limits that did tighten:** an ALP window near the $\pi^0$ was closed ([arXiv:2611.21728](https://arxiv.org/abs/2611.21728)), and SN 1987A gives $\mu_{\nu_e}\lesssim4.8\times10^{-13}\mu_B$ ([arXiv:2611.21729](https://arxiv.org/abs/2611.21729)).

**Thermal inelastic-DM models for the LZ signal: steady, but sloppy.** The models keep coming:
- composite-Higgs resonances ([arXiv:2611.21737](https://arxiv.org/abs/2611.21737)), the only one this week to check solar capture, the sideband and gamma rays together;
- a radion portal ([arXiv:2611.22890](https://arxiv.org/abs/2611.22890)), which checks solar neutrinos only by proxy;
- two near-identical photon-mediated templates ([arXiv:2611.25931](https://arxiv.org/abs/2611.25931), [arXiv:2611.26274](https://arxiv.org/abs/2611.26274)) that skip solar capture entirely.

**AI agents: heating up.**
- **11-18, reproduction:** a Codex reproduction of CMS $J/\psi$ cross sections had a 21% RMS spread ([arXiv:2611.22723](https://arxiv.org/abs/2611.22723)).
- **11-19, the standard:** Alimena argued competence should be judged by the evidence behind a result ([arXiv:2611.23330](https://arxiv.org/abs/2611.23330)).
- **11-23, new results:** an agent produced new Feynman-integral bases, chosen because the output is checkable ([arXiv:2611.26688](https://arxiv.org/abs/2611.26688)). Interpretability work also repaired an infrared-safety failure in a jet foundation model ([arXiv:2611.27079](https://arxiv.org/abs/2611.27079)).

## Turning points

- **Toponium vs. CP-odd $A$ (11-23).** Both sit in the same ${}^1S_0$ colour-singlet channel, so they must interfere. Unitarity then fixes the line shape through one complex ratio $\kappa$, with an exact amplitude zero above $M_A$. Additive fits are invalid ([arXiv:2611.27704](https://arxiv.org/abs/2611.27704)). A same-day general argument relates such amplitude zeros to UV structure ([arXiv:2611.27681](https://arxiv.org/abs/2611.27681)). Context: measured threshold cross sections span 3–13 pb ([arXiv:2611.22421](https://arxiv.org/abs/2611.22421)).
- **YR4 retired.** LHCHWG Report 5 is the new Higgs cross-section citation ([arXiv:2611.26281](https://arxiv.org/abs/2611.26281)). PDFs are now the leading uncertainty for the best-predicted modes, and the gluon-fusion N³LO-PDF mismatch uncertainty is doubled relative to YR4.
- **γ = 63.2°⁺²·³₋₂.₂.** This comes from LHCb's new combination, which also gives the most precise charm-mixing parameters to date ([arXiv:2611.26449](https://arxiv.org/abs/2611.26449)).
- **$V_{ud}$ floor identified.** The first EFT evaluation of $\bar\delta_{\rm NS}$ across 12 transitions finds that short-distance contact terms leave $\delta V_{ud}\simeq6\times10^{-4}$ ([arXiv:2611.18830](https://arxiv.org/abs/2611.18830), [arXiv:2611.18843](https://arxiv.org/abs/2611.18843)). A QMC follow-up shows three-body $\mathcal{O}(\alpha^2)$ terms move $V_{ud}$ at the 10⁻⁴ level ([arXiv:2611.24825](https://arxiv.org/abs/2611.24825)).

## Open questions

- **ATLAS instanton excess** ([arXiv:2611.22092](https://arxiv.org/abs/2611.22092)): is the 3.5σ local? How robust is the minimum-bias background? It joins the 13.6 GeV diphoton and 146 GeV $e\mu$ excesses on the unclosed list.
- **ATLAS expected limits:** watch for disclosure of the expected-limit method.
- **Keshet's WIMP line triads** ([arXiv:2611.21595](https://arxiv.org/abs/2611.21595)): only 2.8σ trial-corrected in the blind scan. The 6.1σ requires combining with the author's earlier samples.
- **$V_{ud}$:**
  - no first-row unitarity verdict in either abstract;
  - the ¹⁰C transition, where coupled-cluster came in 30% below QMC, is still unresolved.
- **PTA phase-transition preference:** rises back above 3σ if SMBHB merger times exceed ~6.5 Gyr.
- **Heavy-hadron tensions:**
  - **$D_{s1}(2460)$ radiative ratio:** Belle measures 0.74±0.08 ([arXiv:2611.20531](https://arxiv.org/abs/2611.20531)); theory predicts 0.57 ([arXiv:2611.27363](https://arxiv.org/abs/2611.27363)).
  - **KPW rule:** fails at 6.3σ in $\Xi_c^0\to pK^-$, and eight $\Lambda_c$ modes would decide whether it survives ([arXiv:2611.27716](https://arxiv.org/abs/2611.27716)).
  - **$K_1^*(1870)$:** the $3S$–$2D$ interpretation predicts a subordinate $K\eta'$ mode, awkward given that is the discovery channel ([arXiv:2611.19498](https://arxiv.org/abs/2611.19498)).
  - **X(2370):** interference among known pseudoscalars removes the need for X(2800) and undercuts the glueball reading ([arXiv:2611.24372](https://arxiv.org/abs/2611.24372)).
- **LZ models:** watch for any that confront solar capture.
- **Charm CPV:** the γ combination ([arXiv:2611.26449](https://arxiv.org/abs/2611.26449)) includes $A_{CP}(KK)$ and $A_{CP}(\pi\pi)$, but the abstract gives no values.
- **Radiative-return generators:** the new YFS+NLO generator agrees with BabaYaga at the per-mille level but differs from KKMC by up to 2%, which matters for HVP ([arXiv:2611.27883](https://arxiv.org/abs/2611.27883)).
- **Mass ordering:**
  - the precision-weighted intercept formalism ([arXiv:2611.21252](https://arxiv.org/abs/2611.21252)) generalizes Machado's 11-11 balance-of-pulls finding;
  - matter effects make the usual no-T-violation test in $\nu_\mu$ disappearance an identity ([arXiv:2611.27985](https://arxiv.org/abs/2611.27985));
  - SBND νe-on-argon data prefer lower-cross-section generators ([arXiv:2611.25098](https://arxiv.org/abs/2611.25098)).

## Recurring references

- **GW forecasts:** [arXiv:2611.18794](https://arxiv.org/abs/2611.18794), [arXiv:2611.23371](https://arxiv.org/abs/2611.23371), [arXiv:2611.26417](https://arxiv.org/abs/2611.26417)
- **Superradiance:** [arXiv:2611.18833](https://arxiv.org/abs/2611.18833), [arXiv:2611.23384](https://arxiv.org/abs/2611.23384), [arXiv:2611.26541](https://arxiv.org/abs/2611.26541)
- **$V_{ud}$:** [arXiv:2611.18843](https://arxiv.org/abs/2611.18843), [arXiv:2611.24825](https://arxiv.org/abs/2611.24825)
- **LHC statistics and excesses:** [arXiv:2611.24065](https://arxiv.org/abs/2611.24065), [arXiv:2611.22092](https://arxiv.org/abs/2611.22092)
- **Top threshold:** [arXiv:2611.27704](https://arxiv.org/abs/2611.27704)
- **New standard references:** [arXiv:2611.26281](https://arxiv.org/abs/2611.26281), [arXiv:2611.26449](https://arxiv.org/abs/2611.26449)
- **LZ models:** [arXiv:2611.21737](https://arxiv.org/abs/2611.21737)
- **Triple-exchange bispectra (two in one week):** [arXiv:2611.20356](https://arxiv.org/abs/2611.20356), [arXiv:2611.27611](https://arxiv.org/abs/2611.27611)
