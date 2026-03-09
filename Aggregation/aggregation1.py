"""
1- Select specific column
2- filter rows
3-combine multiple conditions

1-square brackets
2-boolean conditions

Selecting columns
1- a series
2- dataframe multiple columns of data

column= df["Column Name"]
subset = df["Column1", "Column2","..."]

filtering rows
boolen indexing

#based on a single condition
filtered_rows = df[df["salary"] > 50000 ]

#combine multiple conditions
filtered_rows = df[(df["Column"] > value) & (df["Column2"] < 80000)]
"""


import pandas as pd

data = {
    "Name" : ['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj',' Simran'],
    "Age" : [28,34,22,30,29,40,25,32],
    "Salary": [50000,60000,45000,52000,49000,70000,48000,58000,],
    "Performance_Score": [85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)

#Selection of single columns
print("Single column return series")
name = df['Name']
print(name)

#selecting multiple columns
subset = df[["Name", "Salary"]]
print('\n Subset with name and Salary')
print(subset)

#Single condition filtering

high_salary = df[df['Salary'] > 50000]
print("Employee with salary > 50000")
print(high_salary)

# Multiple condition filtering
filtered = df[(df["Age"] > 30)  & (df["Salary"] > 50000) ]
print(" Employee with age > 30 and salary > 50000")
print(filtered)

# Multiple conditions with OR filtering
filter_or = df[(df["Age"] > 35) | (df["Performance_Score"] > 90) ]
print(" Employee with age > 30 and performance > 90")
print(filter_or)