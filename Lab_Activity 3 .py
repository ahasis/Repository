
age = int(input("Enter Age: "))
student =input("Are Your a Student? (yes/no): ")
if age <= 12:
    print("You are Eligible for a Free Ticket")
elif 13<age<18 and student == 'yes':
    print("You are Eligible for a Student Discount")
else: 
    print("You are not Elligible for the free ticket")