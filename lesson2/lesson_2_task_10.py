def bank(deposit, term):
    for x in range(0, term):
        deposit += deposit * (annual / 100)
    return deposit


deposit = input("Enter deposit amount: ")
term = input("Enter term lenght: ")
annual = 10
print("After " + str(term) + " years deposit sum will be " + str(bank(int(deposit), int(term))))