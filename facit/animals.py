"""One possible final version of the animal classes."""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def move(self):
        return f"{self.name} ({self.age}) is moving"

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Horse(Animal):
    def speak(self):
        return "Neigh"


class Cow(Animal):
    def speak(self):
        return "Moo"
