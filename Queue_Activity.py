from queue import LifoQueue

list_of_patient= LifoQueue()

def Enter_patient():
    patient = input("Enter the Name of the Patient: ")
    list_of_patient.put(patient)
    print("Patient Registered Successfully")

def Remove_patient():
    patient = input("Enter Patient Name: ")
    if patient in list_of_patient.queue:
        list_of_patient.queue.remove(patient)
        print("Patient Removed Successfully")
    else:
        print("Patient Not Registered")
def display_patient():
    if not list_of_patient.empty():
        for number , patient in enumerate(list_of_patient.queue):
            print(number + 1, ".", patient)
    else: 
        print(" No patients Registered yet")

while True :
    print("Menu")
    print("1. Register Patient")
    print("2. Remove Patient")
    print("3. Display Patients in Queue ")
    print("4. Exit ")

    choice = int(input("Enter the Number:"))

    if choice == 1:
        Enter_patient()
    elif choice == 2:
        Remove_patient()
    elif choice == 3 :
        display_patient()
    elif choice == 4 :
        print("Exiting the Program")
        break
    else:
        print("invalid Number Input")
        






