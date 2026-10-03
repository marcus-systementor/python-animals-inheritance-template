"""Demonstrate inheritance and polymorphism with the final classes."""

from animals import Animal, Dog, Cat, Horse, Cow


animal = Animal("Test", 5)
dog = Dog("Fido", 4)
cat = Cat("Milo", 2)
horse = Horse("Star", 7)
cow = Cow("Bessie", 3)

print(animal.eat())
print(animal.sleep())
print(animal.move())
print(animal.speak())

for creature in [dog, cat, horse, cow]:
    print(creature.name, creature.age)
    print(creature.eat())
    print(creature.sleep())
    print(creature.move())
    print(creature.speak())
