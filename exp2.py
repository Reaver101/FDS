# Import libraries
from google.colab import drive
import pandas as pd
import numpy as np

# Mount Google Drive
drive.mount('/content/drive')

# Read the Excel file
file_path = "/content/drive/MyDrive/FDS/EXP2.xlsx"

df = pd.read_excel(file_path, engine='openpyxl')

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display complete dataset
print("\nDataset:")
print(df)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Select the Marks column
marks = df["Marks"]

# Mean
print("\nMean:")
print(marks.mean())

# Median
print("\nMedian:")
print(marks.median())

# Mode
print("\nMode:")
print(marks.mode())

# Minimum
print("\nMinimum:")
print(marks.min())

# Maximum
print("\nMaximum:")
print(marks.max())

# Range
print("\nRange:")
print(marks.max() - marks.min())

# Variance
print("\nVariance:")
print(marks.var())

# Standard Deviation
print("\nStandard Deviation:")
print(marks.std())