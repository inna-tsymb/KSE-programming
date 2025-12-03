## Part 2: Data Analysis with Orthopedic Dataset (6 points)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# URL for raw CSV
url = 'https://raw.githubusercontent.com/Roit93/Orthopedic-patient-analysis/master/Dataset%20column_3C_weka.csv'
patients = pd.read_csv(url)

### Question 1: Pandas - Data Exploration & Filtering (1 point)

# Part A: Exploration
print("First 5 patients:")
print(patients.head())

print(f"\nDataset shape: {patients.shape}")
print("\nColumn names and data types:")
print(patients.dtypes)

# Part B: Filter severe cases
severe_cases = patients[
    (patients['degree_spondylolisthesis'] > 30) | (patients['pelvic_incidence'] > 70)
]

print(f"\nSevere cases found: {len(severe_cases)}")
print("\nClass distribution of severe cases:")
print(severe_cases['class'].value_counts())

### Question 2: Pandas - Group Analysis (1 point)

# a) Group statistics
diagnosis_stats = patients.groupby('class').agg({
    'degree_spondylolisthesis': 'mean',
    'pelvic_incidence': 'mean',
    'lumbar_lordosis_angle': 'std',
    'class': 'count'
})

# Rename count column
diagnosis_stats.rename(columns={'class': 'count'}, inplace=True)

print("Statistics by Diagnosis:")
print(diagnosis_stats.round(2))

# b) Highest spondylolisthesis
highest_diagnosis = diagnosis_stats['degree_spondylolisthesis'].idxmax()
print(f"\nDiagnosis with highest spondylolisthesis: {highest_diagnosis}")

### Question 3: NumPy - Statistical Analysis (1 point)

# a) NumPy statistics for pelvic_incidence
pelvic_incidence_array = patients['pelvic_incidence'].to_numpy()

mean_pi = np.mean(pelvic_incidence_array)
median_pi = np.median(pelvic_incidence_array)
std_pi = np.std(pelvic_incidence_array)
p25 = np.percentile(pelvic_incidence_array, 25)
p75 = np.percentile(pelvic_incidence_array, 75)

print("Pelvic Incidence Statistics:")
print(f"Mean: {mean_pi:.2f}")
print(f"Median: {median_pi:.2f}")
print(f"Std Dev: {std_pi:.2f}")
print(f"25th percentile: {p25:.2f}")
print(f"75th percentile: {p75:.2f}")

# b) Z-score normalization for degree_spondylolisthesis
spondylo_array = patients['degree_spondylolisthesis'].to_numpy()

spondylo_mean = np.mean(spondylo_array)
spondylo_std = np.std(spondylo_array)
spondylo_zscore = (spondylo_array - spondylo_mean) / spondylo_std

# Add z-score column to DataFrame
patients['spondylo_zscore'] = spondylo_zscore

# Count outliers (|z-score| > 2)
outliers = np.abs(spondylo_zscore) > 2
num_outliers = np.sum(outliers)

print(f"\nNumber of outliers (|z-score| > 2): {num_outliers}")
print(f"Percentage of outliers: {(num_outliers/len(patients)*100):.1f}%")

### Question 4: Matplotlib - Visualization (1.5 points)

# Create figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Histogram of degree_spondylolisthesis
axes[0].hist(patients['degree_spondylolisthesis'], bins=30,
             color='skyblue', edgecolor='black', alpha=0.7)
mean_spondylo = patients['degree_spondylolisthesis'].mean()
axes[0].axvline(mean_spondylo, color='red', linestyle='--', linewidth=2,
                label=f'Mean: {mean_spondylo:.1f}')
axes[0].set_xlabel('Degree of Spondylolisthesis', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].set_title('Distribution of Spondylolisthesis', fontsize=14)
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Plot 2: Box plot of pelvic_incidence by diagnosis
diagnosis_groups = [
    patients[patients['class'] == 'Normal']['pelvic_incidence'],
    patients[patients['class'] == 'Hernia']['pelvic_incidence'],
    patients[patients['class'] == 'Spondylolisthesis']['pelvic_incidence']
]

