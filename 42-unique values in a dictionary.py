#Q.42 Write a Python program to print all unique values in a dictionary.

dict1 = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1,"f":4}
values = set(dict1.values())
print(values)