def month_to_season(month):
    if month in range(1, 3) or month == 12:
        print("Winter")
    elif month in range(3, 6):
        print("Spring")
    elif month in range(6, 9):
        print("Summer")
    elif month in range(9, 12):
        print("Autumn")
    elif month > 12:
        print("No such a month")


for n in range(1, 14):
    month_to_season(n)
