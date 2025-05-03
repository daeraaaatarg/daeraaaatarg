
class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        suma = self.first + self.second
        print(suma)

calculator = Calculator(first = 5, second = 2)
calculator.plus()