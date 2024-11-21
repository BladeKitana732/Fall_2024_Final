#courses class 
class Course: 
    #attributes 
    def __init__(self, title , faculty):
        title = self.title
        faculty = None #was advised on requirements to set this to None initially 

    #methods 
    def get_info(self, faculty, title): #needed to self to return information about course and its assigned faculy; still need a dictionary 
        #returns info about the course and assigned faculty 
        faculty_name = f"{self.faculty.first_name} {self.faculty.last_name}" if self.faculty else "None"
        return {"Course Name:" : self.title, "Faculty:" : faculty_name}
    
    def __str__(self):
        #returns a string representation of Course instance 
        faculty_name = f"{self.faculty.first_name} {self.faculty.last_name}" if self.faculty else "None"
        return f"Course: {self.title}, Faculty: {faculty_name}"