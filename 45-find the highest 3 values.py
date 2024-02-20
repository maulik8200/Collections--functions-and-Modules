# Q.45-->Write a Python program to find the highest 3 values in a dictionary

dict1={'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69 , 'G':82}
print("original Dictionary :",dict1)
print("Dictionary with 3 highest values:")
print("Keys Values")
list1=list(dict1.values()) 
list1.sort(reverse=True)
list1=list1[:3]       
for i in list1:
        for j in dict1.keys():
            if(dict1[j]==i):     
                print((j)+" : "+str(dict1[j]))