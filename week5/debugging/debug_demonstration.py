"""
debug_demonstration.py

Simple program with basic bugs for instructor debugging demonstrations.
This is for showing debugging techniques to Week 5 students:
- print debugging
- VS Code breakpoint debugging
- Reading error messages

Run as: python debug_demonstration.py
"""


def calculate_average(numbers):
    """Calculate average of a list of numbers. Has a bug."""

    total = sum(numbers)
    average = total / len(numbers)
    return average


def get_student_grade(student_name, grades_dict):
    """Get a student's grade from a dictionary. Has a bug."""

    grade = grades_dict[student_name]
    return grade


def count_vowels(text):
    """Count vowels in a text string. Has bugs."""
    vowels = "aeiou"
    count = 0
    

    for letter in text:
        if letter.lower() in vowels:
            count = count + 1
    

    print(f"Found {count} vowels")



def process_numbers(number_list):
    """Process a list of numbers. Has indexing bug."""
    results = []
    

    for i in range(len(number_list) + 1):
        results.append(number_list[i] * 2)
    
    return results


def greet_user(name):
    """Greet a user by name. Has string bug."""

    first_letter = name[0]
    greeting = f"Hello, {first_letter}. Nice to meet you!"
    return greeting


def simple_calculator(a, b, operation):
    """Simple calculator with division bug."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Unknown operation"


def main():
    """Main function to demonstrate the bugs."""
    print("=== Debugging Demo for Week 5 Students ===")
    
    # Demo 1: Empty list average
    print("\n1. Testing average calculation:")
    try:
        numbers = []  # Empty list will cause division by zero
        avg = calculate_average(numbers)
        print(f"Average: {avg}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    
    # Demo 2: Missing student
    print("\n2. Testing student grades:")
    grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
    try:
        grade = get_student_grade("David", grades)  # David not in dictionary
        print(f"David's grade: {grade}")
    except KeyError as e:
        print(f"Error: Student {e} not found")
    
    # Demo 3: Empty string vowel counting
    print("\n3. Testing vowel counting:")
    text = ""  # Empty string
    count = count_vowels(text)  # This will return None because of missing return
    print(f"Vowel count result: {count}")
    
    # Demo 4: Index out of range
    print("\n4. Testing number processing:")
    numbers = [1, 2, 3]
    try:
        doubled = process_numbers(numbers)
        print(f"Doubled numbers: {doubled}")
    except IndexError as e:
        print(f"Error: {e}")
    
    # Demo 5: Empty name greeting
    print("\n5. Testing greeting:")
    try:
        message = greet_user("")  # Empty string will cause index error
        print(message)
    except IndexError as e:
        print(f"Error: {e}")
    
    # Demo 6: Division by zero in calculator
    print("\n6. Testing calculator:")
    try:
        result = simple_calculator(10, 0, "divide")  # Division by zero
        print(f"10 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    
    print("\nDebugging demonstration complete!")


if __name__ == "__main__":
    # Students can add print statements here to debug:
    # print("Starting program...")
    
    # Or set a breakpoint here in VS Code
    main()