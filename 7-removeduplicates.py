# Q.7 Write a Python program to remove duplicates from a list.

list= [10,50,40,30,30,10,302,10]
print("original list ", list)
set1=set(list)  
print(set1)
print("List After removing duplicates ", set1)
print("------------------------------------")
list1 = []   
for i in list:   
    if i not in list1:  
        list1.append(i)  
print("List After removing duplicates ", list1)