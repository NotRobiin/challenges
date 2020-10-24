class Pizza:
    order_number = 0

    def __init__(self, ing):
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
        self.ingredients = ing

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])


p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
p2 = Pizza.garden_feast()  # order 2
print(p1.ingredients)  # ["bacon", "parmesan", "ham"]
print(p2.ingredients)  # ["spinach", "olives", "mushroom"]
print(p1.order_number)  # 1
print(p2.order_number)  # 2

