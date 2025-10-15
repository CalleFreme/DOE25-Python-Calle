def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def division(a, b):
    #return a // b # Heltalsdivision
    try:
        return a / b # Vanlig division
    except ZeroDivisionError:
        raise ValueError
    
while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    except ValueError:
        print("Invalid input, please enter numbers only.")