class SmartFridge:
    def __init__(self, temp):
        self._temp = temp # Internal attribute

    @property
    def temp(self):
        """The Getter: allows reading the value like an attribute"""
        return f"{self._temp}°F"

    @temp.setter
    def temp(self, new_temp):
        """The Setter: acts as a gatekeeper"""
        if 32 <= new_temp <= 45:
            self._temp = new_temp
        else:
            print("Error: Temperature outside safe food range!")

my_fridge = SmartFridge(36)
my_fridge.temp = 40    # Valid change
my_fridge.temp = 100   # Triggers validation error