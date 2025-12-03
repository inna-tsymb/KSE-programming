import matplotlib.pyplot as plt
import numpy as np

# Generate data
time = np.linspace(0, 10, 100)
expression1 = np.sin(time)
expression2 = np.cos(time)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(time, expression1, label='Gene A', linewidth=2)
plt.plot(time, expression2, label='Gene B', linewidth=2, linestyle='--')

plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Expression Over Time', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()