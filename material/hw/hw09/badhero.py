import pandas as pd

df = pd.read_csv('heroes.csv', sep=';')

badheroes = df[(df['Strength'] <= 10) & (df['Intelligence'] == 'low')]

for name in badheroes['Name']:
    print(name)