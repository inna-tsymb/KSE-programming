import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 50)
y = np.sin(x)

# Create customized plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='#2E86AB', linewidth=3, linestyle='-', 
         marker='o', markersize=6, markerfacecolor='white', 
         markeredgewidth=2, markeredgecolor='#2E86AB', label='sin(x)')

# Customize
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('y', fontsize=14, fontweight='bold')
plt.title('Customized Sine Wave', fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.5)
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.show()