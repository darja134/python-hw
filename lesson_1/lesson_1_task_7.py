#Variant no.1
def print_number(number):
    return str(number)

# Print 88005553535 by caling functions
number = print_number(8) + print_number(8) + print_number(0) + print_number(0) + print_number(5) + \
    print_number(5) + print_number(5) + print_number(5) + print_number(3) + print_number(5) + print_number(3)
print("Variant no.1: " + number)

# Variant no.2
def print_number_2(number):
    print(number, end = "")

# Print 88005553535 by caling functions
print("Variant no.2: ", end = "")
print_number_2(8)
print_number_2(8)
print_number_2(0)
print_number_2(0)
print_number_2(5)
print_number_2(5)
print_number_2(5)
print_number_2(3)
print_number_2(5)
print_number_2(3)
print_number_2(5)