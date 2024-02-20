# Q.24 Write a Python program to convert a list to a tuple.

list=[]
n=int(input("Enter total element :"))
for i in range(n):
    list.append(input("value of list=")) 
print("list is ",list)    
print(type(list)) 
tu=tuple(list)
print(f"tuple is {tu}")
print(type(tu))