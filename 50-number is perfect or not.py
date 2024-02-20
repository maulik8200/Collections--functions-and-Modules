# Q.50 Write a Python function to check whether a number is perfect or not.

def perfect(n):
    sum = 0   
    for i in range(1, n):
        if(n % i == 0):  
            print(i)     
            sum = sum + i   
        else:
            pass   
    if (sum == n):  
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
n = int(input("Enter any number: "))
perfect(n)