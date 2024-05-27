num_student=int(input("Enter the Number of the Students: "))

i=1
while i <= num_student:
    total_grade = 0
    num_subject = int(input(f"Enter the number of the subject for the students {i}: "))

    for j in range(1, num_subject + 1):
        grade = float(input(f"Enter subject{j} grade for the students {i}: "))
        total_grade += grade
        
        average_grade = total_grade / num_student
        print(f"Average Grade for students {i}: {average_grade: .2f}")

        i+=1

