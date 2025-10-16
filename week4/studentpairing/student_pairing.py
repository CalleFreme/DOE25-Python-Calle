#!/usr/bin/env python3
"""
Student Grouping Script
Reads student names from students.txt and creates random groups of specified size.
Outputs the groups to student_pairs.txt (or student_groups.txt for larger groups).

GIVET: A list of student names in a text file (students.txt), one name per line.
SÖKT: A text file listing the randomly created groups with user-specified group size.
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


def create_groups(students, group_size=2):
    """Create random groups from a list of students with specified group size."""
    if group_size < 1:
        raise ValueError("Group size must be at least 1")
    
    # Make a copy to avoid modifying the original list
    student_list = students.copy()
    
    # Shuffle the list randomly
    random.shuffle(student_list)
    
    groups = [] # Will have structure: [ [name1, name2, ...], [name3, name4, ...], ... ]
    
    # Create groups from the shuffled list
    for i in range(0, len(student_list), group_size):
        group = student_list[i:i + group_size]
        groups.append(group)
    
    return groups


def write_groups_to_file(groups, filename, group_size):
    """Write the student groups to a text file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write header with timestamp
            group_name = "Pairs" if group_size == 2 else "Groups"
            file.write(f"Student {group_name} - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 60 + "\n")
            file.write(f"Group size: {group_size}\n\n")
            
            # Write groups
            for i, group in enumerate(groups, 1):
                if group_size == 2 and len(group) == 2:
                    # Special formatting for pairs (backwards compatibility)
                    file.write(f"Pair {i:2d}: {group[0]:<15} - {group[1]}\n")
                elif group_size == 2 and len(group) == 1:
                    # Single student in a pair
                    file.write(f"Pair {i:2d}: {group[0]:<15} - No partner\n")
                else:
                    # General group formatting
                    file.write(f"Group {i:2d}: {', '.join(group)}\n")
            
            # Write summary
            total_students = sum(len(group) for group in groups)
            file.write(f"\nTotal groups: {len(groups)}\n")
            file.write(f"Total students: {total_students}\n")
            
            # Check for incomplete groups
            incomplete_groups = [group for group in groups if len(group) < group_size]
            if incomplete_groups:
                file.write(f"Incomplete groups: {len(incomplete_groups)}\n")
        
        print(f"Groups successfully written to '{filename}'")
        return True
        
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")
        return False


def get_group_size():
    """Get the desired group size from user input."""
    while True:
        try:
            size = input("Enter group size (default is 2 for pairs): ").strip()
            if not size:  # Empty input, use default
                return 2
            size = int(size)
            if size < 1:
                print("Group size must be at least 1. Please try again.")
                continue
            return size
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to orchestrate the grouping process."""
    input_file = "students.txt"
    
    print("Student Grouping Script")
    print("-" * 25)
    
    # Read students from file
    print(f"Reading students from '{input_file}'...")
    students = read_students(input_file)
    
    if not students:
        print("No students found. Exiting.")
        return
    
    print(f"Found {len(students)} students:")
    for i, student in enumerate(students, 1):
        print(f"  {i:2d}. {student}")
    
    # Get desired group size
    print()
    group_size = get_group_size()
    
    # Determine output filename
    if group_size == 2:
        output_file = "student_pairs.txt"
    else:
        output_file = "student_groups.txt"
    
    # Create random groups
    group_name = "pairs" if group_size == 2 else "groups"
    print(f"\nCreating random {group_name} of size {group_size}...")
    groups = create_groups(students, group_size)
    
    # Display groups on screen
    print(f"\nGenerated {group_name}:")
    for i, group in enumerate(groups, 1):
        if group_size == 2 and len(group) == 2:
            print(f"  Pair {i:2d}: {group[0]:<15} - {group[1]}")
        elif group_size == 2 and len(group) == 1:
            print(f"  Pair {i:2d}: {group[0]:<15} - No partner")
        else:
            members = ", ".join(group)
            print(f"  Group {i:2d}: {members}")
    
    # Show summary
    total_complete_groups = len([g for g in groups if len(g) == group_size])
    incomplete_groups = len([g for g in groups if len(g) < group_size])
    
    print(f"\nSummary:")
    print(f"  Total students: {len(students)}")
    print(f"  Complete {group_name}: {total_complete_groups}")
    if incomplete_groups > 0:
        print(f"  Incomplete groups: {incomplete_groups}")
    
    # Write groups to file
    print(f"\nWriting {group_name} to '{output_file}'...")
    success = write_groups_to_file(groups, output_file, group_size)
    
    if success:
        print(f"\nGrouping complete! ✓")
    else:
        print(f"\nThere was an error writing the {group_name} to file. ✗")


if __name__ == "__main__":
    main()