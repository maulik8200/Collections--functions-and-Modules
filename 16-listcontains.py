#Q.16 Write a Python program to check whether a list contains a sub list

list1=[] 
n=int(input("Enter total element :"))
for i in range(n):
    list1.append(input("value of list=")) 
print("original list=",list1)  
for i in list1:
    if len(list1) > 1:
        print("sublist is present in list")
        break 
    else:
        print("sub list is present not in list")