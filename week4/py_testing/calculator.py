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
