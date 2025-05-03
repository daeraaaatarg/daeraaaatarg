import math


class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        suma = self.first + self.second
        print(f"Suma: {suma}")

    def minus(self):
        difference = self.first - self.second
        print(f"Difference: {difference}")

    def multiply(self):
        multiplication = self.first * self.second
        print(f"Multiplication: {multiplication}")

    def divide(self):
        if self.second != 0:
             division = self.first / self.second
             print(f"Division: {division}")
        else:
            print("Cannot divide")

    def discriminator(self, a, b, c):
        discriminat = b**2 - 4*a*c
        print(f"Disc is {discriminat}")
        if discriminat < 0:
            print("Cannot, disc is less than zero")
        if discriminat == 0:
            x0 = -b / 2*a
            print(f"Zero disc, so x is {x0}")
        if discriminat > 0:
            x1 = (-b + math.sqrt(discriminat)) / 2*a
            x2 = (-b - math.sqrt(discriminat)) / 2*a
            print(f"First one: {x1}")
            print(f"First one: {x2}")

        if a == 1:
            viet_plus = x1 + x2
            viet_multi = x1 * x2
            print("Checking:")
            print(f"{x1} + {x2} = {viet_plus} = {-b}")
            print(f"{x1} * {x2} = {viet_multi} = {c}")


calculator = Calculator(5,9)
calculator.plus()
calculator.minus()
calculator.multiply()
calculator.divide()
calculator.discriminator(1,9,2)