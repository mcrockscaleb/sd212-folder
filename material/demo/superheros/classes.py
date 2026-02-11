from csv import DictReader

class Hero:

    #defaults everyone to team avengers
    team = "avengers"

    def __init__(self, name, identity, strength):
        self.name = name
        self.identity = identity
        self.strength = strength

    def display(self):
        print(f"{self.name} ({self.identity})")

    def stronger(self, other_hero):
        return self.strength > other_hero.strength
    
heroes = {}

for row in DictReader(open('heroes.csv'), delimiter = ';'):
    if row['Strength'] == '':
        continue
    heroes[row['Name']] = Hero(row['Name'], ['Identity'], ['Strength'])

