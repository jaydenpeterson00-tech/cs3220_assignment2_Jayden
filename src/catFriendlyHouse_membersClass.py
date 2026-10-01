from src.thingClass import Thing

class Food(Thing):
    def __init__(self, weight, calories):
        self.weight = weight
        self.calories = calories
        self.energy = weight * calories

class Milk(Food):
    def __init__(self, weight, calories):
        super().__init__(weight, calories)

    def sayHi(self):
        print("There is a milk")

class Sausage(Food):
    def __init__(self, weight, calories):
        super().__init__(weight, calories)

    def sayHi(self):
        print("There is a sausage")

class Mouse(Food):
    def __init__(self, size):
        self.size = size
        self.energy = size * 1000

    def sayHi(self):
        print(f"There is a Mouse with a power {self.energy}")
