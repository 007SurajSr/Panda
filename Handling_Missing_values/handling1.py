"""
NaN (Not a Number)
Nonw (For object data types)

isnull()
True - NaN is missing
False - value is prese

df.dropna(axis = 1, inplace= True)
Axis = 1 (remove values from colums)
Axis = 0 (remove values from rows)

"""
import pandas as pd

data = {
    "Name" : ['Ram',None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj',' Simran'],
    "Age" : [28,None,22,30,29,40,25,32],
    "Salary": [50000,60000,None,52000,49000,70000,48000,58000,],
    "Performance Score": [85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)


df.dropna(inplace=True)
print(df)