import random 

secret_number = random.randrange(1, 10)
no_chances = 3 

def welcome_page():
    print("\nWelcome to the Number Guessing Game")
    print(f"You have {no_chances} chances to get the Correct Number.")

def recursion_function(no_chances):
    if no_chances >= 1:
        sel_no = int(input("Enter Your Guess Number: "))
        
        if sel_no == secret_number:
            print("Congratulations! You made the right guess.")
        else:
            print("Unfortunately, your guess is incorrect.")
            print(f"You have {no_chances - 1} chances left")
            recursion_function(no_chances - 1)

    else:
        print("Sorry, you have run out of your chances!")
        print(f"The Correct number is {secret_number}. ")

welcome_page()
recursion_function(no_chances) # You forgot to give the argument in the list.
print(f"The the memory address of the {secret_number} is : {id(secret_number)}")
