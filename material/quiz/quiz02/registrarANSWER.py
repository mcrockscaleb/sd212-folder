# Fill in your code here!

import pandas as pd

df = pd.read_csv('courses.csv')
dept = df["Department"].value_counts().index[0]
print(dept)

filtered = df[(df['Department'] == dept) & (df["Course number"] <= 400) & (df["Course number"] >= 300)]
#print(filtered)

print((filtered["Capacity"] - filtered["Enrollment"]).sum())