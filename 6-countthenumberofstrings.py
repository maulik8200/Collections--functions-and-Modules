# Q.6 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

count=0
list1=[]   
n=int(input("Enter element of list1:"))
for i in range(n):   
    list1.append(input("value=")) 
print("list1 is=",list1) 

for i in list1: 
    if len(i) >= 2 and i[0] == i[-1]:  
        print(i) 
        count+=1   
print("the given words are=",[count])