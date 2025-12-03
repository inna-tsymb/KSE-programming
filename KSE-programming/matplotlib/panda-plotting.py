import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS'],
    'Expression': [5.2, 8.1, 3.4, 9.7, 6.3]
})

# Plot directly from DataFrame
df.plot(x='Gene', y='Expression', kind='bar', figsize=(10, 6), 
        legend=False, color='steelblue', edgecolor='black')

plt.xlabel('Gene', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Expression', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()