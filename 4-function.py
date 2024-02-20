# Q.4 Write a python function to get the largest number,smallest num and sum of all from a list.

def number(a):
    print("largest number  =",max(list))
    print("smallest number =",min(list)) 
    sum=0
    for i in list:
        sum+=i
    print("all list sum is ",sum)   

list=[] 
n=int(input("Enter element :"))
for i in range(n): 
    list.append(int(input("value= "))) 
print("list is = ",list)        
number(list)