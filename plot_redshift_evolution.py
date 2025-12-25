import numpy as np
import matplotlib.pyplot as plt
from colossus.cosmology import cosmology

# Set cosmology to Planck 2018
params = {'flat': True, 'H0': 67.66, 'Om0': 0.3111, 'Ob0': 0.049, 'sigma8': 0.811, 'ns': 0.9665}
cosmo = cosmology.setCosmology('planck18', params)

def get_teg_suppression(k, z, kappa_0=0.0012, n_scaling=1.5):
    """
    Returns the suppression ratio P_TEG(k) / P_LCDM(k) at redshift z.
    
    Ansatz: Effective coupling kappa scales as (1+z)^(-n).
    If n > 0, the effect was weaker in the past (high z).
    """
    # Scaling ansatz
    kappa_z = kappa_0 * ((1 + z)**(-n_scaling))
    
    # Delta_max derived from kappa (linear approximation from your sensitivity study)
    # [cite_start]At z=0, kappa=0.0012 -> delta_max ~ 0.088 [cite: 56]
    delta_max_z = (kappa_z / 0.0012) * 0.088
    
    # Shape function (sigmoid activation in non-linear regime)
    # We shift the activation scale k_start slightly with z because non-linearity 
    # happens at smaller scales (higher k) in the past.
    k_pivot = 0.1 * (1 + z)**(2/3) 
    
    # Calculate suppression factor D(k)
    # Using the logistic form from your paper
    # f(k) = 1 / (1 + exp(-2 * (log10(k) - log10(k_pivot))))
    log_k = np.log10(k)
    log_pivot = np.log10(k_pivot)
    
    fk = 1.0 / (1.0 + np.exp(-2.0 * (log_k - log_pivot)/0.5))
    
    ratio = 1.0 - delta_max_z * fk
    return ratio

# Generate Plot
k = np.logspace(-2, 1.5, 200) # 0.01 to 30 h/Mpc
redshifts = [0, 0.5, 1.0, 2.0, 4.0]
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd'] # Red to Purple

plt.figure(figsize=(8, 6))

for z, color in zip(redshifts, colors):
    ratio = get_teg_suppression(k, z, kappa_0=0.0012, n_scaling=1.5)
    plt.semilogx(k, ratio, label=f'z = {z}', color=color, linewidth=2.5)

# Formatting
plt.axhline(1, color='k', linestyle='--', alpha=0.5)
plt.fill_between([0.1, 10], 0.8, 1.05, color='yellow', alpha=0.1, label='Lensing Window')
plt.xlabel(r'Wavenumber $k$ [$h$/Mpc]', fontsize=12)
plt.ylabel(r'Ratio $P_{\mathrm{TEG}} / P_{\Lambda\mathrm{CDM}}$', fontsize=12)
plt.title(r'Redshift Evolution of Suppression ($\kappa \propto (1+z)^{-1.5}$)', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.ylim(0.85, 1.02)
plt.xlim(0.01, 20)

plt.tight_layout()
plt.savefig('TEG_Redshift_Evolution.png', dpi=300)
print("Redshift figure generated.")
