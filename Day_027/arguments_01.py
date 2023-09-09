def add(*args):  # Unlimited Positional Arguments
    total = 0
    for num in args:
        total += num

    return total


print(add(3, 4, 5))


def calculate(n, **kwargs):  # Unlimited Keyword Arguments
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)
