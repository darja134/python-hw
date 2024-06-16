class Address:

    def __init__(self, index, city, street, building, flat):
        #if(not address):
        #    raise ValueError("Value(s) should not be empty!")
        #else:
            self.index = index
            self.city = city
            self.street = street
            self.building = building
            self.flat = flat


    def print_address(self):
        stringAddress = str(self.index) + ", " + self.city + ", " + self.street + ", " + \
              str(self.building) + "-" + str(self.flat)
        return stringAddress
