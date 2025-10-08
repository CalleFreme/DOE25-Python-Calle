def validate_age(age):
    try:
        if int(age) > 0:
            return True
        else:
            False
    except ValueError:
        return False
    
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
    
if validate_age("19"):
    print("Valid age")
else:
    print("Invalid age")

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

# With if statements:
age = input("Enter your age: ")
if age.isnumeric():
    if int(age) < 18:
        print("You must be 18 or older.")
    else:
        print("Welcome in to the club!")
else:
    print("Please enter valid number value")

def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0

try:
    a = int(input("First number: "))
    b = int(input("Divide by second number: "))
    result = division(a, b)
    print(result)
except ValueError:
    print("Only numbers allowed")

num_list = [1, 5, 2, 6]
# index:    0  1  2  3
try:
    print(num_list[5])
except IndexError:
    print("That index does not exist in this list")

print(num_list[-2])

# TypeError example:
try:
    result = "5" + 3
except TypeError:
    print("You can't add a string and an integer!")