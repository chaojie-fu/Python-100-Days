"""
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price.
Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""
class Flower():
    def __init__(self, name, petal, price):
        self.Name = name
        self.Petal = petal
        self.Price = price

    def set_name(self, name):
        self.Name = name

    def set_petal(self, petal):
        self.Petal = petal

    def set_price(self, price):
        self.Price = price

    def get_name(self):
        return self.Name

    def get_petal(self):
        return self.Petal

    def get_price(self):
        return self.Price


def main():
    rose = Flower('rose', 10, 100)
    print(rose.get_price())


if __name__ == '__main__':
    main()
