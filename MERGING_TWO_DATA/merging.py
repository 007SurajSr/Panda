#pd.merge(df1, df2, on="Column_name", how= "type of join")

import pandas as pd

#customer dataframe

df_customers = pd.DataFrame({
    "CustomerID" : [1,2,3],
    "name"  : ['Ramesh', 'Suresh', 'Kalpesh']
})

#order dataFrame
df_orders = pd.DataFrame({
    "CustomerID" : [1, 2, 4],
    "orderAmmount": [250, 450, 350]
})

# merge

df_merge = pd.merge(df_customers, df_orders, on = "CustomerID",  how = "inner")

# outer, right, left
print('Inner Join')
print(df_merge)