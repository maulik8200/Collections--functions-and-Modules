# Q.28 Write a Python program to remove an empty tuple(s) from a list of tuples.

list=[(10,'hello'),(  ),(23.3,22,74),(),('python','1:yash'),(25,54),(" ")]
print("orignal list =",list)
for i in list:  
    if(len(i)==0):
        list.remove(i) 
print("remove empty list =",list)