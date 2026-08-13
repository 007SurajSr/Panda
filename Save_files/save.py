import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
print(df)

# Save to CSV
df.to_csv("Output.csv", index=False)

# Save to Excel (requires 'openpyxl') #pip install openpyxl
df.to_excel("Output.xlsx", index=False)

# Save to JSON (use orient='records' for a clean list of objects)
df.to_json("Output.json", orient="records", indent=4)