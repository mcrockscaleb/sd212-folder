# YOU FILL THIS IN

class Bids:

    def __init__(self):
        self.bids = {}
        

    def add_bid(self, name, bid):
        #Records a bid with the given amount by the named contractor
        self.bids[name] = int(bid)
        
    def get_lowest(self):
        #Returns the name (only) of the lowest bidder so far.
        lowest = 1000
        keys = list(self.bids.keys())
        values = list(self.bids.values())
        for item in values:
            item = int(item)
        print(min(values))
        
        if min(values).isin(self.bids):
            return key

    