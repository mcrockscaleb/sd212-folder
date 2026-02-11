class Bids:
    def __init__(self):
        # Dictionary to store bids: {name: amount}
        self.bids = {}

    def add_bid(self, name, amount):
        # Record or update a bid for the given contractor
        self.bids[name] = amount

    def get_lowest(self):
        # Find the contractor with the lowest bid amount
        lowest_name = None
        lowest_amount = None

        for name, amount in self.bids.items():
            if lowest_amount is None or amount < lowest_amount:
                lowest_amount = amount
                lowest_name = name

        return lowest_name
