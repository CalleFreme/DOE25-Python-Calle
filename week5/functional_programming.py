"""
Funktionell programmering i Python - Introduktion och demonstrationer
=====================================================================

Detta program introducerar grundläggande koncept inom funktionell programmering
i Python med svenska kommentarer och praktiska exempel.

Författare: DOE25 Python Course
Datum: 2025-10-20
"""

from functools import reduce
from typing import List, Tuple, Any
import math

# =============================================================================
# INTRODUKTION TILL FUNKTIONELL PROGRAMMERING
# =============================================================================

"""
VAD ÄR FUNKTIONELL PROGRAMMERING?

Funktionell programmering är ett programmeringsparadigm som fokuserar på:
- Användning av funktioner som första klassens objekt
- Undvikande av förändring av tillstånd (immutability)
- Användning av rena funktioner (pure functions)
- Funktionskomposition och högre ordningens funktioner
   
Fördelar:
- Mer förutsägbar kod
- Lättare att testa och debugga
- Mindre bieffekter
- Bättre för parallell programmering
"""

print("=== INTRODUKTION TILL FUNKTIONELL PROGRAMMERING ===\n")

# =============================================================================
# RENA FUNKTIONER (PURE FUNCTIONS)
# =============================================================================

"""
RENA FUNKTIONER

En ren funktion är en funktion som:
1. Alltid returnerar samma resultat för samma input
2. Har inga bieffekter (påverkar inte externa variabler eller tillstånd)
3. Är deterministisk och förutsägbar
"""
to_add = 1
def f(x):
    to_add = 2 # Side effect inside function
    return x + to_add
f(2)
f(2) # = 3
to_add = 2
f(2) # = 4

print("1. RENA FUNKTIONER (Pure Functions)")
print("-" * 40)

# Exempel på ren funktion
def add_numbers(a: int, b: int) -> int:
    """
    Ren funktion: adderar två tal
    - Inga bieffekter
    - Samma input ger alltid samma output
    """
    return a + b

add_numbers(3, 5)
add_numbers(3, 5)

# Exempel på ICKE-ren funktion (för jämförelse)
counter = 0

def impure_increment():
    """
    ICKE-ren funktion: modifierar global variabel
    - Har bieffekter
    - Resultatet beror på extern tillstånd
    """
    global counter # Behöver deklarera global för att modifiera den
    counter += 1   
    return counter 

print(f"Ren funktion - add_numbers(3, 5): {add_numbers(3, 5)}")
print(f"Ren funktion - add_numbers(3, 5): {add_numbers(3, 5)}")  # Samma resultat
print(f"Icke-ren funktion - impure_increment(): {impure_increment()}")
print(f"Icke-ren funktion - impure_increment(): {impure_increment()}")  # Olika resultat

# Bättre version av increment som är ren
def pure_increment(value: int) -> int:
    """Ren version av increment-funktionen"""
    return value + 1

print(f"Ren increment - pure_increment(5): {pure_increment(5)}")
print(f"Ren increment - pure_increment(5): {pure_increment(5)}")  # Samma resultat
print()

# =============================================================================
# LAMBDA-FUNKTIONER (ANONYMA FUNKTIONER)
# =============================================================================

"""
LAMBDA-FUNKTIONER

Lambda-funktioner är anonyma funktioner som kan definieras inline.
Syntax: lambda argument(er): uttryck

Användningsområden:
- Korta, enkla funktioner
- Som argument till högre ordningens funktioner
- Snabb funktionsdefinition utan att namnge funktionen
"""

print("2. LAMBDA-FUNKTIONER (Anonymous Functions)")
print("-" * 40)

def squared(x):
    return x ** 2

# Grundläggande lambda-exempel
square = lambda x: x ** 2
print(f"Lambda för kvadrat - square(4): {square(4)}")

# Jämförelse med vanlig funktion
def square_function(x):
    return x ** 2

print(f"Vanlig funktion - square_function(4): {square_function(4)}")

# Lambda med flera argument
multiply = lambda x, y: x * y
print(f"Lambda med två argument - multiply(3, 7): {multiply(3, 7)}")

# 4 % 2 = 0
# 5 % 2 = 1
# Lambda för mer komplexa uttryck
is_even = lambda n: n % 2 == 0
print(f"Jämn nummer check - is_even(8): {is_even(8)}")
print(f"Jämn nummer check - is_even(7): {is_even(7)}")

# Lista med lambda-funktioner
operations = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x ** 2
]

number = 5
print(f"\nAnvända olika lambda-operationer på {number}:")
for i, op in enumerate(operations):
    print(f"Operation {i+1}: {op(number)}")
