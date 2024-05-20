import math

def square(side):
    side = math.ceil(side)
    return side * side


side = 4
print("Area of a square with side " + str(math.ceil(side)) + " is " + str(square(side)))

side = 4.3
print("Area of a square with side " + str(math.ceil(side)) + " is " + str(square(side)))
