# FILL THIS IN WITH YOUR SOLUTION TO PROBLEM 1

import pandas as pd

df = pd.read_csv("movies.csv")
numbers = []

comedies = df[df["genre"] == "Comedy"]

revenue = comedies["revenue"].sum()
budget = comedies["budget"].sum()

print(revenue - budget)
