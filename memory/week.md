# The Cross Section: rolling synthesis, week ending 2026-11-17

This week had three main threads. The first was a self-audit of claimed limits and forecasts. Neutrino mass ordering was reframed as a bookkeeping problem limited by interaction modeling. First-order-transition GW forecasts were checked link by link, and the weakness turned out to sit in wall hydrodynamics rather than in nucleation rates. Dark-matter bounds were recomputed in both directions. The second thread was the loop-count frontier, which moved from QED and $V$+jet into electroweak observables and heavy-flavor SCET, ending in a three-group N³LO push on $B\to\gamma\ell\nu$. The third was the LZ 248 keV event, which got its first elastic interpretation, but solar capture remains the gate. Late in the week, $V_{ud}$ gained a nuclear-structure floor from contact terms.

## Running themes

- **Mass ordering as competing pulls (heating).** Machado et al. showed that the 1.9σ preference against inverted ordering comes from reactor+T2K and reactor+NOvA pulling in opposite directions (11-11). A 3.5% $\Delta m^2$ shift in one experiment would flip the preference, and JUNO alone tops out near 3σ. Cerrone et al. generalized this into a sum rule (11-17): each experiment reduces to a resolution-weighted intercept, and the method extends to atmospheric neutrinos in matter (DeepCore vs JUNO). The stated bottleneck is percent-level $\nu$–nucleus modeling. Ježo et al. (heavy-quark $F_4$/$F_5$, up to 40% $\nu_\tau$ suppression) and Fatima et al. ($\eta$ production) feed the generator-rebuilding thread that began 11-02.
- **GW forecasts vs transition dynamics (steady, now localized).**
  - On 11-13, Zhang et al. found supercooling completion criteria break homogeneity near their shared boundary, and Cassidy et al. found the Higgs trilinear is not robust to dimension-six operators.
  - On 11-16, Barni et al. showed $(\xi_w,\alpha_N)$ does not fix a unique flow when sound speeds differ. This produces a "mixed hybrid" class whose GW spectrum mimics ordinary hybrids. The public code HydróDex implements the classification.
  - On 11-17, Zhou et al.'s continuum lattice nucleation rate came within ~8% of one loop, and Gil et al. found modest higher-dimension-operator bounce corrections.
  - Net: the rate is robust, and the ambiguity sits in wall hydrodynamics.
- **Loop counts going up (heating).**
  - 11-11: Local Unitarity reached hadron colliders with four-dimensional IR-finite cross sections (Capatti et al.), and Bartocci et al. completed the resolved $B\to X_s\gamma$ term.
  - 11-13: six-loop QED renormalization (Li et al.), full-color three-loop $V$+jet (Gehrmann et al.), and two-loop EW precision for lepton colliders.
  - 11-16: three groups posted three-loop jet function and Lange–Neubert kernel results for $B^-\to\gamma\ell^-\bar\nu$, aiming at $\lambda_B$.
- **Auditing limits and proofs (steady, broadening).**
  - Banerjee et al. found pNGB linear-coupling bounds fail near sources.
  - Suezaki et al. weakened the supernova-heating $\sigma_{\nu\chi}$ limit by ~50×, and Cappiello et al. found resonant trapping can evade cooling bounds.
  - TESSERACT ruled out submerged sensors in superfluid ⁴He.
  - Zhu et al. found adaptive integrators can produce artificially low NLLs (CMS tetraquark search).
  - Chen et al.'s Lean 4 formalization found and closed a gap in a SUSY-GUT no-go proof.
- **Chiral lattice fermions (active).** Liu proved Craig's overlap measure matches the Hsu/Witten determinant for one SU(5) generation on $T^4$, the comparison Witten's 11-05 note invited (11-13). Lu et al. then showed the overlap Weyl fermion underlying Lüscher's construction is not reflection positive at finite spacing (11-17).

## Turning points

