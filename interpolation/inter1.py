# 10
# 20
# Nan = 30
# 40
# 50

# 1000
# 2000
# 3000
# 4000
# 5000

# Liner 

# 1- preserve data integrity
# 2- smooth trends
# 3- avoid data loss

# interpolate()

import pandas as pd

data = {
    "Name" : ['Ram','Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj',' Simran'],
    "Age" : [28,None,22,30,29,40,25,32],
    "Salary": [50000,60000,None,52000,49000,70000,48000,58000,],
    "Performance_Score": [85,None,78,92,88,95,80,89]
}

print("Before interpolation:")
print(df)

numeric_cols = df.select_dtypes(include=['number']).columns

# Interpolate missing numerical values
df[numeric_cols] = df[numeric_cols].interpolate(method="linear", axis=0)
print("\nAfter interpolation:")
print(df)