import matplotlib.pyplot as plt
import numpy as np

# Create 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Data
x = np.linspace(0, 10, 100)

# Plot 1: Line
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine Wave')

# Plot 2: Scatter
axes[0, 1].scatter(x, np.cos(x))
axes[0, 1].set_title('Cosine Scatter')

# Plot 3: Bar
axes[1, 0].bar(['A', 'B', 'C'], [3, 7, 5])
axes[1, 0].set_title('Bar Chart')

# Plot 4: Histogram
axes[1, 1].hist(np.random.normal(0, 1, 1000), bins=30)
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()