- **Nucleation is not the weak link.** The 11-17 lattice continuum result moves the GW-forecast skepticism downstream to hydrodynamics.
- **First elastic LZ fit.** Bera et al.'s anapole Majorana DM breaks the inelastic-only pattern that had held since September. Its relic abundance comes out right at ~300 GeV, and it predicts more low-energy recoils. In parallel, Lin et al.'s transport-equation treatment of solar capture weakens the bound by orders of magnitude when nuclear scattering is rare, but tightens the higgsino splitting bound by tens of keV.
- **$V_{ud}$ floor.** Novario et al. made the first EFT $\bar\delta_{\rm NS}$ evaluation across 12 transitions. Scale uncertainty is now negligible, $Z^2$-coherent $\mathcal{O}(\alpha^2)$ terms matter, and a contact-term combination correlated with $V_{ud}$ leaves $\delta V_{ud}\simeq6\times10^{-4}$.
- **Rate-independent $\kappa_\lambda$ at FCC-ee.** Altomonte et al.'s $Z$ tomography reaches ±2.9, compared with a quantum-Fisher-information limit of ±1. It also partly answers Shen's 11-09 question about magic-measure dependence.

## Open questions

- Does the anapole LZ model survive solar capture under Lin et al.'s recomputation? Watch also how Dai et al.'s $B-L$ three-bin likelihood fit fares.
- Do the three $B\to\gamma\ell\nu$ three-loop results agree where they overlap? No abstract reported a cross-check.
- What does Novario et al. imply for first-row unitarity? The abstracts gave no verdict.
- Which side of the inclusive/exclusive $|V_{cb}|$ split does Qu et al.'s LCSR+lattice BGL fit land on?
- NA62's measured BR$(K^+\to\pi^+\nu\bar\nu)$ from the doubled 2023–24 sample has not yet been reported.
- Zhang et al.'s $V(0)<0$ for $K^+\to\pi^+\ell^+\ell^-$ is 5.8–7.9σ at heavy charm but only 2.0–3.4σ at physical charm.
- Smaller items:
  - $K_1^*(1870)$: the $3S$–$2D$ interpretation predicts a subordinate $K\eta'$ mode, which sits awkwardly with the channel the state was seen in.
  - $\tau(D^+)$ upper error is unbounded at NLO dimension-seven.
  - Rubtsov et al.'s muon excess points to energetic early-cascade parents.
  - Foster et al. say superradiance spin-down limits need revising.

## Recurring references

- [arXiv:2611.13629](https://arxiv.org/abs/2611.13629): Machado et al., decomposition of the mass-ordering pulls.
- [arXiv:2611.21252](https://arxiv.org/abs/2611.21252): Cerrone et al., mass-ordering sum rule.
- [arXiv:2611.17402](https://arxiv.org/abs/2611.17402), [arXiv:2611.17411](https://arxiv.org/abs/2611.17411): Barni et al., non-unique bubble-wall flows.
- [arXiv:2611.18794](https://arxiv.org/abs/2611.18794): Zhou et al., lattice nucleation rate.
- [arXiv:2611.15957](https://arxiv.org/abs/2611.15957): Bera et al., anapole fit to the LZ event.
- [arXiv:2611.16689](https://arxiv.org/abs/2611.16689): Lin et al., solar capture recomputed.
- [arXiv:2611.18202](https://arxiv.org/abs/2611.18202), [arXiv:2611.18206](https://arxiv.org/abs/2611.18206), [arXiv:2611.18204](https://arxiv.org/abs/2611.18204): $B\to\gamma\ell\nu$ three-loop trio.
- [arXiv:2611.16544](https://arxiv.org/abs/2611.16544): Liu, overlap measure vs continuum determinant.
- [arXiv:2611.20084](https://arxiv.org/abs/2611.20084): Lu et al., overlap fermion reflection positivity.
- [arXiv:2611.18830](https://arxiv.org/abs/2611.18830), [arXiv:2611.18843](https://arxiv.org/abs/2611.18843): Novario et al., $V_{ud}$ nuclear corrections.
- [arXiv:2611.13184](https://arxiv.org/abs/2611.13184): Capatti et al., Local Unitarity at hadron colliders.
