import pandas as pd 

#read data from a CSV file into a dataform

#df = pd.read_csv("employee_data.csv", encoding= "utf-8")
#df1 = pd.read_csv("employee_data.csv", encoding = "latin1")

#To read the excel file

#df = pd.read_excel("Inventory_Records.xlsx")

# To read the Json file

#df = pd.read_json("file.json")

#gcsfs

df = pd.gcsfs("https://drive.google.com/file/d/1OCx6hZn6XGQJL6gNpL5ZMGo6nBkXYz1n/view")
print(df)