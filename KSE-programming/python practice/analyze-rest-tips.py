import pandas as pd

# Load data
tips = pd.read_csv('tips.csv')

# Your tasks:
# 1. Find the day with highest average bill
best_day = tips.groupby('day')['total_bill'].mean().idxmax()
print(f"Best day: {best_day}")

# 2. Calculate total tips per day
daily_tips = tips.groupby('day')['tip'].sum()
print(daily_tips)

# 3. Count how many tables had 2 people
two_people = (tips['size'] == 2).sum()
print(f"Tables with 2 people: {two_people}")

# 4. Find average tip percentage by day
tips['tip_pct'] = tips['tip'] / tips['total_bill'] * 100
avg_tip_pct = tips.groupby('day')['tip_pct'].mean()
print(avg_tip_pct)