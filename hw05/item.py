# DO NOT CHANGE THIS FILE
# You need to use the Item class as-is inside your Backpack.

class Item:
    def __init__(self, name, weight, value):
        self._name = name
        self._weight = weight
        if value < 50:
            self._rarity = "Common"
        elif value < 80:
            self._rarity = "Rare"
        else:
            self._rarity = "Legendary"

    def get_weight(self):
        return self._weight

    def get_rarity(self):
        return self._rarity

    def __str__(self):
        return f"[{self.get_rarity()}] {self._name} ({self.get_weight()}kg)"
