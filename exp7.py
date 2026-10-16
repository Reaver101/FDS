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