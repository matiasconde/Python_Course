## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt

admissions = pd.read_csv("admissions.csv")

plt.scatter(admissions["gpa"],admissions["admit"])
plt.show()

## 4. Logistic function ##

import numpy as np

# Logistic Function
def logistic(x):
    return np.exp(x)  / (1 + np.exp(x)) 
    
# Generate 50 real values, evenly spaced, between -6 and 6.
x = np.linspace(-6,6,50, dtype=float)

# Transform each number in t using the logistic function.
y = logistic(x)

# Plot the resulting data.
plt.plot(x, y)
plt.ylabel("Probability")
plt.show()

## 5. Training a logistic regression model ##

from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()

logistic_model.fit(admissions[["gpa"]], admissions["admit"])



## 6. Plotting probabilities ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

pred_probs = logistic_model.predict_proba(admissions[["gpa"]])

x_values = admissions["gpa"]
y_values = pred_probs[:,1]

plt.scatter(x_values,y_values)
plt.show()

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
fitted_labels = logistic_model.predict(admissions[["gpa"]])
plt.scatter(admissions["gpa"],fitted_labels)
plt.show()
admissions["predicted"] = fitted_labels
print(admissions.shape)
print(admissions.head(50))
print(admissions["admit"].value_counts())
print(admissions["predicted"].value_counts())