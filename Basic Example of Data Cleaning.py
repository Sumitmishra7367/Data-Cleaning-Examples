import pandas as pd
import numpy as np

# Step 1: Raw data
data = {
    'Name': ['Amit ', 'Sita', 'Ram', 'Sita', None],
    'Age': [20, 25, None, 25, 30],
    'City': ['Delhi', ' delhi', 'Mumbai', 'Delhi', 'Kolkata']
}

df = pd.DataFrame(data)

print("🔹 RAW DATA")
print(df)

# Step 2: Cleaning
df['Name'] = df['Name'].str.strip().fillna("Unknown")   # strip spaces + fill missing
df['Age'] = df['Age'].fillna(df['Age'].mean())          # fill missing with mean
df['City'] = df['City'].str.strip().str.lower()         # strip + lowercase
df.drop_duplicates(inplace=True)                        # remove duplicates

print("\n✅ CLEANED DATA")
print(df)
