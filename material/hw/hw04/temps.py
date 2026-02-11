# You fill this in!
class Temps:

    def __init__(self):
        self.readings = []
    
    def add_reading(self, x):
        self.readings.append(x)
        return self.readings

    def get_count(self):
        return len(self.readings)

    def get_average(self):
        return sum(self.readings)/len(self.readings)

    def get_high(self):
        return max(self.readings)
    

if __name__  == '__main__':
    from temps import Temps # import the class from your file

    hot_day = Temps() # create a new object
    print(hot_day.get_count()) # should be 0
    hot_day.add_reading(80)
    hot_day.add_reading(87)
    hot_day.add_reading(92)
    hot_day.add_reading(87)
    print(hot_day.get_count()) # should be 4
    # this should be (80 + 87 + 92 + 87) / 4 = 86.5
    print("Average temp on hot day:", hot_day.get_average())
    print("High on a hot day:", hot_day.get_high()) # should be 92

    # create a different object
    cool_day = Temps()
    cool_day.add_reading(65)
    cool_day.add_reading(75)
    # this should print 70.0 and 75
    print("Cool day stats:", cool_day.get_average(), cool_day.get_high())

    # both objects are independent; should be 4 and 2
    print("Number of readings on hot/cool days:", hot_day.get_count(), cool_day.get_count())