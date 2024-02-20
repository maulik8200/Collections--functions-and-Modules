# Q.29 Write a Python program to unzip a list of tuples into individual lists.

list1=[(1,2),(3,4),(8,9)]
list1=list(zip(*list1)) 
print(f"unzip list={list1}")