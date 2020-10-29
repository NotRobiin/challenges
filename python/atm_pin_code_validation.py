def is_valid_PIN(pin):
    return len(pin) in [4, 6] and pin.isdigit()

print(is_valid_PIN("1234"))
print(is_valid_PIN("12345"))
print(is_valid_PIN("a234"))
print(is_valid_PIN(""))
