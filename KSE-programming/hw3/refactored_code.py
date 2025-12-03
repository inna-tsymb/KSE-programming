## Part 1: Code Refactoring (4 points)

### Task: Clean Up This Messy Code

## A colleague wrote this code to analyze gene expression data, 
# but it's difficult to understand and maintain. 
# Refactor it following clean code principles.

### Requirements for refactoring (4 points total):

##**1. Descriptive names (1 point):**
#- Replace cryptic variable names (a, d, r, x, y, cnt1, cnt2, f)
#- Use meaningful function names
#- Variables should explain their purpose

#**2. Remove magic numbers (0.5 points):**
#- Define constants for the age threshold (50)
#- Use named constants at the top of your code
#- Constants should be UPPERCASE

#**3. Split into functions (1.5 points):**
#- One function should load data
#- One function should find responsive patients
#- One function should calculate survival statistics
#- Main function coordinates these

#**4. Add documentation (0.5 points):**
#- Docstrings for all functions
#- Explain parameters and return values

#**5. Better pandas usage (0.5 points):**
#- Replace `.iloc` loops with pandas filtering
#- Use `.groupby()` where appropriate
#- Avoid iterating over rows when possible

### Submission for Part 1:
#- Submit file: `refactored_code.py`
#- Code should be clean, readable, and follow PEP 8

import pandas as pd

# Constants
AGE_THRESHOLD = 50
CANCER_TYPE_LUNG = 'Lung'
TREATMENT_A = 'Treatment_A'
CONTROL_TREATMENT = 'Control' 


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load clinical trial patient data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the patient data.
    """
    return pd.read_csv(file_path)

def find_responsive_patients(data: pd.DataFrame) -> list:
    """
    Identify patients who are responsive to treatment.

    A patient is considered responsive if they are aged 50 or older,
    have lung cancer, and their final tumor size is smaller than their baseline tumor size.

    Parameters:
    data (pd.DataFrame): DataFrame containing the patient data.

    Returns:
    list: List of patient IDs who are responsive to treatment.
    """
    responsive_patients = data[
        (data['age'] >= AGE_THRESHOLD) &
        (data['cancer_type'] == CANCER_TYPE_LUNG) &
        (data['final_tumor_size'] < data['baseline_tumor_size'])
    ]['patient_id'].tolist()
    
    return responsive_patients

def calculate_survival_statistics(data: pd.DataFrame) -> None:
    """
    Calculate and print average survival months for different treatment groups.

    Parameters:
    data (pd.DataFrame): DataFrame containing the patient data.
    """
    survival_stats = data.groupby('treatment')['survival_months'].mean()
    
    avg_survival_treatment_a = survival_stats.get(TREATMENT_A, 0)
    avg_survival_control = survival_stats.get(CONTROL_TREATMENT, 0)
    """
    Returns:
    pd.DataFrame: DataFrame containing average survival months per treatment group.
    """
    print("Avg survival Treatment A:", avg_survival_treatment_a)
    print("Avg survival Control:", avg_survival_control)

def analyze_clinical_trial(file_path: str) -> list:
    """
    Analyze clinical trial data to find responsive patients and calculate survival statistics.

    Parameters:
    file_path (str): The path to the CSV file containing patient data.

    Returns:
    list: List of patient IDs who are responsive to treatment.
    """
    data = load_data(file_path)
    responsive_patients = find_responsive_patients(data)
    calculate_survival_statistics(data)
    
    print("Responsive patients:", len(responsive_patients))
    
    return responsive_patients

result = analyze_clinical_trial("clinical_trial_patients.csv")
# Returns:
#    list: List of patient IDs who are responsive to treatment and survival statistics.



