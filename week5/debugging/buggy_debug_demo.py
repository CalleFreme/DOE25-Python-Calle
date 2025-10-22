"""
buggy_debug_demo.py

A deliberately buggy file to practice debugging strategies. The file contains
several small, obvious bugs and a few that are slightly trickier. The goal is
for students to fix them using print-debugging and breakpoints.

Hints are provided in comments. Don't forget to run tests and use the
Python debugger (pdb) or VS Code breakpoints.

Run as: python buggy_debug_demo.py
"""

from typing import List


def get_even_numbers(nums: List[int]):
    """Return a list of even numbers from nums. Bug: uses wrong condition."""
    evens = []
    for n in nums:
        if n % 2 == 1:
            evens.append(n)
    return evens


def compute_average(nums: List[float]):
    """Return the average of nums. Bug: division by zero if empty list."""
    total = sum(nums)
    return total / len(nums)


def find_max_index(nums: List[int]):
    """Return the index of the maximum value. Bug: returns value, not index."""
    if not nums:
        return None
    max_val = max(nums)
    return max_val


def format_person_info(name: str, age: int):
    """Return a formatted string. Bug: wrong order and missing type conversion."""
    return "{0} is {1} years old".format(age, name)


def main():
    data = [1, 2, 3, 4, 5]

    print("All numbers:", data)

    # Debugging exercise 1: fix get_even_numbers
    evens = get_even_numbers(data)
    print("Even numbers (should be [2,4]):", evens)

    # Debugging exercise 2: fix compute_average
    avg = compute_average([])
    print("Average (should handle empty list):", avg)

    # Debugging exercise 3: fix find_max_index
    idx = find_max_index([5, 2, 8, 3])
    print("Index of max (should be 2):", idx)

    # Debugging exercise 4: fix format_person_info
    info = format_person_info("Kalle", 29)
    print("Person info:", info)


if __name__ == "__main__":
    # Students should set breakpoints or add prints to find/fix issues.
    main()
