'''#And oparator
#Example 1
x=5
print(x>3 and x<10) # True because both conditions are True

#Example 2
y=12
print(y>10 and y%5==0) # False because the second condition is False

#OR operator
#Example 1
x=5
print(x<3 or x>10) #False because both conditions are False

#Example 2
y=12
print(y<10 or y%2==0) #True because the second condition is True

#NOT operator
#Example 1
x=5
print(not(x>3 and x<10)) # False because the condition inside the not is True

#Example 2
y=12
print(not(y>10 and y%5==0)) # True because the condition inside the not is False

'''
x=int(input("Enter your age:"))
y=input("Are you a student? (yes/no): ").lower()

if x<=12 or ((x>=13 and x<=18) and y=="yes"):
    print("You are eligible for a discount on the movie ticket.")
else:
    print("You are not eligible for a discount on the movie ticket.")
