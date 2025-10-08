# Validerar ålder
def validate_age(age):
    try:
        if int(age) > 0: # Vi använder is-sats för att kontrollera om åldern är positiv
            return True
        else:
            False
    except ValueError: # Om konvertering till int misslyckas
        return False

    
if validate_age("19"):
    print("Valid age")
else:
    print("Invalid age")



def validate_menu_choice(choice, options):
    # choice : string input = 1 or 2 or 3
    # options : list of options = ["1. First option", "2. Second option", "3. Third option"]
    try:
        if int(choice) > 0:
            menu_option = options[int(choice-1)]
        else:
            raise IndexError
    except IndexError:
        print(f"Choice not in range of options. There are {len(options)} possible options")
    except ValueError:
        print(f"Choice must be a number between 1 and {len(options)}")

# Med try-except:
try:
    age = int(input("Enter your age: "))
    if age < 18:
        print("You must be 18 or older.")
    else:
        print("Welcome in to the club!")
except ValueError:
    print("Please enter a valid numeric value.")
except IndexError:
    print("Please enter an index value")

# Samma logik fast med if-sats och isnumeric():
age = input("Enter your age: ")
if age.isnumeric():
    if int(age) < 18:
        print("You must be 18 or older.")
    else:
        print("Welcome in to the club!")
else:
    print("Please enter valid number value")


# ZeroDivisionError exempel:
def division(a, b):
    # Vi kan lägga try-except inuti funktionen:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0

# Vi kan också välja att lägga try-except runt anropet av funktionen:
try:
    a = int(input("First number: "))
    b = int(input("Divide by second number: "))
    result = division(a, b)
    print(result)
except ValueError:
    print("Only numbers allowed")

# IndexError exempel:
num_list = [1, 5, 2, 6]
# index:    0  1  2  3
try:
    print(num_list[5]) # Finns inget index 5 i listan! Får index out range, d.v.s. IndexError
except IndexError:
    print("That index does not exist in this list")

print(num_list[-2]) # Negativa index gör att vi räknar baklänges från slutet av listan. Vad blir utskriften?

# TypeError exempel:
try:
    result = "5" + 3
except TypeError:
    print("You can't add a string and an integer!")