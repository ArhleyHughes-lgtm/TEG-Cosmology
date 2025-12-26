import numpy as np
import matplotlib.pyplot as plt


def get_teg_suppression(k, z, kappa_0=0.0012, n_scaling=1.5):
    # Scaling ansatz: Effective coupling kappa scales as (1+z)^(-n)
    kappa_z = kappa_0 * ((1 + z)**(-n_scaling))
    
    # Delta_max derived from kappa
    delta_max_z = (kappa_z / 0.0012) * 0.088
    
    # Shape function pivot
    k_pivot = 0.1 * (1 + z)**(2/3) 
    
    log_k = np.log10(k)
    log_pivot = np.log10(k_pivot)
    
    # Logistic suppression
    fk = 1.0 / (1.0 + np.exp(-2.0 * (log_k - log_pivot)/0.5))
    
    ratio = 1.0 - delta_max_z * fk
    return ratio

# Generate Plot
k = np.logspace(-2, 1.5, 200) 
redshifts = [0, 0.5, 1.0, 2.0, 4.0]
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd'] 

plt.figure(figsize=(8, 6))

for z, color in zip(redshifts, colors):
    ratio = get_teg_suppression(k, z, kappa_0=0.0012, n_scaling=1.5)
    plt.semilogx(k, ratio, label=f'z = {z}', color=color, linewidth=2.5)

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
print("Saved TEG_Redshift_Evolution.png")

# Keep window open if run via double-click
# input("Press Enter to exit...")
