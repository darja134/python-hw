from address import Address

class Mailing:
    to_address = "000000,City,St. Street,13,4"
    from_address = "000000,City,St. Street,13,4"
    cost = 0
    track = "0000000"


    def __init__(self, to_address, from_address, cost, track):
        if(not to_address or not from_address or not cost or not track):
            raise ValueError("Value(s) should not be empty!")
        else:
            self.to_address = Address(to_address.split(","))
            self.from_address = Address(from_address.split(","))
            self.cost = cost
            self.track = track


    def printMailInfo(self):
        print("Отправление " + str(self.track) + " из " + self.from_address.printAddress() + " в " + \
              self.to_address.printAddress() + ". Стоимость " + str(self.cost) + " рублей.")
