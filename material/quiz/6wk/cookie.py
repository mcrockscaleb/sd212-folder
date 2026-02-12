# FILL THIS IN WITH YOUR SOLUTION TO PROBLEM 2

class CookieJar:

    stolen = 0

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def steal(self, value):
        self.amount = self.amount - value
        CookieJar.stolen = CookieJar.stolen + value

    def total_stolen(self):
        return CookieJar.stolen
    
    def __str__(self):
        return f"{self.name}: {self.amount} cookies"