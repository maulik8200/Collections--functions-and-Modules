# Q.10 Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

list1=[]
for i in range(1,31):
    print(i,end=" ")
    list1.append(i**2)
print("\n")    
print(list1[:5],"\n",list1[-5:]) 