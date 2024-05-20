list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for x in range(0, len(list)):
    if list[x] % 3 == 0 and list[x] < 30:
        print(str(list[x]))