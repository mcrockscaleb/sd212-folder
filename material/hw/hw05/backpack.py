# YOU FILL IN THIS FILE with your Backpack class
from item import Item

class Backpack:

    def __init__(self, capacity):
        self.capacity = capacity
        self._count = 0
        self._pack = []
    
    def add(self, item):
        print(f"adding {item}")
        self._count += item._weight
        self._pack.append(item)
        #print(self._count)
        if (self._count) > self.capacity:
            print("OVER CAPACITY")
            self._count -= item._weight
            self._pack.pop()
        
    def total_weight(self):
        return self._count
    
    def get_by_rarity(self, rarity):
        pack = []
        for item in self._pack:
            if item.get_rarity() == rarity:
                pack.append(item)  
        return pack

'''
big_pack = Backpack(10.0)

sword = Item("Iron Sword", 5.5, 60)
big_pack.add(sword)
big_pack.add(sword)
print(f"Big pack weight: {big_pack.total_weight()}")
results = big_pack.get_by_rarity("Rare")
for item in results:
    print(item)
'''