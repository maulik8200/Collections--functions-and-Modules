# Q.11 Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(list1):
    list1=set(list1)
    set1=list(list1)
    print(set1)
list1=[]
n=int(input("Enter element of list1:"))
for i in range(n): 
    list1.append(int(input("value="))) 
unique(list1)