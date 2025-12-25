# TEG Cosmology: Topological Entropic Gravity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18051561.svg)](https://doi.org/10.5281/zenodo.18051561)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A unified cosmological framework** where cosmic expansion and structural growth are governed by the topology of the vacuum, modeled as a ν=5/3 Fractional Quantum Hall fluid.

## Paper

**"Topological Entropic Gravity: Unifying the Quantum Hall Vacuum with Cosmic Structure Formation to Resolve the S₈ Tension"** — Ahrley Hughes (2025)

📄 **[Read the Preprint on Zenodo](https://doi.org/10.5281/zenodo.18051561)**

---

## Overview

The standard ΛCDM model faces two major tensions:

1. **S₈ Tension**: Weak lensing surveys (KiDS, DES, HSC) measure S₈ ≈ 0.76, while Planck CMB infers S₈ ≈ 0.83 (>3σ discrepancy).
2. **Dark Energy Evolution**: DESI DR2 favors dynamical "thawing" dark energy.

**TEG proposes** that the vacuum behaves as an incompressible topological fluid. Gravitational collapse locally increases the filling factor, generating a repulsive **Entropic Pressure**. This force is protected by **Berry phases**, preserving quantum coherence and avoiding the decoherence issues of standard entropic gravity.

---

## Key Results

| Observable | ΛCDM (Planck) | TEG Prediction | Weak Lensing Data |
|------------|---------------|----------------|-------------------|
| **σ₈** | 0.811 | **0.766** | ~0.76 – 0.78 |
| **Suppression** | — | **5.6%** | Matches required suppression |
| **Halo Structure** | Cuspy (NFW) | **Cored** (M < 10¹¹ M☉) | Matches SPARC / LITTLE THINGS |

![TEG Visual Abstract](visual_abstract_2x.png)

---

## The "Zero-Parameter" Derivation

TEG is not a fit to galaxy data. The parameters are derived entirely from fundamental constants and condensed matter topology.

### 1. The Physics

- **Stiffness (Γ = 5/3):** Fixed by the topology of the vacuum, identified as the ν=5/3 Quantum Hall state (the stable particle-hole conjugate of the Laughlin ν=1/3 state).
- **Coupling (κ ≈ α/2π):** Derived from the Schwinger term for vacuum polarization.

### 2. Parameter Convergence

The value required to solve the tension matches theoretical predictions from two independent physical routes:

| Source | Formula | Value | Gap to Obs. |
|--------|---------|-------|-------------|
| **QED (Vacuum Polarization)** | κ = α/2π | **0.00116** | **3%** |
| **Thermodynamics (BBN)** | κ ~ η^(-1/3) | 0.00085 | 30% |
| **Geometric Mean** | √(κ_QED × κ_thermo) | 0.00099 | 18% |
| **Observational Fit** | (Required for S₈) | **0.00120** | — |

**Conclusion:** The coupling constant is not fine-tuned; it is a fundamental property of the vacuum.

---

## Code Usage

### Installation

```bash
git clone https://github.com/ahrleyhughes/TEG-Cosmology.git
cd TEG-Cosmology
pip install -r requirements.txt
```

### Main Simulation

Calculates the power spectrum suppression and generates publication figures.

```bash
python teg_accurate.py
```

**Output:**
- `TEG_Figures_1_and_2.png`: Reproduces the paper's main figures.
- Console output: Detailed σ₈ comparison.
- `teg_data.npz`: Saved arrays for external analysis.

### Sensitivity Analysis

Verifies robustness against parameter variation.

```bash
python sensitivity_analysis.py
```

---

## Figures

### Figure 1: Power Spectrum Suppression

- Shows P_TEG / P_ΛCDM.
- Suppression activates exactly in the non-linear regime (k > 0.1 h/Mpc).
- Linear scales remain unity, preserving CMB constraints.

### Figure 2: Concentration-Mass Relation

- Demonstrates the **Topological Signature** of the theory.
- Predicts a steep divergence from ΛCDM for dwarf halos (M < 10¹¹ M☉).
- Transforms "cuspy" NFW profiles into constant-density cores.

---

## Model Discrimination (TEG vs. Baryonic Feedback)

A key requirement for any alternative explanation of the S₈ tension is **non-degeneracy** with baryonic feedback models.

To demonstrate this, we compare the predicted suppression shape from TEG with a representative AGN-feedback suppression profile (schematic, HMCode/OWLS-like).

![Model Discrimination](TEG_vs_Baryons.png)

**Key distinction:**
- **TEG** produces a monotonic, saturated “shelf” of suppression driven by a fundamental pressure term.
- **Baryonic feedback** typically produces a localized “spoon” shape with an overshoot at high k due to cooling and star formation.

This qualitative difference provides a clear observational discriminant, independent of overall suppression amplitude.

---
## Redshift Evolution of Suppression

TEG predicts that suppression should activate primarily at **late times**, consistent with a thawing dark energy interpretation and the absence of an S₈ tension at high redshift.

We parameterize this behavior using a minimal phenomenological ansatz:

\[
\kappa(z) = \kappa_0 (1 + z)^{-n},
\]

with \( n > 0 \) indicating weaker effects in the early universe.

![Redshift Evolution](TEG_Redshift_Evolution.png)

For illustrative values \( n \sim 1–2 \), suppression becomes significant only at \( z \lesssim 1 \), matching the redshift range probed by weak lensing surveys.

This scaling is **not assumed as a derivation**, but introduced to demonstrate testable, model-specific predictions distinguishable from baryonic feedback.
---

## Falsifiability & Testable Predictions

TEG makes concrete predictions distinguishable from both ΛCDM and baryonic feedback models:

### Robust Predictions
- **Scale-dependent suppression** of the matter power spectrum by ~5–6% for \( k > 0.1\,h/\mathrm{Mpc} \), with no impact on linear scales.
- **Late-time activation** of suppression, consistent with thawing dark energy behavior.
- **Mass-dependent reduction of halo concentrations** for \( M \lesssim 10^{11} M_\odot \), reducing central cusps without stochastic feedback effects.

### Model Discriminants
- The suppression profile exhibits a **monotonic saturation**, unlike the characteristic “spoon” shape of AGN feedback.
- The redshift evolution of suppression differs qualitatively from baryonic prescriptions tied to star formation history.

### Speculative Extensions (Theoretical)
- **Halo Oblateness**: If the vacuum exhibits Quantum Hall topology, chiral edge modes may induce small anisotropies in dwarf halos.
- **Quantization**: If κ reflects topological phase structure, discrete changes may occur across cosmic epochs.

These extensions are secondary to the core, falsifiable predictions above.

---

## Citation

```bibtex
@article{Hughes2025TEG,
  title={Topological Entropic Gravity: Unifying the Quantum Hall Vacuum with Cosmic Structure Formation to Resolve the S8 Tension},
  author={Hughes, Ahrley},
  publisher={Zenodo},
  year={2025},
  doi={10.5281/zenodo.18051561},
  url={https://doi.org/10.5281/zenodo.18051561}
}
```

---

## Contact

**Ahrley Hughes**  
Independent Researcher, Cincinnati, OH  
ArhleyHughes@proton.me

---

## License

MIT License - see `LICENSE` file for details.
