#Q.5 How will you compare two list?

list1=[]   
n=int(input("Enter element of list1:"))
for i in range(n):   
    list1.append(int(input("value="))) 
print("list1 is=",list1) 

list2=[] 
n=int(input("Enter element of list2 :"))
for i in range(n): 
    list2.append(int(input("value="))) 
print("list2 is=",list2)

list1.sort() 
print("Ascending list1=",list1)
list2.sort()
print("Ascending list1=",list2)
print("\n")
if (list1 == list2): 
    print("[The list1 and list2 are equal]")
else:
    print("[The list1 and list2 are not equal]")