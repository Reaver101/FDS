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