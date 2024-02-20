#Q.15 Write a Python program to get unique values from a list

list1=[]
n=int(input("Enter total element :"))
for i in range(n):
    list1.append(input("value="))
print("original list=",list1) 
d_value=set(list1)
list=d_value
print("unique values=",list)