# SD212 Quiz 03: Lowest bidder

## Scenario

The Navy is contracting out work for new projects and needs to
keep track of who is the lowest bidder.

## Your task

Write a class `Bids` that has a constructor and two methods:

*   `add_bid(name, amount)`: Records a bid with the given amount
    by the named contractor

*   `get_lowest()`: Returns the name (only) of the lowest bidder so far.

## Example usage

Look at the file `btest.py` for an example program that uses your
`Bids` class. If your class works correctly, then running that
program should produce the following output:

    Ship Winner: General Dyn
    Flight Winner: Northrop
    New Ship Winner: Bollinger
    Flight Winner remains: Northrop

## Commands to submit

    club -csd212 -pquiz03 bids.py

    submit -c=sd212 -p=quiz03 bids.py
