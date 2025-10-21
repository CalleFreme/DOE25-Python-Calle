# Vecka 5: Funktionell Programmering och Debugging

Välkommen till vecka 5 av DOE25 Python-kursen! Denna vecka fokuserar vi på funktionell programmering i Python samt viktiga debugging-strategier som hjälper dig att skriva bättre kod och lösa problem mer effektivt.

## Vill du så kan du. Kan du så vill du.

## Repetition är kunskapens moder


## 📚 Innehåll

### Funktionell Programmering
- [Introduktion till funktionell programmering](#funktionell-programmering)
- [Rena funktioner (Pure Functions)](#rena-funktioner)
- [Lambda-funktioner](#lambda-funktioner)
- [Inbyggda funktioner för funktionell programmering](#inbyggda-funktioner)
- [List Comprehensions](#list-comprehensions)

### Debugging
- [Debugging-strategier](#debugging-strategier)
- [Vanliga fel och lösningar](#vanliga-fel-och-lösningar)
- [Verktyg för debugging](#debugging-verktyg)

## 🔧 Funktionell Programmering

### Vad är funktionell programmering?

Funktionell programmering är ett programmeringsparadigm som fokuserar på:

- **Funktioner som första klassens objekt** - Funktioner kan tilldelas till variabler, skickas som argument och returneras från andra funktioner
- **Immutability** - Undvikande av förändring av tillstånd efter att data skapats
- **Rena funktioner** - Funktioner utan bieffekter som alltid ger samma resultat för samma input
- **Funktionskomposition** - Bygga komplexa operationer genom att kombinera enkla funktioner

### Fördelar med funktionell programmering:

✅ **Förutsägbar kod** - Rena funktioner ger alltid samma resultat  
✅ **Lättare att testa** - Inga beroenden på extern tillstånd  
✅ **Mindre buggar** - Färre bieffekter betyder färre oväntade problem  
✅ **Bättre för parallellisering** - Immutable data är säkrare i multi-threaded miljöer  
✅ **Mer läsbar kod** - Deklarativ stil som beskriver VAD som ska göras

### Rena funktioner

En ren funktion uppfyller två kriterier:

1. **Deterministisk** - Samma input ger alltid samma output
2. **Inga bieffekter** - Modifierar inte externa variabler eller tillstånd

```python
# Ren funktion ✅
def add(x, y):
    return x + y

# Icke-ren funktion ❌
counter = 0
def increment():
    global counter
    counter += 1  # Bieffekt!
    return counter
```

### Lambda-funktioner

Lambda-funktioner är anonyma funktioner som kan definieras inline:

```python
# Lambda-syntax
lambda argument(er): uttryck

# Exempel
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda n: n % 2 == 0
```

**Använd lambda när:**
- Funktionen är kort och enkel
- Den används som argument till högre ordningens funktioner
- Du behöver en snabb, engångsfunktion

### Inbyggda funktioner

Python erbjuder flera kraftfulla inbyggda funktioner för funktionell programmering:

#### `map(function, iterable)`
Applicerar en funktion på alla element i en iterabel:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# Resultat: [1, 4, 9, 16, 25]
```

#### `filter(function, iterable)`
Filtrerar element baserat på ett villkor:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
# Resultat: [2, 4, 6, 8, 10]
```

#### `sorted(iterable, key=function)`
Sorterar med anpassade kriterier:

```python
words = ["python", "java", "go", "javascript"]
by_length = sorted(words, key=len)
# Resultat: ['go', 'java', 'python', 'javascript']
```

#### `zip(*iterables)`
Kombinerar element från flera iterables:

```python
names = ["Anna", "Erik", "Maria"]
ages = [25, 30, 22]
combined = list(zip(names, ages))
# Resultat: [('Anna', 25), ('Erik', 30), ('Maria', 22)]
```

#### `reduce(function, iterable[, initializer])`
Reducerar en sekvens till ett enda värde:

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
# Resultat: 15
```

#### `any(iterable)` och `all(iterable)`
Logiska operationer över samlingar:

```python
numbers = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in numbers))  # True - alla jämna
print(any(x > 5 for x in numbers))       # True - några > 5
```

### List Comprehensions

List comprehensions erbjuder ett koncist sätt att skapa listor:

```python
# Grundläggande syntax
[uttryck for element in iterabel if villkor]

# Exempel
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
```

**Fördelar med list comprehensions:**
- Mer läsbar än traditionella loopar
- Ofta snabbare prestanda
- Pythonic kod
- Kan ersätta många map/filter-operationer

## 🐛 Debugging-strategier

Debugging är en kritisk färdighet för alla programmerare. Här är de viktigaste strategierna:

### 1. Förstå problemet

Innan du börjar debugga:
- **Reproducera felet** - Se till att du kan få felet att uppstå konsekvent
- **Läs felmeddelandet** - Python ger ofta mycket användbar information
- **Identifiera vad som fungerade** - När slutade programmet att fungera?

### 2. Debugging-tekniker

#### Print-debugging
Den enklaste och ofta mest effektiva metoden:

```python
def complex_calculation(data):
    print(f"Input data: {data}")  # Debug-utskrift
    
    result = process_data(data)
    print(f"After processing: {result}")  # Debug-utskrift
    
    return result
```

#### Logging
För mer professionell debugging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_user_data(user_data):
    logger.debug(f"Processing data for user: {user_data.get('name')}")
    # ... kod här ...
    logger.info(f"Successfully processed user {user_data.get('name')}")
```

#### Assertions
För att verifiera antaganden:

```python
def divide(a, b):
    assert b != 0, "Division med noll är inte tillåten"
    assert isinstance(a, (int, float)), "a måste vara ett nummer"
    assert isinstance(b, (int, float)), "b måste vara ett nummer"
    return a / b
```

### 3. Använda debugger

Python inkluderar en inbyggd debugger (pdb):

```python
import pdb

def problematic_function(data):
    pdb.set_trace()  # Breakpoint här
    # Koden pausar här och du kan inspektera variabler
    result = complex_operation(data)
    return result
```

**pdb-kommandon:**
- `n` (next) - Nästa rad
- `s` (step) - Stega in i funktioner  
- `c` (continue) - Fortsätt körning
- `l` (list) - Visa kod omkring aktuell position
- `p variabel` - Skriv ut variabelvärde
- `q` (quit) - Avsluta debugger

### 4. Vanliga fel och lösningar

#### NameError
```python
# Problem: Variabel ej definierad
print(namn)  # NameError: name 'namn' is not defined

# Lösning: Definiera variabel först
namn = "Anna"
print(namn)
```

#### IndexError
```python
# Problem: Index utanför listans räckvidd
lista = [1, 2, 3]
print(lista[5])  # IndexError: list index out of range

# Lösning: Kontrollera listans längd
if len(lista) > 5:
    print(lista[5])
else:
    print("Index för stort")
```

#### KeyError
```python
# Problem: Nyckel finns inte i dictionary
person = {"namn": "Anna", "ålder": 25}
print(person["stad"])  # KeyError: 'stad'

# Lösning: Använd get() eller kontrollera nyckel
print(person.get("stad", "Okänd"))  # Returnerar "Okänd" om nyckel saknas
```

#### TypeError
```python
# Problem: Fel datatyp
tal = "5"
resultat = tal + 10  # TypeError: can only concatenate str to str

# Lösning: Konvertera datatyp
tal = int("5")
resultat = tal + 10
```

### 5. Debugging-verktyg

#### VS Code Debugger
- Sätt breakpoints genom att klicka i marginalen
- Använd F5 för att starta debugging
- F10 för step over, F11 för step into
- Inspektera variabler i Debug-panelen

#### IPython/Jupyter
```python
# Magic commands för debugging
%debug          # Starta debugger efter fel
%pdb on         # Automatisk debugger vid fel
%timeit kod     # Mät exekveringstid
%profile kod    # Profilera kodprestanda
```

#### Pylint/Flake8
Statisk kodanalys för att hitta potentiella problem:

```bash
# Installera
pip install pylint flake8

# Analysera kod
pylint my_file.py
flake8 my_file.py
```

### 6. Bästa praxis för debugging

#### Skriv testbar kod
```python
# Svår att testa
def process_user_input():
    # Svårare att testa eftersom den tar input
    name = input("Namn: ")
    age = int(input("Ålder: "))
    return calculate_something(name, age)

# Lättare att testa
def process_user_data(name, age):
    return calculate_something(name, age)

def get_user_input():
    name = input("Namn: ")
    age = int(input("Ålder: "))
    return process_user_data(name, age)
```

#### Använd enhetstester
```python
import unittest

class TestCalculations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
```

#### Dokumentera antaganden
```python
def calculate_bmi(weight, height):
    """
    Beräknar BMI (Body Mass Index).
    
    Args:
        weight (float): Vikt i kilogram (måste vara > 0)
        height (float): Längd i meter (måste vara > 0)
    
    Returns:
        float: BMI-värde
    
    Raises:
        ValueError: Om weight eller height är <= 0
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Vikt och längd måste vara positiva värden")
    
    return weight / (height ** 2)
```

## 📁 Filer i denna vecka

- `functional_programming.py` - Huvudfil med demonstrationer av funktionell programmering
- `README.md` - Denna fil med dokumentation och guidelines

## 🎯 Lärandemål

Efter denna vecka ska du kunna:

- ✅ Förstå grundläggande principer för funktionell programmering
- ✅ Skriva rena funktioner utan bieffekter
- ✅ Använda lambda-funktioner effektivt
- ✅ Tillämpa map, filter, reduce och andra funktionella verktyg
- ✅ Skriva eleganta list comprehensions
- ✅ Kombinera flera funktionella tekniker
- ✅ Identifiera och åtgärda vanliga fel
- ✅ Använda olika debugging-tekniker
- ✅ Skriva kod som är lättare att debugga

## 🚀 Övningar

1. **Funktionell databehandling** - Använd funktionella tekniker för att bearbeta dataset
2. **Text-analys** - Skapa funktioner för att analysera textfiler
3. **Debugging-utmaning** - Hitta och fixa buggar i given kod
4. **Performance-jämförelse** - Jämför prestanda mellan olika implementationer

## 📖 Ytterligare resurser

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Real Python: Functional Programming](https://realpython.com/python-functional-programming/)
- [Python Debugging Guide](https://docs.python.org/3/library/pdb.html)
- [Effective Debugging Strategies](https://realpython.com/python-debugging-pdb/)

---

**Lycka till med funktionell programmering och debugging!** 🐍✨