x=int(input("Enter the number you want the multiplication of: "))
y=int(input("Enter the limit up to which you want the multiplication table to be generated: "))

for i in range(1,y+1):
    print(f"{x} x {i} = {x*i} ")
    
