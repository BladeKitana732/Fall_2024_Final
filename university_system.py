#university system class 
from student import Student
from faculty import Faculty
from course import Course
import csv

class UniversitySystem: 
    #attributes 
    def __init__(self, students, faculties, courses):
        students = Student.get_info()
        faculties = Faculty.assign_course()
        courses = Course.get_info()

    #methods 
    def add_student(first_name, last_name): 
        print("test")

    def add_faculty(first_name, last_name):
        print("test")

    def add_course(course_name):
        print("test")

    def save_students_to_csv(filename = "students.csv"):
        print("test")


