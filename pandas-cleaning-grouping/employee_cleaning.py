import pandas as pd
import numpy as np

# Create dataset
data = {
    "Employee": ["Amit", "Neha", "Rahul", "Sneha", "Vikram", "Priya", "Arjun", "Divya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [600000, 500000, np.nan, 700000, 520000, np.nan, 650000, 480000],
    "Temporary_Notes": ["On probation", "Contract", "Pending docs", "Verified",
                        "Intern", "New joiner", "On leave", "Temporary role"]
}

df = pd.DataFrame(data)


print("Missing Values:\n", df.isnull().sum())


df["Salary"].fillna(df["Salary"].mean(), inplace=True)


df.drop("Temporary_Notes", axis=1, inplace=True)


df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)


result = df.groupby("Department").agg({
    "Annual_Salary": "mean",
    "Employee": "count"
})


result.rename(columns={"Employee": "Employee_Count"}, inplace=True)


print("\nFinal Summary:\n", result)
