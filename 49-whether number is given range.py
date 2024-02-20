#Q.49 Write a Python function to check whether a number is in a given range 
  
def num_range(num):  
    if num in range(0,50): 
        print(f" num of [{num}] in renge")     
    else :
        print(f"num of [{num}] is Out of range")
        
num=int(input("Enter num :"))
num_range(num)    

def is_in_range(num, upper, lower):
    return upper <= num <= lower