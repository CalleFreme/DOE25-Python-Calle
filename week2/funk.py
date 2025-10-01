'''
Förstå varför funktioner används.

Känna till syntaxen för att definiera och anropa en funktion.

Förstå parametrar, returvärden och scope.

Träna på att refaktorera kod till funktioner.
'''



# Nested strings:
print("This is a quote by Uncle Bob: \"Clean code is a code that is easy to read.\"")
print("This is a quote by Uncle Bob: 'Clean code is a code that is easy to read.'")

# Varför funktioner?
# - Återanvändbarhet - Reusability
# Om vi har logik som används på flera ställen, samla den logiken på en plats, och återanvänd!
def greet(name): # Function definition
    if name.isalpha() == True:
        return f"Hello, {name}!"
    else:
        print("Not a valid name")
        return
    
greeting = greet("Ada") # Function call
print(greeting)

# - Struktur
def read_user():
    return input("Name? ")

def main():
    name = read_user()
    greeting_message = greet(name)
    print(greeting_message)

# - Enklare att läsa
def calculate_discount(price, rate):
    i = 0
    discounted_price = price * (1 - rate)
    return discounted_price

calculate_discount(100, 0.2)
calculate_discount(120, 0.2)
calculate_discount(100, 0.4)
calculate_discount(140, 0.9)

# - Testbarhet
def square(x):
    return x * x

def test_square():
    assert square(2) == 4
    assert square(10) == 100
    assert square(-3) == 9

test_square()
print()

# - Undvika upprepning (DRY - Don't Repeat Yourself)
# Refaktorerar upprepad kod in i en enstaka funktion för att undvika dubbla förekomster och buggar.
def print_heading(text):
    print("-"*len(text))
    print(text)
    print("="*len(text))

header_text1 = input("Enter a header text: ")
print_heading(header_text1)

header_text2 = input("Enter a header text: ")
print_heading(header_text2)

# - Scope (lokala variabler)
def f():
    x = 10 # Lokal variabel

y = 5 # Global variabel


# - Modularisering
#project/
#    -- tasks/
#        -- main.py
#        -- helper_functions.py
#    -- README.md

def say_hello(user_name, extra_message="No message"): # extra_message is optional parameter
    print(f"Hello user {user_name} - {extra_message}")

def get_name_length(name):
    length = len(name)
    return length

name = input("Your name: ")

name1 = "Berit"
say_hello(name1, "Vad fin du är") # Anrop/call function
len1 = get_name_length(name1)
print(f"Length of name {name1} is: {len1}")

name2 = "Adam"
say_hello(name2, "Du är snäll")
len2 = len(name2)
print(f"Length of name {name2} is: {len2}")

name3 = "Isak"
say_hello()

print()
print("Hello world")
print("Hello world again", end=", ")



def f(x):
    y = x + 1
    return y

def square(x):
    y = x * x
    return y

first_square = square(2)
second_square = square(3)
third_square = square(4)

print(first_square)

squared_square = square(square(first_square))

print(squared_square)
