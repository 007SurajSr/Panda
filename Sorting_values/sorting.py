import pandas as pd

data = {
    "Name" : ['Arun', 'Varun', 'Karan'],
    "Age"  : [28,34,22],
    "Salary":[100000, 200000, 300000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending= True, inplace = True)
#df.sort_values(by=["Age", "Salary"], ascending = [True, False], inplace = True)

print(df)