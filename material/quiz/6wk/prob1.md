# SD212 6wk Practicum Problem 1: Movie Profits

## Scenario

You have been hired as a data analyst for a major Hollywood studio. The
executives want to understand which genres are actually making money,
rather than just generating high revenue.

Specifically, they want you to calculate the total **profit** generated
by all movies in the **Comedy** genre.

## The Data

The movie data is in a file called `movies.csv`. Each row contains the
movie title, the genre, the production budget (cost), and the box office
revenue (earnings).

**Example `movies.csv` content:**

    title,genre,budget,revenue
    Barbie,Comedy,145000000,1446000000
    Dune: Part Two,Sci-Fi,190000000,711000000
    Anyone But You,Comedy,25000000,220000000
    Oppenheimer,Drama,100000000,975000000

## Example Calculation

Based on the sample data above, we need to filter for **"Comedy"** and
then calculate `revenue - budget` for each matching movie.

1.  **Barbie** (Comedy):
    $1,446,000,000 (Revenue) - $145,000,000 (Budget) = **$1,301,000,000** Profit

2.  **Anyone But You** (Comedy):
    $220,000,000 (Revenue) - $25,000,000 (Budget) = **$195,000,000** Profit

* (Note: *Dune* and *Oppenheimer* are ignored because they are not Comedies.)

**Total Comedy Profit:**
1,301,000,000 + 195,000,000 = **1,496,000,000**

**What your program would print:**

    1496000000

## Your Task

Write a Python program `profits.py` that reads a file called `movies.csv`
and prints out the total profit of all Comedy movies, as a single
number.

Make sure your code works on any `movies.csv` file formatted as above,
not just this one specific example.

## Commands to submit

    club -csd212 -p6wkp1 profits.py

    submit -c=sd212 -p=6wkp1 profits.py
