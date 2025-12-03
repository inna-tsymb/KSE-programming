import matplotlib.pyplot as plt
import numpy as np

# Create subplots with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Data
time = np.linspace(0, 24, 100)
gene1 = np.sin(time)
gene2 = np.cos(time)

# Top plot
ax1.plot(time, gene1, 'b-', linewidth=2)
ax1.set_ylabel('Gene A Expression', fontsize=12)
ax1.set_title('Gene Expression Patterns', fontsize=14)
ax1.grid(True, alpha=0.3)

# Bottom plot
ax2.plot(time, gene2, 'r-', linewidth=2)
ax2.set_xlabel('Time (hours)', fontsize=12)
ax2.set_ylabel('Gene B Expression', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()