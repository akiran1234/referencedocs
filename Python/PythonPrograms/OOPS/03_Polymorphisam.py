# Polymorphism with classes
# Polymorphism with class methods.

class Bear:
    def sound(self):
        print("Groarrr")


class Dog:
    def sound(self):
        print("Woof woof!")


def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound( bearObj )
makeSound( dogObj )