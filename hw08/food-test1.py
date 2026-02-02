# This program is used to test your code.
# It will not be submitted; you can change it if you want to
# do more tests!

from food import Food, Yogurt

bagel = Food('bagel', 'breakfast', 350)
pizza = Food('pizza', 'dinner', 800)
lemyo = Yogurt('lemon')
plainyo = Yogurt('plain')

bagel.info()   # prints "bagel is a breakfast food with 350 calories"
pizza.info()   # prints "pizza is a dinner food with 800 calories"
lemyo.info()   # prints "lemon yogurt is a lunch food with 150 calories"
plainyo.info() # prints "plain yogurt is a lunch food with 150 calories"

bagel.eat()    # prints "350 calories so far"
lemyo.stir()   # prints "Stirring your lemon yogurt"
lemyo.eat()    # prints "500 calories so far"
pizza.eat()    # prints "1300 calories so far"
plainyo.stir() # prints "Stirring your plain yogurt"
plainyo.eat()  # prints "1450 calories so far"
