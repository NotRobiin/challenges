import n2w

def num_to_eng(n):
    return n2w.convert(n)



print(num_to_eng(0), num_to_eng(0) == "zero")
print(num_to_eng(18), num_to_eng(18) == "eighteen")
print(num_to_eng(126), num_to_eng(126) == "one hundred twenty six")
print(num_to_eng(909), num_to_eng(909) == "nine hundred nine")
