# caleb chau
# sd212 // gentile
# hw02
# 1/8

import pandas as pd
import datetime

# i read in the csv file and then converted the df into a datetime object
df = pd.read_csv("times.csv")
df["time"] = pd.to_datetime(df["time"], format="%H:%M:%S")

# using groupby, i made a new column in the df that took the difference of duplicated times accoring to their duplicated bibs
df["final"] = df.groupby("bib")["time"].diff()

# sorted the list based on the lowest df['final'] time
sort = df.sort_values(by="final")

# get only the first index, of the name column, which is ChristianBale
print(sort.iloc[0]["name"])

