#Q.64 Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

num=int(input("Enter Element num : "))
list1=[]  
for i in range(num):
    list1.append(float(input("Enter value :")))
print(list1)
print("maximum number :",max(list1))
print("minimum number :",min(list1))