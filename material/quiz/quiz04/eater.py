# YOU FILL THIS IN

class Eater:
    def __init__(self, name, ate=0):
        self.name = name
        self.ate = ate

    def __add__(self, other):
        total_ate = self.ate + other.ate
        return Eater(self.name + " and " + other.name, total_ate)

    def __str__(self):
        return f"{self.name} ate {self.ate}"