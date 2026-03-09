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

grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)