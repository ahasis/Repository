
student_list = []
student_info = {}

def Add_student ():
    student_name = input("Enter Student name: ")
    age = int(input("Enter Your Age: "))
    grade = int(input("Enter Your garde: "))
    student_list.append(student_name)
    student_info[student_name] = {"ages" : age, "grades" : grade }
    print("Student Information Added Successfully")
    print("Thank you")
    

def search_student():
    name = input("Entet the name of the Student: ")
    if name in student_list:
        print(f"{name}\nStudent Information:\n {   student_info[name]}")
    else:
        print(" Student not Recorded ")

def remove_student():
    name = input("Enter the Name of the student : ")
    if name in student_list:
        student_list.remove(name)
        del student_info[name]
    else: 
        print("Student Not registered in the lsit")

while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3.Get Information about the Student")
    print("4. Exit system")
    option = int(input("Enter the Number: "))
    if option == 1:
        Add_student()
    elif option == 2:
        remove_student()
    elif option == 3:
        search_student()
    elif option == 4:
        break
    else:
        print("Wrong Input")


