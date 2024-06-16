from address import Address

class Mailing:

    def __init__(self, to_address: Address, from_address: Address, cost, track):
        #if(not to_address or not from_address or not cost or not track):
        #    raise ValueError("Value(s) should not be empty!")
        #else:
            self.to_address = to_address
            self.from_address = from_address
            self.cost = cost
            self.track = track


    def print_mail_info(self):
        print("Отправление " + str(self.track) + " из " + self.from_address.print_address() + " в " + \
              self.to_address.print_address() + ".\nСтоимость " + str(self.cost) + " рублей.")
