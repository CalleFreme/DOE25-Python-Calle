# Simpelt exempel på klassmetoder och cls
# En klassmetod är en metod som är bunden till klassen och inte till instansen av klassen.
# De är användbara för att t.ex. skapa instanser på olika sätt, eller för att utföra operationer som
# är relaterade till klassen, och inte till en specifik instans/objekt.
# Vi använder keyword cls, istället för self, för att referera till klassen inom klassmetoden.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")

    @classmethod
    def from_string(cls, person_str):
        '''
        Skapar en Person-instans från en sträng.
        '''
        name, age = person_str.split(", ")
        return cls(name, int(age))
    
    @classmethod
    def from_dict(cls, person_dict):
        '''
        Skapar en Person-instans från en dictionary.
        '''
        return cls(person_dict["name"], person_dict["age"])
    
    @classmethod
    def from_list(cls, person_list):
        '''
        Skapar en Person-instans från en lista.
        '''
        return cls(person_list[0], person_list[1])
    
    @classmethod
    def from_input(cls):
        '''
        Skapar en Person-instans från användarens inmatning.
        Det är OK att vi kallar på input() i en klassmetod.
        '''
        name = input("Ange namn: ")
        age = int(input("Ange ålder: "))
        return cls(name, age)
    
    @classmethod
    def is_adult(cls, age):
        '''
        Kollar om en ålder är vuxen (18 år eller äldre).
        '''
        return age >= 18
    
    @classmethod
    def average_age(cls, people):
        '''
        Beräknar medelåldern för en lista av Person-instans.
        '''
        total_age = sum(person.age for person in people)
        return total_age / len(people)
    
# Exempel på användning av klassmetoder
person1 = Person.from_string("Alice, 30")   # Skapar en Person-instans från en sträng
person2 = Person.from_dict({"name": "Bob", "age": 25}) # Skapar en Person-instans från en dictionary
person3 = Person.from_list(["Charlie", 35]) # Skapar en Person-instans från en lista
person4 = Person.from_input()
people = [person1, person2, person3, person4]

Person.is_adult(20)  # True
Person.average_age(people)

