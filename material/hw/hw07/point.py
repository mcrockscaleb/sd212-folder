# Write your Point class in this file

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point(new_x, new_y)

    def __truediv__(self, other):
        new_x = self.x * other.y
        new_y = self.y * other.x
        
        return Point(new_x, new_y)

    def __str__(self):
        return f"({self.x},{self.y})"