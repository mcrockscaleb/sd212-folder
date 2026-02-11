# SD212 Quiz 04: Hot Dog Eating Contest

## Scenario

Write a class `Eater` to manage contestants in a hot dog eating contest.
Your class will keep track of the name or names of the contestants, and
how many hot dogs they ate. You will overload the + operator to combine
two contestants together.

Specifically your class should have three methods:

*   A constructor `__init__` which takes the contestant's name and how
    many dogs they ate

*   An overloaded `__add__` method to perform the + operation on two
    Eater instances and **return a new instance of the Eater class**.
    The new Eater's name should be the original names with " and " in
    between, and the new Eater's dog count should be the sum of the
    original ones.

*   An overloaded `__str__` method used by the print() function
    to display a line like "NAME ate COUNT"

## Example usage

For example if I run this code:

    from eater import Eater

    joey = Eater("Joey", 62)
    miki = Eater("Miki", 51)
    print(joey)           # Joey ate 62
    jm = joey + miki
    print(jm)             # Joey and Miki ate 113
    print(miki)           # Miki ate 51
    domenica = Eater("Domenica", 30)
    print(jm + domenica)  # Joey and Miki and Domenica ate 143

That should display these four lines to the terminal:

    Joey ate 62
    Joey and Miki ate 113
    Miki ate 51
    Joey and Miki and Domenica ate 143

## Commands to submit

    club -csd212 -pquiz04 eater.py

    submit -c=sd212 -p=quiz04 eater.py