bp = axes[1].boxplot(diagnosis_groups,
                     labels=['Normal', 'Hernia', 'Spondylolisthesis'],
                     patch_artist=True)
colors = ['lightgreen', 'orange', 'lightcoral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

axes[1].set_ylabel('Pelvic Incidence (degrees)', fontsize=12)
axes[1].set_xlabel('Diagnosis', fontsize=12)
axes[1].set_title('Pelvic Incidence by Diagnosis', fontsize=14)
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', alpha=0.3)

# Plot 3: Scatter plot pelvic_incidence vs degree_spondylolisthesis
colors_map = {'Normal': 'green', 'Hernia': 'orange', 'Spondylolisthesis': 'red'}
for diagnosis in patients['class'].unique():
    diagnosis_data = patients[patients['class'] == diagnosis]
    axes[2].scatter(diagnosis_data['pelvic_incidence'],
                    diagnosis_data['degree_spondylolisthesis'],
                    c=colors_map[diagnosis],
                    label=diagnosis,
                    alpha=0.6,
                    s=50,
                    edgecolors='black',
                    linewidth=0.5)

axes[2].set_xlabel('Pelvic Incidence (degrees)', fontsize=12)
axes[2].set_ylabel('Degree of Spondylolisthesis', fontsize=12)
axes[2].set_title('Pelvic Incidence vs Spondylolisthesis', fontsize=14)
axes[2].legend(title='Diagnosis')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('orthopedic_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

### Question 5: Pandas - Correlation & Complex Query (0.75 points)

# Part A: Correlation matrix
numeric_data = patients.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()

print("Correlation Matrix:")
print(correlation_matrix.round(3))

# Find strongest positive correlation (excluding diagonal)
corr_pairs = correlation_matrix.unstack()
# Remove self-correlations
corr_pairs = corr_pairs[corr_pairs < 0.999]
# Sort by correlation value
sorted_corr = corr_pairs.sort_values(ascending=False)
strongest_pair = sorted_corr.index[0]
strongest_value = sorted_corr.iloc[0]

print(f"\nStrongest positive correlation: {strongest_pair} = {strongest_value:.3f}")

# Part B: Complex filtering
specific_patients = patients[
    (patients['pelvic_incidence'].between(50, 70)) &
    (patients['degree_spondylolisthesis'] > 20) &
    (patients['class'] == 'Spondylolisthesis')
]

print(f"\nPatients matching criteria: {len(specific_patients)}")
print(f"Percentage of total: {(len(specific_patients)/len(patients)*100):.1f}%")

### Question 6: Pandas - Summary Report Creation (0.75 points)

# a) Create abnormal flag
patients['abnormal'] = patients['class'].isin(['Hernia', 'Spondylolisthesis'])

print(f"Normal patients: {(~patients['abnormal']).sum()}")
print(f"Abnormal patients: {patients['abnormal'].sum()}")

# b) Compare Normal vs Abnormal groups
comparison = patients.groupby('abnormal').agg({
    'pelvic_incidence': 'mean',
    'pelvic_tilt': 'mean',
    'lumbar_lordosis_angle': 'mean',
    'sacral_slope': 'mean',
    'pelvic_radius': 'mean',
    'degree_spondylolisthesis': 'mean'
})

# Add patient count
comparison['patient_count'] = patients.groupby('abnormal').size()

print("\nNormal vs Abnormal Comparison:")
print(comparison.round(2))

# Which feature differs most?
differences = comparison.loc[True] - comparison.loc[False]
biggest_diff = differences.drop('patient_count').abs().idxmax()

print(f"\nFeature with biggest difference: {biggest_diff}")
print(f"Difference: {differences[biggest_diff]:.2f}")

