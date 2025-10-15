#!/usr/bin/env python3
"""
Student Pairing Script
Reads student names from students.txt and creates random pairs.
Outputs the pairings to student_pairs.txt

GIVET: A list of student names in a text file (students.txt), one name per line.
SÖKT: A text file (student_pairs.txt) listing the randomly created pairs.
"""

import random
import os
from datetime import datetime


def read_students(filename):
    """Read student names from a text file, one name per line."""
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file: # file is a long string
            # Read lines and strip whitespace, filter out empty lines
            lines = file.readlines() # lines is a list of strings
            for line in lines: # line is name with newline: "Alexander\n"
                line = line.strip("\n") # line is a name: "Alexander"
                if line: # Handle empty lines: ""
                    students.append(line)

            # students = [line.strip() for line in file if line.strip()] # List comprehension to read and clean lines
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return []


def create_pairs(students):
    """Create random pairs from a list of students."""
    # Make a copy to avoid modifying the original list
    student_list = students.copy()
    
    # Shuffle the list randomly
    random.shuffle(student_list)
    
    pairs = [] # Will have structure: [ (name1, name2), (name3, name4), ... ]
    
    # Create pairs from the shuffled list
    # range(start, stop, step)
    for i in range(0, len(student_list), 2): # i goes 0, 2, 4, ..., len-1 or len-2
        if i + 1 < len(student_list):
            # Normal pair
            pairs.append((student_list[i], student_list[i + 1])) # pair is a tuple (name1, name2)
        else:
            # Odd number of students - last student gets paired with "No partner"
            pairs.append((student_list[i], "No partner"))
    
    return pairs


def write_pairs_to_file(pairs, filename):
    """Write the student pairs to a text file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write header with timestamp
            file.write(f"Student Pairs - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 60 + "\n\n")
            
            # Write pairs
            for i, (student1, student2) in enumerate(pairs, 1):
                file.write(f"Pair {i:2d}: {student1:<15} - {student2}\n")
            
            # pair = (name1, name2)
            # Could be (name1, "No partner")
            file.write(f"\nTotal pairs: {len(pairs)}")
            if any(pair[1] == "No partner" for pair in pairs):
                file.write(" (1 student without pair)")
            file.write("\n")
        
        print(f"Pairs successfully written to '{filename}'")
        return True
        
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")
        return False


def main():
    """Main function to orchestrate the pairing process."""
    input_file = "students.txt"
    output_file = "student_pairs.txt"
    
    print("Student Pairing Script")
    print("-" * 25)
    
    # Read students from file
    print(f"Reading students from '{input_file}'...")
    students = read_students(input_file)
    
    if not students:
        print("No students found. Exiting.")
        return
    
    print(f"Found {len(students)} students:")
    # Range gives a list of numbers from 0 to len(students)
    #for i in range(len(students)):
    #    print(f"  {i + 1:2d}. {students[i]}")

    # Enumerate gives both index and value
    for i, student in enumerate(students, 1): # i starts at 1, student is the name
        print(f"  {i:2d}. {student}")
    
    # Create random pairs
    print(f"\nCreating random pairs...")
    pairs = create_pairs(students)
    
    # Display pairs on screen
    print(f"\nGenerated pairs:")
    for i, (student1, student2) in enumerate(pairs, 1):
        print(f"  Pair {i:2d}: {student1:<15} - {student2}")
    
    # Write pairs to file
    print(f"\nWriting pairs to '{output_file}'...")
    success = write_pairs_to_file(pairs, output_file)
    
    if success:
        print("\nPairing complete! ✓")
    else:
        print("\nThere was an error writing the pairs to file. ✗")


if __name__ == "__main__":
    main()