# Vad är TDD?
# Test Driven Development
# Skriv tester innan du skriver koden som ska testas
# Red -> Green -> Refactor -> Repeat
# Innebär att du skriver ett test som misslyckas (Red)
# Sedan skriver du precis så mycket kod att testet går igenom (Green)
# Slutligen refaktorerar du koden för att göra den bättre (Refactor)
# Och upprepar processen (Repeat)

import pytest
from calculator import add, division

def test_add_two_numbers(): # Naming convention test_....
    assert add(2, 3) == 5
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, 0) == 1

def test_subtract():
    from calculator import subtract # Local import
    assert subtract(10, 3) == 7

def test_divide():
    assert division(8, 2) == 4
    assert division(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(5, 0)
