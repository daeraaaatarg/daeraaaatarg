class Human:
    def __init__(self, name, lastname, age=15):
        self.name = name
        self.lastname = lastname
        self.age = age

    def speak_about(self):
        print(f"Hi, my name is {self.name}")
        print(f"Hi, my lastname is {self.lastname}")
        print(f"I am {self.age} yo")


anastasia = Human(name = "Anastasia", lastname = "Kutova")
anastasia.speak_about()