#must import the university system class 
from university_system import UniversitySystem

#input hardcoded approx 3 students and 3 faculty 
def main():
    #this code creates the UniversitySystem module instance 
    uni_sys = UniversitySystem(students = {}, faculties = {}, courses = {})

    #adding students 
    s1 = uni_sys.add_student("Teresa", "Malave", [])
    s2 = uni_sys.add_student("Nory", "Ramos", [])
    s3 = uni_sys.add_student("Bill", "Walton", [])

    #adding faculty 
    f1 = uni_sys.add_faculty("John", "Evers")
    f2 = uni_sys.add_faculty("Harry", "Daniels")
    f3 = uni_sys.add_faculty("Hadiseh", "Gooran")

    #adding courses 
    c1 = uni_sys.add_course("Biology")
    c2 = uni_sys.add_course("Calculus I")
    c3 = uni_sys.add_course("Intro to Python")

    #saving data to a csv file 
    uni_sys.save_students_to_csv()

    print("Student and course data have been sucessfully saved to 'students.csv'.")

if __name__ == "__main__":
    main()