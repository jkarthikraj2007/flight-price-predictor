import pandas as pd

# Load the dataset
df = pd.read_csv("data/Clean_Dataset.csv")

# Preview the data
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nAny missing values?")
print(df.isnull().sum())