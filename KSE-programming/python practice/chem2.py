import numpy as np

# --- 1. Data Input ---

# Original Ligand concentration [L] in nM
L = np.array([3, 10, 30, 100, 300, 1000, 3000])

# Original measured Effect/Response (E)
E = np.array([0.020,0.065,0.17,0.38,0.63,0.79,0.84])

# --- 2. Transform Data (Lineweaver-Burk-like) ---
# x = 1/[L]
x_transformed = 1 / L 
# y = 1/E
y_transformed = 1 / E

# --- 3. Linear Regression (Step 2) ---
# Use numpy.polyfit to find the best-fit line (1st degree polynomial)
# polyfit returns [slope (m), y-intercept (b)]
m, b = np.polyfit(x_transformed, y_transformed, 1)

print("--- Linear Regression Results (y = mx + b) ---")
print(f"Slope (m): {m:.4f}")
print(f"Y-intercept (b): {b:.4f}")

# --- 4. Calculate Parameters (Step 3) ---

# Calculate E_max from the y-intercept (b):
# b = 1 / E_max  =>  E_max = 1 / b
E_max = 1 / b

# Calculate K_D from the slope (m) and E_max:
# m = K_D / E_max  =>  K_D = m * E_max
K_D = m * E_max

print("\n--- Biochemical Parameter Results ---")
print(f"E_max (max effect/response): {E_max:.3f}")
print(f"K_D (Dissociation Constant, nM): {K_D:.1f}")