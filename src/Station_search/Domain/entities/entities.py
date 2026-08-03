import pandas as pd
class Postalcode:
    """
        This class represents a list of charging stations in Berlin of specifc PLZ.
    """
    def __init__(self, plz):
        self.plz = plz

    def check_dtype(self):
        if not isinstance(self.plz, int):
            raise TypeError(f"plz must be of type {int}")
        return isinstance(self.plz, int)

    def check_length(self):
        if len(str(self.plz)) != 5:
            raise ValueError("Invalid postal code: {}. Postal code must have 5 digits.".format(str(self.plz)))
        return True


    def check_range(self):
        print(type(self.plz))
        if not (10115 <= self.plz <= 14200):
            raise ValueError("PLZ must be between 10115 and 14200")
        return True


