import matplotlib.pyplot as plt
import numpy as np

# Generate sample data (gene expression values)
np.random.seed(42)
expression_data = np.random.normal(5, 2, 1000)

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(expression_data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.xlabel('Expression Level', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Gene Expression', fontsize=14)
plt.axvline(expression_data.mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Mean: {expression_data.mean():.2f}')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()