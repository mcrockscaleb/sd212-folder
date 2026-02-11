# Fill in your code here!

import pandas as pd

df = pd.read_csv('courses.csv')
mostOffered = df["Department"].value_counts(ascending=False).idxmax()
print(mostOffered)

offered = df['Department'] == mostOffered
course = (df["Course number"] <= 400) & (df["Course number"] >= 300)
filtered = df[course & offered]
#print(filtered)

spots = (filtered["Capacity"] - filtered["Enrollment"])
print(spots.sum())