print()

# =============================================================================
# MAP() - APPLICERA EN FUNKTION PÅ ALLA ELEMENT
# =============================================================================

"""
MAP() FUNKTIONEN

map() applicerar en funktion på alla element i en iterabel objekt.
Syntax: map(function, iterable)

Returnerar: map-objekt (behöver konverteras till lista för att visa)
"""

print("3. MAP() - Applicera funktion på alla element")
print("-" * 40)

# Grundläggande map-exempel
numbers = [1, 2, 3, 4, 5] # -> [1, 4, 9, 16, 25]
square = lambda x: x ** 2
squared_list =list(map(square, numbers))

# För 2-dimensionell lista:
numbers_2d = [[1, 2], [3, 4], [5, 6]]
squared_2d = list(map(lambda row: list(map(square, row)), numbers_2d))

#squared = list(map(lambda x: x ** 2, numbers))
print(f"Ursprungliga tal: {numbers}")
print(f"Kvadrerade tal (map): {squared}")

# Map med namngiven funktion
def celsius_to_fahrenheit(celsius):
    """Konverterar Celsius till Fahrenheit"""
    return (celsius * 9/5) + 32

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print(f"\nTemperaturer i Celsius: {celsius_temps}")
print(f"Temperaturer i Fahrenheit: {fahrenheit_temps}")

# Map med strängar
names = ["anna", "erik", "maria", "johan"]
capitalized = list(map(str.capitalize, names))
print(f"\nUrsprungliga namn: {names}")
print(f"Namn med stor första bokstav: {capitalized}")

# Map med flera iterables
nums1 = [1, 2, 3, 4]
nums2 = [10, 20, 30, 40]
added = list(map(lambda x, y: x + y, nums1, nums2))
print(f"\nLista 1: {nums1}")
print(f"Lista 2: {nums2}")
print(f"Adderade (map): {added}")
print()

# =============================================================================
# FILTER() - FILTRERA ELEMENT BASERAT PÅ VILLKOR
# =============================================================================

"""
FILTER() FUNKTIONEN

filter() skapar en ny iterabel med element som uppfyller ett villkor.
Syntax: filter(function, iterable)

Funktionen ska returnera True/False för varje element.
"""

print("4. FILTER() - Filtrera element baserat på villkor")
print("-" * 40)

# Grundläggande filter-exempel
numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Alla tal: {numbers}")
print(f"Jämna tal (filter): {even_numbers}")

# Filter med mer komplex logik
ages = [15, 22, 8, 30, 17, 45, 12, 67]
adults = list(filter(lambda age: age >= 18, ages))
print(f"\nAlla åldrar: {ages}")
print(f"Vuxna (≥18): {adults}")

# Filter med strängar
words = ["python", "java", "javascript", "go", "rust", "php"]
short_words = list(filter(lambda word: len(word) <= 4, words))
print(f"\nAlla ord: {words}")
print(f"Korta ord (≤4 bokstäver): {short_words}")

# Filter med namngiven funktion
def is_prime(n):
    """Kontrollerar om ett tal är ett primtal"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(2, 21))
primes = list(filter(is_prime, numbers))
print(f"\nTal 2-20: {numbers}")
print(f"Primtal: {primes}")
print()

# =============================================================================
# SORTED() - SORTERA MED ANPASSADE KRITERIER
# =============================================================================

"""
SORTED() FUNKTIONEN

sorted() returnerar en ny sorterad lista från en iterabel.
Syntax: sorted(iterable, key=function, reverse=False)

key-parametern låter dig specificera sorteringskriterier.
"""

print("5. SORTED() - Sortera med anpassade kriterier")
print("-" * 40)

# Grundläggande sortering
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sorted(numbers)
print(f"Ursprunglig lista: {numbers}")
print(f"Sorterad (stigande): {sorted_numbers}")
print(f"Sorterad (fallande): {sorted(numbers, reverse=True)}")

# Sortera strängar efter längd
words = ["elefant", "katt", "hund", "myra", "björn"]
list_length = len(words)
word_length = words[0]
by_length = sorted(words, key=len)
print(f"\nOrd: {words}")
print(f"Sorterade efter längd: {by_length}")

# Sortera strängar alfabetiskt (case-insensitive)
mixed_case = ["Zebra", "apple", "Banana", "cherry"]
alphabetical = sorted(mixed_case, key=str.lower)
print(f"\nBlandade versaler: {mixed_case}")
print(f"Alfabetisk sortering: {alphabetical}")

# Sortera tupler/listor efter specifikt element
students = [("Anna", 85), ("Erik", 92), ("Maria", 78), ("Johan", 88)]
by_grade = sorted(students, key=lambda student: student[1], reverse=True)
print(f"\nStudenter (namn, betyg): {students}")
print(f"Sorterade efter betyg: {by_grade}")

# Sortera med mer komplex logik
people = [
    {"namn": "Anna", "ålder": 25, "stad": "Stockholm"},
    {"namn": "Erik", "ålder": 30, "stad": "Göteborg"},
    {"namn": "Maria", "ålder": 22, "stad": "Malmö"},
    {"namn": "Johan", "ålder": 28, "stad": "Uppsala"}
]

by_age = sorted(people, key=lambda person: person["ålder"])
print(f"\nPersoner sorterade efter ålder:")
for person in by_age:
    print(f"  {person['namn']}, {person['ålder']} år, {person['stad']}")
print()

# =============================================================================
# ZIP() - KOMBINERA FLERA ITERABLES
# =============================================================================

"""
ZIP() FUNKTIONEN

