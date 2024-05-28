class User:
    def __init__(self, first_name, last_name):
        if(not first_name or not last_name):
            raise ValueError("Value(s) should not be empty!")
        else:
            self.first_name = first_name
            self.last_name = last_name
    

    def printName(self):
        print(self.first_name)


    def printSurname(self):
        print(self.last_name)


    def printNameAnsSurname(self):
        print(self.first_name + " " + self.last_name)

