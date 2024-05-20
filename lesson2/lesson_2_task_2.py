def is_year_leap(year):
    is_leap = False
    if year % 4 == 0 :
        is_leap = True
    return is_leap


year = 2023
is_leap = str(is_year_leap(year))
print("год " + str(year) + ": " + is_leap)

year = 2024
is_leap = str(is_year_leap(year))
print("год " + str(year) + ": " + is_leap)
