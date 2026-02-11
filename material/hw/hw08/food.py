# Write your Food and Yogurt classes in this file

class Food:

    total = 0

    def __init__(self, food, meal, calories=0):
        self.food = food
        self.meal = meal
        self.calories = calories

    def info(self):
        print(f"{self.food} is a {self.meal} food with {self.calories} calories")
    
    def eat(self):
        Food.total += self.calories
        print(f"{Food.total} calories so far")
    

    
class Yogurt(Food):
    def __init__(self, flavor, food='yogurt', meal='lunch', calories=150):
        super().__init__(food, meal, calories)
        self.flavor = flavor
        self.food = self.flavor + ' ' + self.food

    def stir(self):
        print(f"Stirring your {self.food}")
