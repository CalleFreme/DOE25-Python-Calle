
# Person class represents a human with a name and age.
class Person:
    def __init__(self, name, age):
        """
        Initialize a new Person instance.
        :param name: The person's name (str)
        :param age: The person's age (int)
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Return a string representation of the person.
        """
        return f"Name: {self.name} | Age: {self.age}"

    def greet(self, name_to_greet=None):
        """
        Print a greeting with the person's name and age.
        :param name_to_greet: Optional name to greet (str)
        """
        if name_to_greet:
            print(f"Hello {name_to_greet}, my name is {self.name} and I am {self.age} years old.")
        else:
            print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def change_name(self, new_name):
        """
        Change the person's name.
        :param new_name: The new name (str)
        """
        self.name = new_name

    def get_name(self):
        """
        Get the person's name.
        :return: The name (str)
        """
        return self.name
    

p1 = Person("Calle", 31)
p2 = Person("Anna", 25)
p3 = Person("Bertil", 40)
p4 = Person("David", 20)

p1.greet()
p2.greet("Adam")
p3.greet("Eva")
p4.greet()

person_list = [p1, p2, p3, p4]

print(f"{p1.name} is {p1.age} years old.")

# range(x) = intervallet 0 upp till x
for i in range(len(person_list)):
    print(f"Person #{i+1}: {person_list[i]}")

for person in person_list:
    print(person)

new_name = input(f"Set new name for {p1.name}: ")
p1.name = new_name
print("New name is", p1.name)

# Better approach:
new_name = input(f"Set new name for {p1.get_name()} ")
p1.change_name(new_name)
print("New name is", p1.get_name())

print(p1)

person_dict = {"Calle": p1, "Anna": p2, "Bertil": p3, "David": p4}

