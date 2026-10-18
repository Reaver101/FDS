import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
})

print("First 5 Rows:")
print(df.head())

print("\nDataset:")
print(df)

df.columns = df.columns.str.strip()

print(df.head())

plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=5)

plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
