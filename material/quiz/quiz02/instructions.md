# SD212 Quiz 02: Course registrar

## Scenario

You are the USNA registrar and have information on the currently offered
courses, which department and school they are in, what is their course
number, and what is their enrollment and capacity.

You trying to answer two specific question:

1.  Find which **department** offers the most **number of courses**

2.  For that department, how many **empty seats** are there in its
    **300-level courses**?

    (Where "empty seats" is defined as the capacity minus enrollment.)

You want to write a Python program that will print out two lines
answering these two questions.

## The Data

The course data is in a file called `courses.csv` which you can find in
this directory.

## Example calculation

For the sample file you are given, **History** has 4 courses, which is
the most of any single department.

In that file, the History department has 2 300-level courses,
represented by these two rows:

    Humanities,History,350,Naval History,19,22
    Humanities,History,360,Cold War,15,22

The first one has 22-19=3 empty seats, and the second one has 22-15=7
empty seats. So the total number of empty seats in 300-level courses is
3+7=10. There are **10** empty seats in 300-level History courses.

The output of your program should therefore be:

    History
    10

## Your Task

Write a Python program `registrar.py` that reads the `courses.csv` file
and prints the department name with the most number of courses,
followed by the total unused capacity for 300-level courses in that
department.

Your program should just print these two values on two lines,
with no other output.

You can use any method to accomplish this in Python, but it should work
for *any* input file, not just the example one you are given.

Be sure to test that it worked by logging into the submit system! You
can resubmit to try again until you get it right.

## Commands to submit

    club -csd212 -pquiz02 registrar.py

    submit -c=sd212 -p=quiz02 registrar.py
