import matplotlib.pyplot as plt
import numpy as np

# Create plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2)
plt.xlabel('x', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)
plt.title('Sine Wave', fontsize=14)
plt.grid(True, alpha=0.3)

# Save in different formats
plt.savefig('sine_plot.png', dpi=300, bbox_inches='tight')
plt.savefig('sine_plot.pdf', bbox_inches='tight')
plt.savefig('sine_plot.svg', bbox_inches='tight')

plt.show()