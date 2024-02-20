#Q.34 Write a Python script to check if a given key already exists in a dictionary.

dict1={'brand': 'apple','yash': 10,'model':'apple', '125': 1964, 'python': 10, 'year': 1964}
a=input("Enter key :")  
if a in dict1:   
    print("key is already exists")
elif a not in dict1:
    print("key not exists")
else:
    pass