zip() kombinerar element från flera iterables till tupler.
Syntax: zip(iterable1, iterable2, ...)

Stoppar när den kortaste iterabeln tar slut.
"""

print("6. ZIP() - Kombinera flera iterables")
print("-" * 40)

# Grundläggande zip-exempel
names = ["Anna", "Erik", "Maria"]
ages = [25, 30, 22]
combined = list(zip(names, ages))
print(f"Namn: {names}")
print(f"Åldrar: {ages}")
print(f"Kombinerade (zip): {combined}")

# Zip med tre listor
subjects = ["Matematik", "Fysik", "Kemi"]
grades = [85, 92, 78]
teachers = ["Andersson", "Bergström", "Carlsson"]

course_info = list(zip(subjects, grades, teachers))
print(f"\nKursinformation:")
for subject, grade, teacher in course_info:
    print(f"  {subject}: Betyg {grade}, Lärare: {teacher}")

# Zip för att skapa dictionary
cities = ["Stockholm", "Göteborg", "Malmö", "Uppsala"]
populations = [975551, 583056, 347949, 230767]
city_dict = dict(zip(cities, populations))
print(f"\nStäder och befolkning: {city_dict}")

# Unzip (separera kombinerade data)
coordinates = [(1, 4), (2, 5), (3, 6)]
x_coords, y_coords = zip(*coordinates)
print(f"\nKoordinater: {coordinates}")
print(f"X-koordinater: {list(x_coords)}")
print(f"Y-koordinater: {list(y_coords)}")

# Zip med olika längder
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(f"\nLista 1: {list1}")
print(f"Lista 2: {list2}")
print(f"Zip (stannar vid kortaste): {zipped}")
print()

# =============================================================================
# REDUCE() - REDUCERA EN LISTA TILL ETT VÄRDE
# =============================================================================

"""
REDUCE() FUNKTIONEN

reduce() applicerar en funktion kumulativt på element i en sekvens,
från vänster till höger, för att reducera sekvensen till ett enda värde.

Syntax: reduce(function, sequence[, initial])
Kräver: from functools import reduce
"""

print("7. REDUCE() - Reducera lista till ett värde")
print("-" * 40)

# Grundläggande reduce-exempel (summa)
numbers = [1, 2, 3, 4, 5] # -> [3, 3, 4, 5] -> [6, 4, 5] -> [10, 5] -> 15
total = reduce(lambda x, y: x + y, numbers)
print(f"Tal: {numbers}")
print(f"Summa (reduce): {total}")

# Reduce för att hitta maximum
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum (reduce): {max_value}")

# Reduce med initial värde
total_with_initial = reduce(lambda x, y: x + y, numbers, 100)
print(f"Summa med startvärde 100: {total_with_initial}")

# Reduce för att multiplicera alla tal
product = reduce(lambda x, y: x * y, numbers)
print(f"Produkt av alla tal: {product}")

# Reduce med mer komplex logik
words = ["Hej", "världen", "från", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"\nOrd: {words}")
print(f"Mening (reduce): {sentence}")

# Reduce för att hitta längsta ordet
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(f"Längsta ordet: {longest_word}")

# Reduce med mer avancerat exempel - hitta största talet i nestlade listor
nested_numbers = [[1, 5, 3], [9, 2, 8], [4, 7, 6]]
all_numbers = reduce(lambda x, y: x + y, nested_numbers)
max_in_nested = reduce(lambda x, y: x if x > y else y, all_numbers)
print(f"\nNestlade listor: {nested_numbers}")
print(f"Alla tal: {all_numbers}")
print(f"Största talet: {max_in_nested}")
print()

# =============================================================================
# ANY() OCH ALL() - LOGISKA OPERATIONER
# =============================================================================

"""
ANY() OCH ALL() FUNKTIONER

