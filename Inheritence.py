class person:
    def __init__(self, name, age, cid_number):
        self.name= name 
        self.age = age 
        self.cid_number = cid_number
    def walk (self):
        print(f"{self.name} is walking")
    def talk (self):
        print(f"{self.name} is Talking")
    def eat(self):
        print(f"{self.name} is eating ")
    def sleep (self):
        print(f"{self.name} is sleeping")

class teacher (person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    def Grade_students (self):
        print(f"{self.name} is grading the students ")
    def Attend_meeting (self):
        print(f"{self.name} is attending the meeting")

class students (person):
    def __init__(self, name, age, cid_number,Student_id, courses, year, GPA):
        super().__init__(name, age, cid_number)
        self.Student_id = Student_id
        self.courses = courses
        self.year = year
        self.GPA = GPA
    def study (self):
        print(f"{self.name} is studing")
    def Attend_class(self):
        print(f"{self.name} is attending a class")
    def write_exam(self):
        print(f"{ self.name} is writing the exam")


teacher1 = teacher("Sangay", 23, 1123, "physics", 23, "Mechanical", "Senior Lecturer")
student1 = students("Norbu", 11, 11234, 11223, "science", "second", 4.75)

teacher1.teach()
teacher1.Grade_students()
teacher1.Attend_meeting()

student1.study()
student1.Attend_class()
student1.write_exam()
