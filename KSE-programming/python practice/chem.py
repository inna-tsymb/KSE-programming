import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
substrate_conc = np.array([3, 5, 10, 30, 90])  # [S] in µM
velocity = np.array([4.6, 7.5, 14.3, 27.3, 39.1])  # v in µmol/min

# Calculate reciprocals
inv_substrate = 1 / substrate_conc
inv_velocity = 1 / velocity

# Perform linear regression using linregress
slope, intercept, r_value, p_value, std_err = linregress(inv_substrate, inv_velocity)

# Calculate Vmax and Km
Vmax = 1 / intercept
Km = slope * Vmax

print(f"Slope: {slope:.3f}, Intercept: {intercept:.3f}")
print(f"Vmax ≈ {Vmax:.2f} µmol/min, Km ≈ {Km:.2f} µM")

# Plot Lineweaver–Burk
plt.figure(figsize=(8, 6))
plt.scatter(inv_substrate, inv_velocity, color='blue', label='Data Points')
plt.plot(inv_substrate, intercept + slope * inv_substrate, color='red', label='Regression Line')
plt.xlabel('1/[S] (1/µM)')
plt.ylabel('1/v (1/µmol/min)')
plt.title('Lineweaver–Burk Plot')
plt.legend()
plt.grid(True)
plt.show()