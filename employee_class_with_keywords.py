class Employee:
    def __init__(self, name: str, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

        n = name.split(" ")
        self.name = n[0]
        self.lastname = n[1]


if __name__ == "__main__":
    e = Employee("Robert Mokanek", salary=12000)
    print(e.salary)

