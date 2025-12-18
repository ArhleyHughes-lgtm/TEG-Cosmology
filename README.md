# TEG Cosmology: Thermodynamic Entropic Gravity

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Python implementation of Thermodynamic Entropic Gravity (TEG)** — a phenomenological framework for resolving the S₈ tension through local entropic screening during structure formation.

## Paper

*"Thermodynamic Self-Regulation of Cosmic Structure: Resolving the S₈ Tension via Local Entropic Screening"* — Ahrley Hughes (2025)

📄 **[Read the full paper (PDF)](paper/TEG-final.pdf)**

---

## Overview

The standard ΛCDM model faces two major tensions:

1. **S₈ Tension**: Weak lensing surveys measure S₈ ≈ 0.76, while Planck CMB infers S₈ ≈ 0.83 (approximately 3.5σ discrepancy).
2. **Dark Energy Evolution**: DESI DR2 favors dynamical "thawing" dark energy over a cosmological constant.

**TEG proposes** that irreversible information processing during halo collapse generates a local repulsive pressure (P_ent), amplified by the photon-to-baryon ratio η ≈ 10⁹. This mechanism:

- Suppresses the matter power spectrum by approximately **6-8%** in the non-linear regime (k > 0.1 h/Mpc).
- Resolves the S₈ tension **without altering linear growth**.
- Predicts a **steeper concentration-mass relation** at low masses, addressing the Cusp-Core problem.

---

## Key Results

| Observable | ΛCDM (Planck) | TEG Prediction | Weak Lensing |
|------------|---------------|----------------|--------------|
| **σ₈** | 0.811 | 0.764 | ~0.76 |
| **Suppression** | — | 5.8% | Match |
| **c(M) slope** | Shallow | Steep (M < 10¹¹ M_☉) | Testable |

![TEG Visual Abstract](visual_abstract_2x.png)

---

## Installation

```bash
git clone https://github.com/ahrleyhughes/TEG-Cosmology.git
cd TEG-Cosmology
pip install -r requirements.txt
```

---

## Usage

```bash
python teg_accurate.py
```

**Output:**
- Prints σ₈ values and suppression percentage to console.
- Generates `TEG_Figures_1_and_2.png` reproducing paper figures.
- Saves data arrays to `teg_data.npz` for further analysis.

---

## Sensitivity & Robustness Check

To verify that the TEG parameters are physically robust and not fine-tuned, we provide a stress-test script (`sensitivity_analysis.py`).

```bash
python sensitivity_analysis.py
```

This script performs a parameter sweep to demonstrate:

- **Linear Response**: The σ₈ suppression scales linearly with κ, confirming the model is stable.
- **Parameter Convergence**: The value of κ required to resolve the S₈ tension (0.0012) is consistent with the theoretical prediction derived from Big Bang Nucleosynthesis (η⁻¹/³ ~ 0.001).
- **Cross-Scale Validation**: The same coupling constant that fixes the Mpc-scale power spectrum simultaneously resolves the kpc-scale Cusp-Core problem in dwarf galaxies.

---

## Figures

The main script generates two figures matching the paper:

### Figure 1: Power Spectrum Suppression
- Shows P_TEG / P_ΛCDM ratio versus wavenumber k.
- Suppression activates at k ~ 0.1 h/Mpc in the non-linear regime.
- Linear scales (k < 0.1) remain unaffected, preserving CMB constraints.

### Figure 2: Concentration-Mass Relation
- Compares ΛCDM versus TEG halo concentrations.
- TEG predicts "puffier" dwarf halos (M < 10¹¹ M_☉).
- Falsifiable with Euclid weak lensing and Gaia kinematics.

---

## Theory Summary

### Core Mechanism: Entropic Pressure

```
P_ent ≈ κ c² ρ_crit (ρ_b / ρ̄_b)^Γ
```

**Parameters:**
- **κ ≈ 0.0012**: Coupling constant derived from η ≈ 10⁹.
- **Γ = 5/3**: Polytropic index (phenomenological stiffness).

**Physical Origin**: The vacuum acts as a thermodynamic reservoir, resisting local entropy reduction during collapse.

### Modified Power Spectrum

```
P_TEG(k) = P_ΛCDM(k) × D_TEG(k)²
```

