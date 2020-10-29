def is_prime(value):
    if value <= 1:
        return False

    for i in range(2, value):
        if value % i == 0:
            return False

    return True


def sum_primes(l):
    s = sum(list(filter(is_prime, l)))
    return None if not s else s


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 17
print(sum_primes([2, 3, 4, 11, 20, 50, 71]))  # 87
print(sum_primes([]))  # None

