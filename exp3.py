# Import libraries
from google.colab import drive
import pandas as pd
import matplotlib.pyplot as plt

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

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display dataset
print(df.head())

# Generate Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=5)

# Add title and labels
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Show plot
plt.show()