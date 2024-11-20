#university system class 
from student import Student
from faculty import Faculty
from course import Course
import csv

class UniversitySystem: 
    #attributes 
    def __init__(self, students, faculties, courses):
        students = []
        faculties = []
        courses = []

    #methods 
    def add_student(self, first_name, last_name): 
        #adds a student object to the list of students 
        student = Student(self, first_name = str, last_name = str):
        self.students.append(student)

    def add_faculty(self, first_name, last_name):
        print("test")

    def add_course(self, course_name):
        print("test")

    def save_students_to_csv(self, filename = "students.csv"):
        print("test")