any() - returnerar True om NÅGOT element är sant
all() - returnerar True om ALLA element är sanna

Användbart för att testa villkor över samlingar.
"""

print("8. ANY() och ALL() - Logiska operationer")
print("-" * 40)

# ANY() exempel
numbers = [0, 2, 0, 0, 0]
print(f"Tal: {numbers}")
print(f"any() - finns det något sant värde?: {any(numbers)}")

all_zeros = [0, 0, 0, 0]
print(f"Bara nollor: {all_zeros}")
print(f"any() - finns det något sant värde?: {any(all_zeros)}")

# ALL() exempel
positive_numbers = [1, 2, 3, 4, 5]
print(f"\nPositiva tal: {positive_numbers}")
print(f"all() - är alla värden sanna?: {all(positive_numbers)}")

mixed_numbers = [1, 2, 0, 4, 5]
print(f"Blandade tal: {mixed_numbers}")
print(f"all() - är alla värden sanna?: {all(mixed_numbers)}")

# Praktiska exempel med villkor
ages = [20, 25, 30, 17, 22]
print(f"\nÅldrar: {ages}")
print(f"Är någon minderårig? {any(age < 18 for age in ages)}")
print(f"Är alla vuxna? {all(age >= 18 for age in ages)}")

# Kontrollera strängar
words = ["python", "java", "go", "rust"]
print(f"\nProgrammeringsspråk: {words}")
print(f"Innehåller något ord 'o'? {any('o' in word for word in words)}")
print(f"Är alla ord kortare än 10 bokstäver? {all(len(word) < 10 for word in words)}")

# Kontrollera om alla tal är jämna
even_numbers = [2, 4, 6, 8, 10]
mixed_numbers = [2, 4, 7, 8, 10]
print(f"\nJämna tal: {even_numbers}")
print(f"Är alla jämna? {all(num % 2 == 0 for num in even_numbers)}")
print(f"Blandade tal: {mixed_numbers}")
print(f"Är alla jämna? {all(num % 2 == 0 for num in mixed_numbers)}")
print()

# =============================================================================
# LIST COMPREHENSIONS - ELEGANT LISTBEHANDLING
# =============================================================================

"""
LIST COMPREHENSIONS

List comprehensions erbjuder ett koncist sätt att skapa listor.
Syntax: [uttryck for element in iterabel if villkor]

Fördelar:
- Mer läsbar kod
- Ofta snabbare än traditionella loopar
- Mer pythonic
"""

print("9. LIST COMPREHENSIONS - Elegant listbehandling")
print("-" * 40)

# Grundläggande list comprehension
numbers = list(range(1, 11)) # Tal 1-10
squares = [num**2 for num in numbers]
print(f"Tal 1-10: {numbers}")
print(f"Kvadrater (list comp): {squares}")

# Jämförelse med traditionell loop
squares_loop = []
for x in numbers:
    squares_loop.append(x**2)
print(f"Kvadrater (loop): {squares_loop}")

# List comprehension med villkor
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Kvadrater av jämna tal: {even_squares}")

# Mer komplexa uttryck
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# List comprehension med strängar
words = ["python", "java", "javascript", "go"]
lengths = [len(word) for word in words]
print(f"\nOrd: {words}")
print(f"Längder: {lengths}")

# Filtrerad och transformerad lista
long_words_upper = [word.upper() for word in words if len(word) > 4]
print(f"Långa ord (>4 bokstäver) i versaler: {long_words_upper}")

# Nested list comprehension
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"\nMatrix: {matrix}")
print(f"Tillplattad: {flattened}") # Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension med if-else (ternary operator)
numbers = [-2, -1, 0, 1, 2]
absolute_values = [x if x >= 0 else -x for x in numbers]
print(f"\nTal: {numbers}")
print(f"Absolutvärden: {absolute_values}")

# Dictionary comprehension (bonus)
word_lengths = {word: len(word) for word in words}
print(f"\nOrdlängder (dict comprehension): {word_lengths}")

# Set comprehension (bonus)
unique_lengths = {len(word) for word in words}
print(f"Unika längder (set comprehension): {unique_lengths}")
print()

# =============================================================================
# KOMBINERADE EXEMPEL - ANVÄND FLERA TEKNIKER TILLSAMMANS
# =============================================================================

"""
KOMBINERADE EXEMPEL

