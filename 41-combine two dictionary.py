#Q.41 Write a Python program to combine two dictionary adding values for common keys.

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
for key in dict1:   
    if key in dict2: 
        dict2[key]+=dict1[key]
    else:
        dict2[key]=dict1[key] 
print(dict2)