# Set grades score ranges
grade_A_threshold = 90
grade_B_threshold = 80
grade_C_threshold = 70
grade_D_threshold = 60

# Set function to assign letter grades based on score   
def get_letter_grade(score):
    """
    Convert a numeric score to a letter grade.
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: below 60

    Parameters:
    score (float): The numeric score (0-100).

    Returns:
    str: The corresponding letter grade (A, B, C, D, F).
    """
    if score >= grade_A_threshold:
        return 'A'
    elif score >= grade_B_threshold:
        return 'B'
    elif score >= grade_C_threshold:
        return 'C'
    elif score >= grade_D_threshold:
        return 'D'
    else:
        return 'F'
    
# Test cases
if __name__ == "__main__":
    test_scores = [95, 85, 75, 65, 55, 100, 0, 89.5, 70.2]
    for score in test_scores:
        result = get_letter_grade(score)
        print(f"Score: {score} => Grade: {result}")