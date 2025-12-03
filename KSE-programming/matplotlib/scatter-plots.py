import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
gene_length = np.random.normal(1000, 300, 50)
expression = 2 * gene_length + np.random.normal(0, 500, 50)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(gene_length, expression, alpha=0.6, s=100, c='blue', edgecolors='black')

plt.xlabel('Gene Length (bp)', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Length vs Expression', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()