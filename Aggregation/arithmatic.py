"""
df["column_name].mean()
df["column_name].sum()
df["column_name].min()
df["column_name].max()

"""

import pandas as pd

data = {
    "Name" : ['Arun', 'Varun', 'Karan'],
    "Age"  : [28, 334, 22],
    "Salary": [10000, 20000 , 30000]

}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
sum_salary = df['Salary'].sum()
min_salary = df['Salary'].min()
max_salary = df['Salary'].max()

print(avg_salary)
print(sum_salary)
print(min_salary)
print(max_salary)