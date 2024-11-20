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
        student = Student(self, first_name = str, last_name = str)
        self.students.append(student)

    def add_faculty(self, first_name, last_name):
        #adds faculty object to list of faculties 
        faculty = Faculty(self, first_name = str, last_name = str)
        self.faculties.append(faculty)

    def add_course(self, course_name):
        #add course object to list of courses
        course = Course(title = str)
        self.courses.append(title)


    def save_students_to_csv(self, filename = "students.csv"):
        #saves each students name and enrolled courses to csv file 
        with open(filename, mode = "w", newline = '') as file: 
            writer = csv.writer(file)
            writer.writerow(["Student Name", "Enrolled Courses"])
            for student in self.students:
                info = student.get_info()
                writer.writerow(info)

