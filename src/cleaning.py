#!/usr/bin/env python3
"""
Stroke Data Cleaning Pipeline
CRABS Summer School 2025

Usage: python clean_stroke_data.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    """Main data cleaning pipeline"""
    print("🧹 Starting Data Cleaning Pipeline")
    print("=" * 35)
    
    # Load data
    df = pd.read_csv('/Users/user/Desktop/python/data/raw/healthcare-dataset-stroke-data.csv')
    
    # Run all cleaning steps...
    # (Add all the cleaning code here)
    
if __name__ == "__main__":
    main()

    # Check BMI missing pattern
print("🔍 BMI Missing Data")
missing_bmi = df['bmi'].isnull().sum()
print(f"Missing: {missing_bmi} ({missing_bmi/len(df)*100:.1f}%)")

# Fill with median (robust strategy)
median_bmi = df['bmi'].median()
df_clean = df.copy()
df_clean['bmi'].fillna(median_bmi, inplace=True)

print(f"✅ Filled with median: {median_bmi:.1f}")