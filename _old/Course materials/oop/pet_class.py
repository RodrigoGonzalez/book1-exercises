# parent class
class Pet(object):

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# parent class
class Dog(object):

    # class attribute
    species = 'mammal'
    is_hungry = True

    # initializer / Instance attributes
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
print "I have {} dogs.".format(len(my_pets.dogs)),
for dog in my_pets.dogs:
    dog.eat()
    print "{} is {}.".format(dog.name, dog.age),
print "And they're all {}s, of course.".format(dog.species),
if dog.is_hungry is True:
    print "My dogs are hungry."
else:
    print "My dogs are not hungry."
