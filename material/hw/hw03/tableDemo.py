# Your task: Define the Table class here
class Table:

    def __init__(self):
        self.total = 0

    def order(self, item, price):
        self.total += price
        print(f"Ordering {item}")

    def pay(self, percent):
        return self.total + self.total *(percent/100)



#### DO NOT CHANGE THE CODE BELOW!
t1 = Table()
while True:
    line = input("Enter item and price (or 'done'): ")
    if line.strip() == 'done':
        break
    item, price = line.split()
    price = float(price)
    t1.order(item, price)
cheap = t1.pay(10)
nice = t1.pay(25)
print(f"Total with 10% tip would be {round(cheap,2)}, or with 25% would be {round(nice,2)}")
