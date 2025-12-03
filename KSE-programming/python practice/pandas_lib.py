import pandas as pd

# Create DataFrame
genes = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS'],
    'Control': [4.1, 5.2, 3.1, 6.5, 4.8],
    'Treated': [5.2, 8.1, 3.4, 9.7, 6.3]
})

# Calculate fold change
genes['Fold_Change'] = genes['Treated'] / genes['Control']

# Find upregulated genes (FC > 1.5)
upregulated = genes[genes['Fold_Change'] > 1.5]

# Print results
print(upregulated)