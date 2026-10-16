"""
-----------------------------------EXP5----------------------------
Aim: To perform multiple linear regression using Python and evaluate the regression table to identify significant predictors and understand model accuracy.
"""
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

"""
-------------------------------EXP7------------------------------
Aim: To apply Logistic Regression on a dataset and analyze the classification results
"""
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

new_email = np.array([[4, 180]])  # 4 suspicious words, length 180
prediction = model.predict(new_email)
probability = model.predict_proba(new_email)

accuracy = accuracy_score(y, y_pred)

print("Prediction (0 = Not Spam, 1 = Spam):", prediction)
print("Probability [Not Spam, Spam]:", probability)

print("\nAccuracy:", accuracy)