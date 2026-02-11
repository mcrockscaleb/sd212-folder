import pandas as pd


df = pd.read_csv("times.csv")

grouped = df.groupby("name")["time"].agg(["first", "last"]).reset_index()
"""
> returns a DataFrameGroupBy, not necessarily a DataFrame.
> 

> agg() will give two new columns. first and last are predefined functions inside pandas,
> so you couldn't necessarily use like start and end for example.

> essentially, .agg() will allow you to use multiple aggregaton functions
> at the same time in the groupby function. the only reason it works but looks weird is because
> you used first and last, which are inherent functions and not just strings.

> you can just use .first(), but only because you needed .last() as well, you used .agg()

> df.groupby('Name')['count'].agg(['sum', 'min'])


> use the reset_index() during groupby functions so you can reset the numerical indices of each value
"""


grouped.columns = ["name", "start", "end"]

"""
> currently strings. i want the datetime, so i can fully subtract the time from each value

"""

grouped["start_dt"] = pd.to_datetime(grouped["start"], format="%H:%M:%S")
grouped["end_dt"] = pd.to_datetime(grouped["end"], format="%H:%M:%S")

grouped["timedelta"] = grouped["end_dt"] - grouped["start_dt"]

# print(grouped.sort_values('timedelta'))

# min_time = grouped['elapsed'].min()

"""
> let's find the index of the winner instead of sorting
> using .idxmin()
"""

winner_index = grouped["timedelta"].idxmin()

print(grouped.loc[winner_index, "name"])