class Address:
    #index = 000000
    #city = "City"
    #street= "St. Street"
    #building = 13
    #flat = 4


    def __init__(self, address):
        #if(not address):
        #    raise ValueError("Value(s) should not be empty!")
        #else:
            self.index = address[0]
            self.city = address[1]
            self.street = address[2]
            self.building = address[3]
            self.flat = address[4]


    def printAddress(self):
        stringAddress = str(self.index) + ", " + self.city + ", " + self.street + ", " + \
              str(self.building) + " - " + str(self.flat)
        return stringAddress
