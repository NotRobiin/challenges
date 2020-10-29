def cars_needed(n):
    if n == 0:
        return 0

    if n <= 5:
        return 1

    rem = (n % 5) > 0

    return round(n / 5 + rem)

print(cars_needed(5), cars_needed(5) == 1)
print(cars_needed(11), cars_needed(11) == 3)
print(cars_needed(0), cars_needed(0) == 0)
