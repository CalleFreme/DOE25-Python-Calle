'''
Förstå varför funktioner används.

Känna till syntaxen för att definiera och anropa en funktion.

Förstå parametrar, returvärden och scope.

Träna på att refaktorera kod till funktioner.
'''

# Varför funktioner?
# - Återanvändbarhet
# - Struktur
# - Enklare att läsa
# - Testbarhet
# - Undvika upprepning (DRY - Don't Repeat Yourself)
# - Scope (lokala variabler)
# - Modularisering


def say_hello(user_name, extra_message=""): # Function definition, extra_message is optional parameter
    print(f"Hello user {user_name} - {extra_message}")
    name_length = len(user_name)
    return name_length

name = input("Your name: ")

len1 = say_hello("Calle", "Vad fin du är") # Anrop/call function
print(f"Length of name Calle is: {len1}")

len2 = say_hello("Adam", "Du är snäll")
print(f"Length of name Adam is: {len2}")

len3 = say_hello(name)
print(f"Length of name {name} is: {len3}")

def f(x):
    y = x + 1
    return y

def calc_square(x):
    y = x * x
    return y

first_square = square(2)
second_square = square(3)
third_square = square(4)

print(first_square)

squared_square = square(square(first_square))

print(squared_square)
