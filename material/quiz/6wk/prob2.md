# SD212 6wk Practicum Problem 2: Cookie Monster

## Scenario

Write software to manage a kitchen with several cookie jars.
You need to track how many cookies are in each specific jar, but you
also need to track a "Cookie Monster" who is stealing cookies from
all of them.

## Your task

Write a class `CookieJar` in a file named `cookie.py` with the
following methods:

*   A constructor that takes the owner's
    name and the number of cookies initially in the jar.

*   `steal`: A method that takes an integer n. It should remove
    n cookies from this specific jar **and** update a running total
    of cookies stolen from all jars combined.

*   `total_stolen`: Returns the total number of cookies stolen
    from all jars combined so far.

*   `__str__()`: Returns a string formatted like "OWNER: COUNT cookies"

## Example usage

For example if I run this code:

    from cookie import CookieJar

    # Setup two different jars
    bert = CookieJar("Bert", 10)
    ernie = CookieJar("Ernie", 20)

    print(bert)
    print(ernie)

    # Steal from Bert
    bert.steal(2)
    print(bert)
    print(f"Monster has {bert.total_stolen()} cookies")

    # Steal from Ernie (Should update the SAME global counter)
    ernie.steal(5)
    print(ernie)
    print(f"Monster has {ernie.total_stolen()} cookies")

    # Steal from Bert AGAIN
    bert.steal(3)
    print(bert)
    print(f"Monster has {bert.total_stolen()} cookies")

That should display these lines to the terminal:

    Bert: 10 cookies
    Ernie: 20 cookies
    Bert: 8 cookies
    Monster has 2 cookies
    Ernie: 15 cookies
    Monster has 7 cookies
    Bert: 5 cookies
    Monster has 10 cookies

## Commands to submit

    club -csd212 -p6wkp2 cookie.py

    submit -c=sd212 -p=6wkp2 cookie.py
