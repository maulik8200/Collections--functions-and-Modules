#Q.38 Write a Python program to check multiple keys exists in a dictionary

dict1={"processor":"Window","course":"python","fees":25000,"year":2023,"book":"vscode"}
print(dict1)
for key in ["year","bike","fees"]:
    if key in dict1: 
        print(f"This key [{key}] are present") 
    else:
        print(f"This key [{key}] are not present")