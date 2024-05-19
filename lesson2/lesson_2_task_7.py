list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Variant no.1
print("1. Sum of all elements is: " + str(sum(list)))

# Variant no.2
sum = 0
for x in range(0, len(list)):
    sum += list[x]

print("2. Sum of all elements is: " + str(sum))