# Q.32 Write a Python script to sort (ascending and descending) a dictionary by value.

dict1={'yash': 4, 'savan': 6, 'nimit': 2, 'raj': 5, 'sahil': 1, 'abhay': 3}
list1=list(dict1.keys()) 
list1.sort()     
dict2={}   
for i in list1:
    dict2.update({i:dict1[i]}) 
    
print("ascending dict",dict2)  

dict1={'yash': 4, 'savan': 6, 'nimit': 2, 'raj': 5, 'sahil': 1, 'abhay': 3}
list1=list(dict1.keys())  
list1.sort(reverse=True)   
dict2={}
for i in list1:
    dict2.update({i:dict1[i]}) 
    
print("descending dict",dict2)