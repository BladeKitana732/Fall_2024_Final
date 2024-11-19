#student class 
class Student:
    #attributes 
    def __init__(self, first_name, last_name):
        first_name = self.first_name 
        last_name = self.last_name 
        courses = []

    #methods 
    def enroll(self, course):
        #enrolls student if not already enrolled 
        if course not in self.courses: 
            self.courses.append(course)

    def get_info(self):
        #returns the information about student and their courses combining first and last name together and joining returning a list of name and course_names
        student_name = f"{self.first_name} {self.last_name}"
        course_names = ', '.join("test")
        return [student_name, course_names]




