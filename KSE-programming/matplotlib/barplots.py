import matplotlib.pyplot as plt

# Gene expression data
genes = ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS']
expression = [5.2, 8.1, 3.4, 9.7, 6.3]
colors = ['red', 'blue', 'green', 'orange', 'purple']

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(genes, expression, color=colors, alpha=0.7, edgecolor='black')

plt.xlabel('Gene', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Expression Comparison', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()