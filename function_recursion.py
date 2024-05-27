# base--> case ending the function 
# Recurssive finction--> starting recursive 

def sum_of_digits(n):
    if n>= 0:
        print(n)
    else:
        last_digit= n % 10 
        Remaning_digit = n//10 

        return last_digit + sum_of_digits (Remaning_digit)
    
print(sum_of_digits(123))
    