Här visar vi hur olika funktionella programmeringstekniker
kan kombineras för att lösa mer komplexa problem elegant.
"""

print("10. KOMBINERADE EXEMPEL - Flera tekniker tillsammans")
print("-" * 40)

# Exempel 1: Bearbeta studentdata
students_data = [
    {"namn": "Anna", "ålder": 20, "betyg": [85, 90, 78]},
    {"namn": "Erik", "ålder": 22, "betyg": [92, 88, 85]},
    {"namn": "Maria", "ålder": 19, "betyg": [78, 82, 90]},
    {"namn": "Johan", "ålder": 21, "betyg": [95, 92, 88]}
]

# Beräkna medelbetyg för varje student
students_with_average = [
    {**student, "medelbetyg": sum(student["betyg"]) / len(student["betyg"])}
    for student in students_data
]

print("Studenter med medelbetyg:")
for student in students_with_average:
    print(f"  {student['namn']}: {student['medelbetyg']:.1f}")

# Hitta studenter med högt medelbetyg (>85)
high_performers = list(filter(
    lambda s: s["medelbetyg"] > 85,
    students_with_average
))

print(f"\nHögpresterande studenter (>85):")
for student in high_performers:
    print(f"  {student['namn']}: {student['medelbetyg']:.1f}")

# Exempel 2: Textanalys
text = "Python är ett fantastiskt programmeringsspråk för både nybörjare och experter"
words = text.lower().split()

# Analysera orden med funktionella tekniker
word_analysis = {
    "totalt_antal_ord": len(words),
    "unika_ord": len(set(words)),
    "ord_längre_än_5": len([w for w in words if len(w) > 5]),
    "innehåller_python": any("python" in word for word in words),
    "alla_alfabetiska": all(word.isalpha() for word in words),
    "längsta_ordet": max(words, key=len),
    "kortaste_ordet": min(words, key=len)
}

print(f"\nTextanalys av: '{text}'")
for key, value in word_analysis.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")

# Exempel 3: Databehandling med chained operations
sales_data = [
    {"produkt": "Laptop", "pris": 15000, "antal": 5},
    {"produkt": "Mus", "pris": 200, "antal": 50},
    {"produkt": "Tangentbord", "pris": 800, "antal": 25},
    {"produkt": "Monitor", "pris": 3000, "antal": 10},
    {"produkt": "Headset", "pris": 1200, "antal": 15}
]

# Beräkna totala intäkter och sortera efter lönsamhet
revenue_analysis = sorted(
    map(
        lambda item: {
            **item,
            "totala_intäkter": item["pris"] * item["antal"]
        },
        sales_data
    ),
    key=lambda x: x["totala_intäkter"],
    reverse=True
)

print(f"\nFörsäljningsanalys (sorterad efter totala intäkter):")
for item in revenue_analysis:
    print(f"  {item['produkt']}: {item['totala_intäkter']:,} kr")

total_revenue = sum(item["totala_intäkter"] for item in revenue_analysis)
print(f"\nTotala intäkter: {total_revenue:,} kr")
print()

# =============================================================================
# SAMMANFATTNING OCH BÄSTA PRAXIS
# =============================================================================

print("11. SAMMANFATTNING OCH BÄSTA PRAXIS")
print("-" * 40)

print("""
FUNKTIONELL PROGRAMMERING I PYTHON - SAMMANFATTNING:

1. RENA FUNKTIONER:
   - Inga bieffekter
   - Deterministiska resultat
   - Lättare att testa och förstå

2. LAMBDA-FUNKTIONER:
   - Anonyma funktioner för enkla operationer
   - Använd sparsamt för läsbarhetens skull

3. INBYGGDA FUNKTIONER:
   - map(): Applicera funktion på alla element
   - filter(): Filtrera element baserat på villkor
   - sorted(): Sortera med anpassade kriterier
   - zip(): Kombinera flera iterables
   - reduce(): Reducera till ett värde
   - any()/all(): Logiska operationer

4. LIST COMPREHENSIONS:
   - Koncis och läsbar syntax
   - Ofta snabbare än traditionella loopar
   - Kan ersätta många map/filter-operationer

BÄSTA PRAXIS:
- Använd funktionell programmering för databehandling
- Kombinera tekniker för eleganta lösningar
- Prioritera läsbarhet över korthet
- Testa funktioner individuellt
- Använd type hints för klarhet
""")

if __name__ == "__main__":

    print("\n=== PROGRAM SLUTFÖRT ===")
    print("Detta program demonstrerar grundläggande funktionell programmering i Python.")
    print("Kör programmet för att se alla exempel och förklaringar!")