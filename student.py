#student class 
from course import Course

class Student:
    #attributes 
    def __init__(self, first_name, last_name, courses):
        first_name = self.first_name 
        last_name = self.last_name 
        courses = []

    #methods 
    def enroll(courses):
        if len(courses) <= 1 and courses[0] != "Intro to Python": 
            courses.append("Intro to Python")
            print(courses)
        elif len(courses) == 1 and courses[0] == "Intro to Python":
            courses.append(Course)
            print(courses)
        elif len(courses) >= 1 and courses[0] == "Intro to Python": 
            courses.append(Course)
            print(courses)
        elif len(courses) == 2 and courses[0] == "Intro to Python":
            courses.append(Student)
            print(courses)
        elif len(courses) == 3 and courses[0] == "Intro to Python":
            courses.append(Course)
            print("You have reached the max number of courses able to join", courses)

    def get_info():
        print("test")

student_dictionary = {} #needed to help store the key value pairs of id to student 

