# Student Registration System

# NEEDS
# Datastruktur för studenter
# Loop för menyn
# Menyn har 3 val: 1. Add Student 2. List students 3. Quit

from studentregister_funcs import print_main_menu

test_student = {"name": "Adam", "age": "21"}
test_student2 = {"name": "Calle", "age": "22"}
test_student3 = {"name": "Bert", "age": "20"}
test_student4 = {"name": "David", "age": "23"}
test_student5 = {"name": "Erik", "age": "24"}
test_student6 = {"name": "Frank", "age": "25"}
test_student7 = {"name": "Gustav", "age": "26"}
test_student8 = {"name": "Hugo", "age": "27"}
test_student9 = {"name": "Ivan", "age": "28"}
test_student10 = {"name": "Johan", "age": "29"}
test_student11 = {"name": "Kalle", "age": "30"}
test_student12 = {"name": "Lars", "age": "31"}
student_list = [test_student, test_student2, test_student3, test_student4, test_student5, test_student6, test_student7, test_student8, test_student9, test_student10, test_student11, test_student12] # Default students

max_no_students_to_print = 10

def main():
    print("Welcome to the student register!")
    while True:
        print_main_menu()
        
        menu_choice = input("Choose 1-3: ")

        if menu_choice == "1":
            new_student_name = input("New student name: ")
            new_student_age = input("New student age: ")
            new_student_dict = {"name": new_student_name, "age": new_student_age}
            student_list.append(new_student_dict)

            print()
            print("New student created:")
            print(f"Name: {new_student_dict['name']}, Age: {new_student_dict['age']}")
            print()
            #print(f"Age: {new_student_dict["age"]}")
            # How to deal with nested strings:



        elif menu_choice == "2":
            index = 0
            while index < len(student_list):
                for student in student_list[index:index+10]:
                    print(f"Name: {student['name']}, Age: {student['age']}")
                index += 10
                if index < len(student_list):
                    cont = input("Print next 10 students? (y/n): ")
                    if cont.lower() != 'y':
                        break

        elif menu_choice == "3":      
            print("Students: ")
            print(student_list)
            quit()
        else:
            print("Choice not valid. Please choose a menu 1-3.")

if __name__ == "__main__":
    main()
    