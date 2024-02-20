# Q.47 Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.  
# Sample string: 'w3resource' 
# Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

str1= 'w3resource'
dict1={}  
for i in str1:
    if i in dict1: 
        dict1[i]+=1
    else:             
        dict1[i]=1 
print(dict1)