# Inheritance / Arv: A class can inherit attributes and methods from another class.

class Animal(object): # All base classes inherits from the basic object type
    def __init__(self, name, legs=0):
        self.name = name
        self.legs = legs

    def speak(self):        
        print("Some sound")

    def describe(self):
        print(f"{self.name} has {self.legs} legs")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 4)

    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 4)
    def speak(self):
        print(f"{self.name} says: Meow!")

class Human(Animal):
    def __init__(self, name):
        super().__init__(name, 2)
    def speak(self):
        print(f"{self.name} says: Hello!")

class Fish(Animal):
    # Fish should have 0 legs
    def __init__(self, name):
        super().__init__(name, 0)

    def speak(self):
        print(f"{self.name} says blubblubblub")



def create_animal(animal_type, name):
    if animal_type == "dog":
        return Dog(name)
    elif animal_type == "cat":
        return Cat(name)
    elif animal_type == "fish":
        return Fish(name)
    elif animal_type == "human":
        return Human(name)
    else:
        return Animal(name)


animal_list = []
while True:
    animal_type = input("Which kind of animal? dog/cat/fish/human: ")
    animal_name = input("What's their name? ")
    new_animal = create_animal(animal_type, animal_name)
    animal_list.append(new_animal)
    cont = input("Create another animal? y/n")
    if cont == "n":
        break

for animal in animal_list:
    animal.describe()
    animal.speak()

#some_animal = Animal("Roger")
#dog = Dog("Buddy")
#cat = Cat("Whiskers")
#fish = Fish("Goldie")

#some_animal.speak()
#dog.speak()
#cat.speak()
#fish.speak()