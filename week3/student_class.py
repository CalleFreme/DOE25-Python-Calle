
# Student class represents a student with a name and points.
import random

class Student:
    def __init__(self, name, points):
        """
        Initialize a new Student instance.
        :param name: The student's name (str)
        :param points: The student's points (int)
        """
        self.name = name
        self.points = points

    def add_points(self, x):
        """
        Add points to the student's total.
        :param x: Points to add (int)
        """
        self.points += x

    def has_passed(self):
        """
        Check if the student has passed (>= 50 points).
        :return: True if passed, False otherwise
        """
        if self.points >= 50:
            print(f"{self.name} has passed with {self.points} points.")
            return True
        else:
            print(f"{self.name} has not passed, only {self.points} points.")
            return False

#s1 = Student("Calle", 45)
#s2 = Student("Adam", 65)

no_students = 30 #int(input("How many students? "))
student_list = []

# [0, 1, 2,... no_student-1]
for i in range(no_students):
    #student_name = "Student" + str(i+1)
    student_name = f"Student #{i+1}"
    student_points = random.randint(0, 100)
    student = Student(student_name, student_points)
    student_list.append(student)

#random_student_idx = random.randint(0, no_students)
#print(student_list[random_student_idx])

#s1 = student_list[0]

print(student_list[0].add_points(15))
print(student_list[0].has_passed())

for student in student_list:
    student.has_passed()

#student_list = [Student("Calle", 45), Student("Adam", 65)]
