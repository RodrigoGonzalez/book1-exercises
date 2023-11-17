# parent class
class Pet():

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


# parent class
class Dog():

    # class attribute
    species = 'mammal'
    is_hungry = True

    # initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # instance method
    def eat(self):
        self.is_hungry = False

    def walk(self):
        return f"{self.name} is walking!"


# child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"


# child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"

# create instances of dogs
my_dogs = [Bulldog("Tom", 6), RussellTerrier("Fletcher", 7), Dog("Larry", 9)]

# instantiate the Pet() class
my_pets = Pet(my_dogs)

# output
my_pets.walk()
