## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[["gpa"]])
admissions["predicted_label"] = labels
print(admissions["predicted_label"].value_counts())
print(admissions.head())

## 2. Accuracy ##

admissions = admissions.rename(axis=1,mapper={"admit":"actual_label"})
matches = admissions["actual_label"] == admissions["predicted_label"]
correct_predictions = admissions.loc[matches==True]
print(correct_predictions.head())
accuracy = matches.sum() / admissions.shape[0]
print(accuracy)

## 4. Binary classification outcomes ##

true_positives = admissions.loc[(admissions["predicted_label"]==admissions["actual_label"])&(admissions["predicted_label"]==1)]
true_negatives = admissions.loc[(admissions["predicted_label"]==admissions["actual_label"])&(admissions["predicted_label"]==0)]
print(true_positives)
print(true_negatives)

## 5. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_negatives = len(admissions.loc[(admissions["actual_label"]!=admissions["predicted_label"])&(admissions["actual_label"]==1)])

sensitivity = true_positives/(false_negatives+true_positives)

## 6. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

false_positives = len(admissions.loc[(admissions["predicted_label"]!=admissions["actual_label"])&(admissions["actual_label"]==0)])

specificity = true_negatives / (false_positives+true_negatives)

