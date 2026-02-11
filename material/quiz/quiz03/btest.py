# THIS FILE IS USED TO TEST YOUR CODE
# You do not need to change it, but you can if you want.

from bidsANSWER import Bids

# Create two separate project instances
ship_contract = Bids()
flight_contract = Bids()

# Project 1: Shipbuilding
ship_contract.add_bid("HII", 500)
ship_contract.add_bid("General Dyn", 450)
ship_contract.add_bid("Austal", 475)

# Project 2: Flight Systems
flight_contract.add_bid("Lockheed", 200)
flight_contract.add_bid("Boeing", 250)
flight_contract.add_bid("Northrop", 180)

# Check results for each independent project
print(f"Ship Winner: {ship_contract.get_lowest()}")     # Expected: General Dyn
print(f"Flight Winner: {flight_contract.get_lowest()}") # Expected: Northrop

# Late bid for Ships
ship_contract.add_bid("Bollinger", 400)
print(f"New Ship Winner: {ship_contract.get_lowest()}")         # Expected: Bollinger
print(f"Flight Winner remains: {flight_contract.get_lowest()}") # Expected: Northrop