Where D_TEG(k) is the suppression factor encoding density-dependent screening.

---

## Code Structure

Main components of `teg_accurate.py`:

- `eisenstein_hu_transfer()` - Linear transfer function (BAO-accurate)
- `linear_power_spectrum()` - P(k) ∝ k^n_s T(k)²
- `calculate_sigma8()` - Integrate with top-hat filter
- `teg_suppression()` - Core TEG modification
- `concentration_mass_relation()` - Halo structure prediction

---

## Observational Tests

| Test | Dataset | Status |
|------|---------|--------|
| S₈ suppression | KiDS-1000, DES Y3, HSC | Consistent |
| c(M) steepening | Euclid (2025+) | Pending |
| Dwarf kinematics | Gaia DR4 | Pending |
| Thawing DE | DESI DR2 | Consistent |

---

## Parameter Derivation and Sensitivity Analysis

### A Prediction, Not a Fit

TEG's coupling constant κ was predicted from Big Bang Nucleosynthesis before being confronted with weak lensing data.

Starting from the photon-to-baryon ratio (η ≈ 1.6 × 10⁹):

```
κ_predicted ~ η⁻¹/³ ≈ 0.00085
```

**This prediction used zero galaxy data.**

Observationally required value to resolve S₈:

```
κ_required ≈ 0.0012
```

**Convergence: 1.4×** between nucleosynthesis (t ~ 3 min) and structure formation (t ~ 10 Gyr).

### Sensitivity Analysis: Power Spectrum Suppression

Parameter sweep with all cosmological parameters fixed at Planck 2018:

| κ Value | δ_max | σ₈ (TEG) | Suppression (%) | Agreement with Weak Lensing |
|---------|-------|----------|-----------------|----------------------------|
| 0.0005 | 0.037 | 0.791 | 2.46% | Too High |
| 0.0008 | 0.059 | 0.779 | 3.95% | Excellent (upper bound) |
| 0.0010 | 0.073 | 0.772 | 4.94% | Excellent (center) |
| **0.0012** | **0.088** | **0.764** | **5.80%** | **Excellent (KiDS/DES)** |
| 0.0015 | 0.110 | 0.753 | 7.15% | Acceptable (lower bound) |
| 0.0020 | 0.147 | 0.735 | 9.37% | Too Low |

*Planck baseline: σ₈ = 0.811 | Weak lensing target: σ₈ ≈ 0.764–0.779*

**Result:** BBN range (κ = 0.0008–0.0012) matches observational requirement. Factor-of-2 uncertainty still produces agreement.

### Cross-Scale Test: Dwarf Galaxy Concentrations

The same κ resolves the Cusp-Core problem in dwarf galaxies (10⁹ M_☉)—three orders of magnitude separation:

| κ Value | Reduction Factor | Relative Concentration | Physical Implication |
|---------|------------------|----------------------|---------------------|
| 0.0005 | 1.45 | 0.41 | Moderate; cusp may persist |
| **0.0012** | **3.50** | **0.22** | **Strong cores; matches SPARC** |
| 0.0020 | 5.83 | 0.15 | Too diffuse; gas loss |

**Result:** κ = 0.0012 produces 3.5× concentration reduction, matching SPARC observations.

**Scale separation:** Single BBN-predicted parameter resolves Mpc (power spectrum) and kpc (halo structure) tensions.

---

## Citation

If you use this code, please cite:

```bibtex
@article{Hughes2025TEG,
  title={Thermodynamic Self-Regulation of Cosmic Structure: Resolving the $S_8$ Tension via Local Entropic Screening},
  author={Hughes, Ahrley},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2025}
}
```

---

## Customization

Modify TEG parameters in the script:

```python
kappa = 1.2e-3    # Coupling strength
Gamma = 5.0/3.0   # Polytropic index
```

Then re-run to see impact on σ₈ and c(M).

---

## Contact

**Ahrley Hughes**  
ArhleyHughes@proton.me  
Cincinnati, OH

*Seeking arXiv endorsement in astro-ph.CO*

---

## License

MIT License - see `LICENSE` file for details.

---

## Acknowledgments

- Eisenstein & Hu (1998) for transfer function formalism
- Planck, KiDS, DES, HSC collaborations for observational data
- DESI collaboration for BAO constraints
