# This is tester code.
# It will not be submitted, so you can modify it if you want.
from point import Point

p1 = Point(3,4)
p2 = Point(5,0)
print(p1)       # displays "(3,4)"
p3 = p1 + p2
print(p3)       # displays "(8,4)"
print(p1)       # still "(3,4)"
print(p2/2)     # displays "(2.5,0)"
midpoint = (p1 + p2) / 2
print(midpoint) # displays "(4,2)"
