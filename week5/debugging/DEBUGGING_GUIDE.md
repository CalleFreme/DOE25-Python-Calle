# DEBUGGING DEMONSTRATION GUIDE

This guide explains the bugs in debug_demonstration.py and suggested debugging
techniques.

The program contains simple, realistic bugs that beginners commonly encounter.

## BUGS PRESENT (7 total)

### 1. **Division by Zero** (calculate_average function)
- **Bug**: Dividing by len(numbers) when list might be empty
- **Error**: ZeroDivisionError: division by zero
- **Demo**: Show how print() can reveal the problem
- **Fix**: Check if len(numbers) > 0 before dividing
- **Debugging tip**: Add `print(f"List length: {len(numbers)}")` before division

### 2. **Missing Dictionary Key** (get_student_grade function)
- **Bug**: Accessing grades_dict[student_name] when student might not exist
- **Error**: KeyError: 'David'
- **Demo**: Use print() to show what keys exist in the dictionary
- **Fix**: Use `grades_dict.get(student_name)` or check `if student_name in grades_dict`
- **Debugging tip**: Add `print(f"Available students: {list(grades_dict.keys())}")`

### 3. **Missing Return Statement** (count_vowels function)
- **Bug**: Function prints result but doesn't return it
- **Error**: Function returns None instead of count
- **Demo**: Show the difference between print() and return
- **Fix**: Add `return count` at the end
- **Debugging tip**: Add `print(f"Function returning: {count}")` before return

### 4. **Index Out of Range** (process_numbers function)
- **Bug**: Loop goes one step too far: `range(len(number_list) + 1)`
- **Error**: IndexError: list index out of range
- **Demo**: Print the values of `i` in each loop iteration
- **Fix**: Use `range(len(number_list))` without the +1
- **Debugging tip**: Add `print(f"Loop iteration {i}, list length: {len(number_list)}")`

### 5. **Empty String Indexing** (greet_user function)
- **Bug**: Accessing name[0] when name might be empty string
- **Error**: IndexError: string index out of range
- **Demo**: Show what happens with different string lengths
- **Fix**: Check `if len(name) > 0` before accessing name[0]
- **Debugging tip**: Add `print(f"Name length: {len(name)}, Name: '{name}'")`

### 6. **Division by Zero in Calculator** (simple_calculator function)
- **Bug**: Dividing by zero without checking
- **Error**: ZeroDivisionError: float division by zero
- **Demo**: Show how to validate inputs
- **Fix**: Check `if b != 0` before dividing
- **Debugging tip**: Add `print(f"Dividing {a} by {b}")`

### 7. **No Validation for Empty String** (count_vowels function)
- **Bug**: Not handling empty strings properly
- **Error**: No error, but unexpected behavior
- **Demo**: Show how empty strings behave in loops
- **Fix**: Add check for empty string at the start
- **Debugging tip**: Add `print(f"Text to process: '{text}', Length: {len(text)}")`

## DEBUGGING TECHNIQUES FOR BEGINNERS

### 1. Print Debugging (Start Here!)
Print debugging is the easiest way to see what's happening in your code.

```python
# Add prints to see variable values
print(f"The variable x is: {x}")
print(f"List has {len(my_list)} items")
print(f"About to process: {item}")

# Trace program flow
print("Starting function")
print("About to enter loop")
print("Finished processing")
```

**When to use**: Always start with print debugging - it's simple and effective!

### 2. VS Code Breakpoints (Visual Debugging)
VS Code's built-in debugger lets you pause and inspect your program.

**How to use**:
1. Click in the left margin (gutter) next to a line number to set a red dot (breakpoint)
2. Press F5 or click "Run and Debug" to start debugging
3. Program will pause at your breakpoint
4. Use the Variables panel to see all variable values
5. Use F10 to step to the next line, F11 to step into functions

**When to use**: When you need to see multiple variables at once, or step through code slowly

### 3. Reading Error Messages
Python gives helpful error messages - learn to read them!

```
Traceback (most recent call last):
  File "debug_demo.py", line 95, in main
    grade = get_student_grade("David", grades)
  File "debug_demo.py", line 25, in get_student_grade
    grade = grades_dict[student_name]
KeyError: 'David'
```

**How to read**:
- Start from the bottom: `KeyError: 'David'` tells you what went wrong
- Work upward: Line 25 in get_student_grade is where the error happened
- The key 'David' doesn't exist in the dictionary

## TEACHING STRATEGY

### For Each Bug:
1. **Run the program** and let students see the error
2. **Read the error message** together
3. **Add print statements** to understand what's happening
4. **Use VS Code debugger** to inspect variables
5. **Fix the bug** and test again

### Progressive Difficulty:
1. Start with obvious errors (division by zero)
2. Move to logic errors (missing return)
3. End with edge cases (empty strings)

### Student Activities:
- Let them predict what will happen before running code
- Have them add their own print statements
- Ask them to explain the error in their own words
- Practice setting breakpoints and using the debugger

## COMMON BEGINNER MISTAKES TO HIGHLIGHT

1. **Not checking for empty collections** before using them
2. **Forgetting return statements** in functions
3. **Off-by-one errors** in loops and indexing
4. **Not validating user input** or function parameters
5. **Assuming data exists** without checking first

## TIPS FOR EFFECTIVE DEBUGGING

1. **Start simple**: Use print() before fancy debuggers
2. **Be systematic**: Add prints at key points, not everywhere
3. **Test edge cases**: Empty lists, zero values, empty strings
4. **Read error messages**: They usually tell you exactly what's wrong
5. **Use meaningful variable names**: Makes debugging much easier
6. **Test small pieces**: Don't wait to test until everything is written