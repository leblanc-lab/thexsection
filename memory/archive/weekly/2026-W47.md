# The Cross Section — weekly synthesis, week ending 2026-11-18

The week had two main currents. Model-building around the LZ 248 keV recoil intensified, and the tests it is judged by shifted when solar capture was recomputed. A self-audit habit also spread across the field, covering GW forecasts, astrophysical limits and quoted error bars. Perturbative precision kept climbing in loop order and reached heavy-flavor SCET at N³LO. Nuclear-structure input to $V_{ud}$ hit a contact-term floor. The week closed with a new LHC anomaly: ATLAS's 3.5σ instanton-like excess.

## Running themes

**LZ 248 keV event: model space widening (heating up).**
- **Elastic option:** Bera et al. offered the first elastic fit. It uses an anapole-only Majorana fermion at ~300 GeV, matches the relic abundance, and predicts more events at lower recoil energy ([arXiv:2611.15957](https://arxiv.org/abs/2611.15957)). Its abstract does not address solar capture.
- **Inelastic models kept arriving:**
  - gauged $B-L$ with a three-bin likelihood ([arXiv:2611.16553](https://arxiv.org/abs/2611.16553));
  - composite-Higgs resonances at a few TeV with ~300 keV splittings, claiming consistency with solar capture and the high-energy sideband ([arXiv:2611.21737](https://arxiv.org/abs/2611.21737));
  - a radion portal at 1 TeV with δ=340 keV, which checks solar neutrinos only by proxy ([arXiv:2611.22890](https://arxiv.org/abs/2611.22890)).

**Loop order climbing (heating up).**
- **11-13:**
  - six-loop QED renormalization for arbitrary $N_f$, pitched as a route to six-loop QCD ([arXiv:2611.15366](https://arxiv.org/abs/2611.15366));
  - full-color three-loop $V$+jet ([arXiv:2611.15836](https://arxiv.org/abs/2611.15836));
  - two-loop electroweak work for lepton colliders ([arXiv:2611.15807](https://arxiv.org/abs/2611.15807), [arXiv:2611.17171](https://arxiv.org/abs/2611.17171)).
- **11-16:** three groups posted N³LO pieces for $B^-\to\gamma\ell\bar\nu$ on the same day ([arXiv:2611.18202](https://arxiv.org/abs/2611.18202), [arXiv:2611.18206](https://arxiv.org/abs/2611.18206), [arXiv:2611.18204](https://arxiv.org/abs/2611.18204)). The largest three-loop effect sits in the jet function, and the payoff is a cleaner $\lambda_B$ extraction.

**GW forecasts vs. transition dynamics (steady, refocusing).**
- **11-13:** Completion criteria share a boundary where homogeneity fails ([arXiv:2611.14593](https://arxiv.org/abs/2611.14593)). The Higgs trilinear is not robust to dimension-six operators, though the GW and di-Higgs predictions are ([arXiv:2611.15856](https://arxiv.org/abs/2611.15856)).
- **11-16:** Barni et al. showed that $(\xi_w,\alpha_N)$ does not fix a unique bubble flow when sound speeds differ. A new "mixed hybrid" class mimics ordinary hybrids in GWs, and the public code HydróDex implements the classification ([arXiv:2611.17402](https://arxiv.org/abs/2611.17402), [arXiv:2611.17411](https://arxiv.org/abs/2611.17411)).

**Auditing limits and error bars (steady; direction flipped mid-week).**
- **Limits loosened on 11-16:**
  - supernova core-heating DM limits weaken ~50× ([arXiv:2611.17922](https://arxiv.org/abs/2611.17922));
  - resonant trapping evades cooling bounds ([arXiv:2611.17604](https://arxiv.org/abs/2611.17604));
  - TESSERACT measured >99% phonon loss into superfluid ⁴He ([arXiv:2611.17365](https://arxiv.org/abs/2611.17365)).
- **Limits tightened on 11-18:**
  - the ALP "pion chimney" was closed using old ATLAS data ([arXiv:2611.21728](https://arxiv.org/abs/2611.21728));
  - SN 1987A gives $\mu_{\nu_e}\lesssim4.8\times10^{-13}\mu_B$ ([arXiv:2611.21729](https://arxiv.org/abs/2611.21729)).
- **Error-bar audits:**
  - treating HERA systematics as uncertain cuts $\chi^2$ from 1363 to 1306 ([arXiv:2611.22891](https://arxiv.org/abs/2611.22891));
  - the lensing-$H_0$ redshift trend drops to ~1σ ([arXiv:2611.21821](https://arxiv.org/abs/2611.21821));
  - adaptive integrators can produce spurious low NLLs ([arXiv:2611.19355](https://arxiv.org/abs/2611.19355));
  - top-mass-scheme spreads in $gg\to ZH$ reach 32–50% ([arXiv:2611.23020](https://arxiv.org/abs/2611.23020)).

**Unclosed LHC excesses (heating up).** ATLAS sees a 3.5σ excess of low-mass isotropic events in 1.6 nb⁻¹ ([arXiv:2611.22092](https://arxiv.org/abs/2611.22092)). It joins the 13.6 GeV diphoton and 146 GeV $e\mu$ excesses, a list that had already prompted a look-elsewhere reckoning.

## Turning points

- **Solar capture is no longer a fixed hurdle.** A transport-equation recomputation shows annihilation drops by orders of magnitude when nuclear scattering is rare. For the inelastic higgsino, it tightens the splitting bound by tens of keV ([arXiv:2611.16689](https://arxiv.org/abs/2611.16689)). LZ models should now be judged against this calculation rather than against proxies.
- **The weak link in the GW pipeline moved.** Lattice nucleation rates differ from one loop by only ~8% ([arXiv:2611.18794](https://arxiv.org/abs/2611.18794)). Consistent dimension-six bounce corrections are modest ([arXiv:2611.20938](https://arxiv.org/abs/2611.20938)). The ambiguity now sits in wall hydrodynamics ([arXiv:2611.17402](https://arxiv.org/abs/2611.17402)).
- **$V_{ud}$ reached a nuclear floor.** The first EFT evaluation of $\bar\delta_{\rm NS}$ across 12 superallowed transitions makes scale uncertainty negligible ([arXiv:2611.18830](https://arxiv.org/abs/2611.18830), [arXiv:2611.18843](https://arxiv.org/abs/2611.18843)). The remaining limit is a magnetic Gamow–Teller contact term that is correlated with $V_{ud}$ itself, leaving $\delta V_{ud}\simeq6\times10^{-4}$.
- **The chiral-lattice thread advanced on both sides.**
  - Liu proves Craig's overlap measure matches the Hsu/Witten determinant up to a local counterterm, for one SU(5) generation on $T^4$ ([arXiv:2611.16544](https://arxiv.org/abs/2611.16544)).
  - Lu et al. show the overlap Weyl fermion is not reflection positive at finite spacing ([arXiv:2611.20084](https://arxiv.org/abs/2611.20084)).

## Open questions

- **ATLAS instanton excess:** Is the 3.5σ local? Does it survive scrutiny of the minimum-bias background modeling ([arXiv:2611.22092](https://arxiv.org/abs/2611.22092))?
- **LZ:**
  - Does the anapole model survive the new solar-capture treatment?
  - Does the full LZ run show its predicted low-energy events?
  - Does the sideband test hold up?
- **Three-loop cross-check:** Do the overlapping three-loop Lange–Neubert kernels and jet functions agree? No abstract reports a comparison.
- **First-row unitarity:** The Novario abstracts don't say where the new $V_{ud}$ leaves it.
- **Numbers the abstracts withheld:**
  - NA62's measured BR($K^+\to\pi^+\nu\bar\nu$) ([arXiv:2611.16530](https://arxiv.org/abs/2611.16530));
  - which side of the inclusive/exclusive split Qu et al.'s $|V_{cb}|$ lands on ([arXiv:2611.17945](https://arxiv.org/abs/2611.17945)).
- **Smaller threads:**
  - $V(0)<0$ for $K^+\to\pi^+\ell\ell$ weakens to 2.0–3.4σ at physical charm ([arXiv:2611.17800](https://arxiv.org/abs/2611.17800));
  - $\tau(D^+)=1.41^{+\infty}_{-0.76}$ ps ([arXiv:2611.20747](https://arxiv.org/abs/2611.20747));
  - the $K_1^*(1870)$ interpretation predicts a subordinate $K\eta'$ mode, at odds with its discovery channel ([arXiv:2611.19498](https://arxiv.org/abs/2611.19498)).
- **Mass ordering:** Cerrone et al.'s intercept formalism ([arXiv:2611.21252](https://arxiv.org/abs/2611.21252)) should frame future DeepCore/JUNO combinations.

## Recurring references

- **[arXiv:2611.16689](https://arxiv.org/abs/2611.16689):** solar-capture recomputation, invoked again on 11-18 as the benchmark LZ models should meet.
- **[arXiv:2611.15957](https://arxiv.org/abs/2611.15957):** the elastic LZ baseline.
- **[arXiv:2611.21737](https://arxiv.org/abs/2611.21737):** first LZ model to claim solar capture, sideband and gamma-ray checks in one abstract.
- **[arXiv:2611.17402](https://arxiv.org/abs/2611.17402) / [arXiv:2611.17411](https://arxiv.org/abs/2611.17411):** non-unique bubble hydrodynamics, cited on 11-17 as where the GW ambiguity now sits.
- **[arXiv:2611.18202](https://arxiv.org/abs/2611.18202), [arXiv:2611.18206](https://arxiv.org/abs/2611.18206), [arXiv:2611.18204](https://arxiv.org/abs/2611.18204):** the $B\to\gamma\ell\nu$ N³LO trio.
- **[arXiv:2611.18830](https://arxiv.org/abs/2611.18830) / [arXiv:2611.18843](https://arxiv.org/abs/2611.18843):** the $V_{ud}$ contact-term floor.
- **[arXiv:2611.16544](https://arxiv.org/abs/2611.16544) / [arXiv:2611.20084](https://arxiv.org/abs/2611.20084):** the chiral-lattice-fermion thread.
- **[arXiv:2611.22092](https://arxiv.org/abs/2611.22092):** the ATLAS instanton-like excess.
