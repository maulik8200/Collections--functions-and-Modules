#Q.48 Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(num): 
    if num <= 0:       
        return 1
    else:
        return num*factorial(num-1) 
num=int(input("Enter int num :"))
print(factorial(num)) 

import math 
n=int(input("Enter int N :"))
print(math.factorial(n))