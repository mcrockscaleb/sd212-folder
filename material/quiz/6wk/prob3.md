# SD212 6wk Practicum Problem 3: Glitchy vending machine

## Scenario

You are auditing a vending machine that has been acting up. The machine
tracks every transaction, but due to a glitch, some items were dispensed
with a price of `0.00` but were still marked as `PAID` (instead of
`CANCELLED`).

You need to identify exactly which items are being given away for free
so the vending company can fix the pricing database.

## The data

You have a file `transactions.csv` which contains lines like this:

    001:Snickers:1.50:PAID
    002:Coke:0.00:PAID
    003:Chips:0.00:CANCELLED
    004:Coke:0.00:PAID
    005:Pretzels:0.00:PAID
    006:Water:1.00:PAID
    007:Pretzels:0.00:PAID

**Important**: Notice that this file uses *colons* (`:`) as separators.

## Your task

Write a **bash script** in the file `glitch.sh` that prints out the
names of the items that were given away.

Your script must meet the following criteria:

1.  It must find transactions where the Price is `0.00` **AND** the
    Status is `PAID`. (Ignore `CANCELLED` transactions).

2.  It must print only the **Item Name** (the second column).

3.  It must **not** print duplicate names. (e.g., if "Coke" was stolen
    twice, only print "Coke" once).

You can test what you did by running:

    bash glitch.sh

For the sample data above, the correct output would look exactly like this:

    Coke
    Pretzels

## Commands to submit

    club -csd212 -p6wkp3 glitch.sh

    submit -c=sd212 -p=6wkp3 glitch.sh
