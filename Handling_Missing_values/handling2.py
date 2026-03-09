import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'Age': [25, 30, None, 40, None],
    'Salary': [50000, None, 60000, None, 70000]
})

# Fill missing values with mean directly
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print(df)
