"""
Other Grouping method methods

1- sum()
2- mean()
3- count()
4- min()
5- max()
6- std()

"""



import pandas as pd

data = {
    "Name" : ['Arun', 'Varun', 'Karan', 'Tarun', "Marun"],
    "Age"  : [28, 34, 22, 34, 28],
    "Salary": [100000, 200000 , 300000, 520000, 480000]

}

df = pd.DataFrame(data)

grouped1 = df.groupby(["Age","Name"])["Salary"].sum()
grouped2 = df.groupby(["Age","Name"])["Salary"].mean()
grouped3 = df.groupby(["Age","Name"])["Salary"].count()
grouped4 = df.groupby(["Age","Name"])["Salary"].min()
grouped5 = df.groupby(["Age","Name"])["Salary"].max()
grouped6 = df.groupby(["Age","Name"])["Salary"].std()

print(grouped1)
print(grouped2)
print(grouped3)
print(grouped4)
print(grouped5)
print(grouped6)

