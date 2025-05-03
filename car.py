class Car:
    def __init__(self, marka, model, year, power, fuel):
        self.marka = marka
        self.model = model
        self.year = year
        self.power = power
        self.economy = fuel

    def speak_about(self):
        print(f"The brand of the car is {self.marka} and the model is {self.model}")
        print(f"The year of manufacture {self.year}")
        print(f"It has {self.power} of power")
        print(f"And {self.economy} of fuel economy")


Pyzhyk = Car(marka = "Peugeot", model = "308 SW", year = "2010", power = "108 - 221 bhp", fuel = "42.3 - 65.6 mpg")
Pyzhyk.speak_about()