import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
})

print("First 5 Rows:")
print(df.head())

print("\nDataset:")
print(df)

print("\nColumn Names:")
print(df.columns)

print("\nDescriptive Statistics:")
print(df.describe())

marks = df["Marks"]

print("\nMean:")
print(marks.mean())

print("\nMedian:")
print(marks.median())

print("\nMode:")
print(marks.mode())

print("\nMinimum:")
print(marks.min())

print("\nMaximum:")
print(marks.max())

print("\nRange:")
print(marks.max() - marks.min())

print("\nVariance:")
print(marks.var())

print("\nStandard Deviation:")
print(marks.std())
