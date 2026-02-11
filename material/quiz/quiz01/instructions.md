# SD212 Quiz 01: Inventory Restock Budget

## Scenario

You are the manager of a local grocery store. Every week, you need to
check your inventory and decide which items to buy more of.
Your policy is: if an item is completely out of stock (quantity is 0),
you will buy exactly 10 new units of that item.

Your task is to write a program that calculates the total cost of
buying these replacement items.

## The Data

The store's stock is saved in a file named `inventory.csv`. Each
row contains the name of the item, the price per unit, and the
number of units currently on the shelf.

**Example `inventory.csv` content:**

    item_name,price,quantity
    Apples,0.50,12
    Bananas,0.30,0
    Milk,2.50,15
    Bread,2.00,0
    Eggs,3.00,24
    Cheese,4.57,0

## Example Calculation

Based on the sample data above:

* Bananas: Quantity is 0. Cost to buy 10 = 0.30 * 10 = 3.0
* Bread:   Quantity is 0. Cost to buy 10 = 2.00 * 10 = 20.0
* Cheese:  Quantity is 0. Cost to buy 10 = 4.57 * 10 = 45.7
* **Total:** 3.0 + 20.0 + 45.7 = 68.7

Expected Output:

    68.7

## Your Task

Write a Python program `restock.py` that reads the `inventory.csv` file
and calculates the total cost to buy 10 of all items that are currently
out of stock.

Your program should just print a single number for the total cost, with
no other output.

You can use any methods you have learned to do this in Python. But it
has to work perfectly - be sure to check the results in the submit
system after you turn it in, and try again if it's not perfect the first
time.

## Commands to submit

    club -csd212 -pquiz01 restock.py

    submit -c=sd212 -p=quiz01 restock.py
