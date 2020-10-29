def first_before_second(source: str, first: str, second: str) -> bool:
    return source.index(second) > source.rfind(first)


print(first_before_second("a rabbit jumps joyfully", "a", "j") == True)
print(first_before_second("knaves knew about waterfalls", "k", "w") == True)
print(first_before_second("happy birthday", "a", "y") == False)
print(first_before_second("precarious kangaroos", "k", "a") == False)
