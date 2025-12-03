import pandas as pd
import matplotlib.pyplot as plt

# Create data
genes = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS'],
    'Control': [4.1, 5.2, 3.1, 6.5, 4.8],
    'Treated': [5.2, 8.1, 3.4, 9.7, 6.3]
})
# Create bar plot comparing control vs treated
genes.set_index('Gene').plot(kind='bar', figsize=(10, 6), alpha=0.7, edgecolor='black') 
plt.xlabel('Gene', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Expression: Control vs Treated', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Condition')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Save the figure
plt.savefig('gene_expression_comparison.png')   