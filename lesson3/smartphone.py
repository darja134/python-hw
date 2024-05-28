class Smartphone:
    def __init__(self, phone, model, number):
        if(not phone or not model or not number):
            raise ValueError("Value(s) should not be empty!")
        else:
            self.phone = phone
            self.model = model
            if(number.startswith("+79")):
                self.number = number
            else:
                raise ValueError("Number should start with '+79'")


    def printInfo(self):
        print(self.phone + " - " + self.model + ". " + self.number)
