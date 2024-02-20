# Q.9 Write a Python function that takes two lists and returns true if they have at least one common member.

def comman_member(a,b): 
    for a in list1:
        for b in list2:
            if a == b:
                print(f"[two list is comman item is {a}]")
    else:
        print("[Two list are not comman]")
                
list1=[]
n=int(input("Enter element of list1:"))
for i in range(n):
    list1.append(int(input("value="))) 

list2=[]
n=int(input("Enter element of list2 :"))
for i in range(n): 
    list2.append(int(input("value="))) 
print("list1 is=",list1)
print("list2 is=",list2)
comman_member(list1,list2)      