# YOU FILL IN THIS FILE with your Weight class

class Weight:
    gpo = 28.3495  #grams per ounce

    def __init__(self, amount, unit):
        if unit == "g":
            self._g = amount
            self._oz = self._g/self.gpo 
        elif unit == 'oz':
            self._oz = amount
            self._g = self._oz*self.gpo

    @property
    def g(self):
        return self._g  

    @property
    def oz(self):
        return self._oz

    @g.setter
    def g(self, value):
        self._g = value
        self._oz = self._g/self.gpo


    @oz.setter
    def oz(self, value):
        self._oz = value
        self._g = self._oz*self.gpo  