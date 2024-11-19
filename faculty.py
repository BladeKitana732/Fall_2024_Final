#faculty class 
class Faculty: 
    #attributes 
    def __init__(self, first_name, last_name):
        first_name = self.first_name
        last_name = self.last_name 
        courses = []

    #method 
    def assign_course(self, course): #also will need a dictionary here for key pair value of teacher name to course
        #assigns a course to faculty member and sets the course modules faculty attribute 
        if course not in self.courses: 
            self.courses.append(course)
            course.faculty = self
    
    def __str__(self):
        #returns a str representation of the Faculty instance 
        pass
