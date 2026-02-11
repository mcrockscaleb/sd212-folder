# Your name: Caleb Chau

# Fill in your code below!
# Be sure to test and submit it and make sure it passes every test case.

import pandas as pd

df = pd.read_csv('inventory.csv')

#print(df[['item_name','price','quantity']])

total = 0

restock = df[df['quantity'] == 0]
total = restock['price'] * 10


print(total.sum())
#print(4.57 * 10 + 2 * 10 + 0.3 * 10)