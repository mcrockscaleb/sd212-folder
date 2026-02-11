# THIS FILE IS USED TO TEST YOUR CODE
# You do not need to change it, but you can if you want.

from eater import Eater

joey = Eater("Joey", 62)
miki = Eater("Miki", 51)
print(joey)           # Joey ate 62
jm = joey + miki
print(jm)             # Joey and Miki ate 113
print(miki)           # Miki ate 51
domenica = Eater("Domenica", 30)
print(jm + domenica)  # Joey and Miki and Domenica ate 143
