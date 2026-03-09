#head()  and tail()
#head(n) -- n number of head
#tail(n) -- n number of tails

#Defauld 5 rows will be visible

import pandas as pd

df = pd.read_json("file.json")

print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))