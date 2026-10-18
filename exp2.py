from google.colab import drive
import pandas as pd
import numpy as np

drive.mount('/content/drive')

file_path = "/content/drive/MyDrive/FDS/EXP2.xlsx"

df = pd.read_excel(file_path, engine='openpyxl')

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
