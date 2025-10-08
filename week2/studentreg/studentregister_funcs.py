def print_main_menu():
    print("--MENU--")
    print("1. Add student")
    print("2. List students")
    print("3. Quit program")

def add_new_student(students):
    new_student_name = input("New student name: ")
    new_student_age = input("New student age: ")
    new_student_dict = {"name": new_student_name, "age": new_student_age}
       
    students.append(new_student_dict)
    return students, new_student_dict