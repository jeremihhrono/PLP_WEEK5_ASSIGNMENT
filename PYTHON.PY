"""assignment 1"""

# Base class
class Character:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def describe(self):
        return f"{self.name} (Power Level: {self.power_level})"

    def attack(self):
        return f"{self.name} attacks with a basic strike."

# Subclass: Superhero
class Superhero(Character):
    def __init__(self, name, power_level, alias):
        super().__init__(name, power_level)
        self.alias = alias

    def describe(self):
        return f"{self.alias}, also known as {self.name} (Power Level: {self.power_level})"

    def attack(self):
        return f"{self.alias} unleashes a heroic punch!"

    def save_civilians(self):
        return f"{self.alias} is saving civilians!"

# Subclass: Villain
class Villain(Character):
    def __init__(self, name, power_level, evil_plan):
        super().__init__(name, power_level)
        self.evil_plan = evil_plan

    def describe(self):
        return f"Villain: {self.name} (Power Level: {self.power_level})"

    def attack(self):
        return f"{self.name} strikes with villainous force! Plan: {self.evil_plan}"

    def taunt(self):
        return f"{self.name} taunts: '{self.evil_plan} is unstoppable!'"

# Example usage:
if __name__ == "__main__":
    hero = Superhero("Clark Kent", 9000, "Superman")
    villain = Villain("Lex Luthor", 8500, "World Domination")

    for character in (hero, villain):
        print(character.describe())
        print(character.attack())

    print(hero.save_civilians())
    print(villain.taunt())








"""ASSIGNMENT 2"""

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} moves... (generic)"

class Car(Vehicle):
    def __init__(self, model, fuel_type):
        super().__init__(model)
        self.fuel_type = fuel_type

    def move(self):
        return f"{self.model} is driving using {self.fuel_type}."

class Plane(Vehicle):
    def __init__(self, model, altitude):
        super().__init__(model)
        self.altitude = altitude

    def move(self):
        return f"{self.model} is flying at {self.altitude} meters."

def travel(vehicle: Vehicle):
    print(vehicle.move())

# Example usage:
if __name__ == "__main__":
    car = Car("Tesla Model 3", "electricity")
    plane = Plane("Boeing 747", 10000)

    for v in (car, plane):
        travel(v)
