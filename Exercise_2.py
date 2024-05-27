students_list=[]
student_dict={}
name=input("Enter your name here: ")
age=int(input("Enter your age here: "))
grade=int(input("Enter your grade here: "))
students_list.append(name)
student_dict[name]={"Age":age, "Grade":grade}
print("Student information added successfully!")
print(student_dict)
search_name=input("Enter the name of the student to search or simple enter t to skip: ")
if search_name in students_list:
    print(f"Student found! Name:{search_name},{student_dict[search_name]}")
else:
    print("Student not found!")

remove_name=input("Enter the name of the student to remove or simple enter t to skip: ")

if remove_name in students_list:
    students_list.remove(remove_name)
    del student_dict[remove_name]
    print("Student has been removed successfully!")
else:
    print("Student not found!")