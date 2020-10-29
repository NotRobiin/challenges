import datetime

def has_friday_13(month, year):
    return bool(datetime.datetime(year, month, 13).strftime("%a") == "Fri")

print(has_friday_13(3, 2020) == True)
print(has_friday_13(10, 2017) == True)
print(has_friday_13(1, 1985) == False)
