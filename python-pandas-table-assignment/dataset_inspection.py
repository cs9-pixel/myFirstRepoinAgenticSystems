import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen"],
    "Age": [21, 22, 20, 23, 21, 24, 22, 23],
    "Score": [85, 78, 92, 88, 76, 95, 81, 89],
    "Label": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)


df.to_csv("students.csv", index=False)


df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())


age_column = df["Age"]
print("\nAge Column:")
print(age_column)


subset = df[["Name", "Score"]]
print("\nSelected Columns (Name, Score):")
print(subset)


filtered = df[df["Score"] > 80]
print("\nFiltered rows (Score > 80):")
print(filtered)
