# THIS IS A TESTER PROGRAM
# You can modify it as you like, but it will not be submitted.

from item import Item
from backpack import Backpack

big_pack = Backpack(20.0)
small_pack = Backpack(3.0)

sword = Item("Iron Sword", 5.5, 60)
spells = Item("Book of Spells", 1.5, 90)
potion = Item("Health Potion", 0.5, 10)
idol = Item("Golden Idol", 12.0, 95)
gem = Item("Precious Gem", 1.4, 99)

big_pack.add(sword) # adding [Rare] Iron Sword (5.5kg)
small_pack.add(potion) # adding [Common] Health Potion (0.5kg)
small_pack.add(sword) # OVER CAPACITY
big_pack.add(idol) # adding [Legendary] Golden Idol (12.0kg)
big_pack.add(spells) # adding [Legendary] Book of Spells (1.5kg)
small_pack.add(gem) # adding [Legendary] Precious Gem (1.4kg)

print(f"Small pack weight: {small_pack.total_weight()}")
print(f"Big pack weight: {big_pack.total_weight()}")
print("Big pack legendary items:")
bigleg = big_pack.get_by_rarity("Legendary")
for item in bigleg:
    print(item)
