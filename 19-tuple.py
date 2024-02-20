# Q.19 Write a Python program to create a tuple with different data types.

list=[]
n=int(input("Enter total element :"))
for i in range(n):
    list.append(input("value of list="))
print(list)    
    
print(type(list))
tuple=tuple(list) 
print(tuple)
print(type(tuple))