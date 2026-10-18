#==============================================================================
# EXPERIMENT 2
# AIM: Apply descriptive statistical techniques on the given dataset using Python to summarize and interpret the data.
#==============================================================================

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


#==============================================================================
# EXPERIMENT 3
# AIM: Generate and interpret histogram plots using Python to identify distribution patterns in the dataset.
#==============================================================================

from google.colab import drive
import pandas as pd
import matplotlib.pyplot as plt

drive.mount('/content/drive')

file_path = "/content/drive/MyDrive/FDS/EXP2.xlsx"

df = pd.read_excel(file_path, engine='openpyxl')

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


#==============================================================================
# EXPERIMENT 4
# AIM: Apply simple linear regression using Python and analyze the regression output to interpret relationships between variables.
#==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Hours':[1,2,3,4,5,6,7,8,9,10],
    'Marks':[35,40,45,50,55,60,65,70,75,80]
}

df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()


#==============================================================================
# EXPERIMENT 5
# AIM: Perform multiple linear regression using Python and evaluate the regression table to identify significant predictors and understand model accuracy.
#==============================================================================

import pandas as pd
import statsmodels.api as sm

data = {
    'Hours': [2, 3, 4, 5, 6, 7, 2, 4, 6, 8, 3, 7],
    'Attendance': [60, 65, 70, 75, 80, 85, 55, 72, 88, 90, 62, 82],
    'Assignments': [4, 5, 6, 6, 7, 8, 3, 5, 8, 9, 4, 7],
    'Marks': [45, 50, 58, 62, 70, 78, 42, 57, 75, 85, 48, 76]
}

df = pd.DataFrame(data)
print(df)

X = df[['Hours', 'Attendance', 'Assignments']]
y = df['Marks']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print("\nModel Accuracy (R-squared):", round(model.rsquared, 4))

print("\nPredicted Marks:")
print(model.predict(X))


#==============================================================================
# EXPERIMENT 7
# AIM: Apply logistic regression on the given dataset and analyze the regression output to interpret classification results.
#==============================================================================

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = np.array([
    [1, 100],                      
    [2, 150],                      
    [3, 200],
    [5, 250]
])

y = np.array([0, 0, 1, 1])

df = pd.DataFrame(X,y)

print("Dataset:")
print(df)


model = LogisticRegression()

model.fit(X, y)

y_pred = model.predict(X)

new_email = np.array([[4, 180]])
prediction = model.predict(new_email)
probability = model.predict_proba(new_email)

accuracy = accuracy_score(y, y_pred)

print("Prediction (0 = Not Spam, 1 = Spam):", prediction)
print("Probability [Not Spam, Spam]:", probability)

print("\nAccuracy:", accuracy)


