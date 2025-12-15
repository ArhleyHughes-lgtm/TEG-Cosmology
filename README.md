# TEG Cosmology: Thermodynamic Entropic Gravity

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Python implementation of Thermodynamic Entropic Gravity (TEG)** — a phenomenological framework for resolving the S8 tension through local entropic screening during structure formation.

**Paper:** *"Thermodynamic Self-Regulation of Cosmic Structure: Resolving the S8 Tension via Local Entropic Screening"* — Ahrley Hughes (2025)

---

## Overview

The standard ΛCDM model faces two major tensions:
1. **S8 Tension**: Weak lensing surveys measure S8 ≈ 0.76, while Planck CMB infers S8 ≈ 0.83 (~3.5σ discrepancy)
2. **Dark Energy Evolution**: DESI DR2 favors dynamical "thawing" dark energy over a cosmological constant

**TEG proposes** that irreversible information processing during halo collapse generates a local repulsive pressure (P_ent), amplified by the photon-to-baryon ratio η ≈ 10⁹. This mechanism:
- Suppresses the matter power spectrum by **~6-8%** in the non-linear regime (k > 0.1 h/Mpc)
- Resolves the S8 tension **without altering linear growth**
- Predicts a **steeper concentration-mass relation** at low masses (Cusp-Core resolution)

---

## Key Results

| Observable | ΛCDM (Planck) | TEG Prediction | Weak Lensing |
|------------|---------------|----------------|--------------|
| **σ8** | 0.811 | 0.764 | ~0.76 |
| **Suppression** | — | 5.8% | Match |
| **c(M) slope** | Shallow | Steep (M < 10¹¹ M☉) | Testable |

---

## Quick Start

### Installation

```bash
git clone [https://github.com/ahrleyhughes/TEG-Cosmology.git](https://github.com/ahrleyhughes/TEG-Cosmology.git)
cd TEG-Cosmology
pip install -r requirements.txt
