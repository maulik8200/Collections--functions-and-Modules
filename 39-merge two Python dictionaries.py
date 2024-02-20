#Q.39 Write a Python script to merge two Python dictionaries

dict1 = {'bike': 'unicorn', 'brand': 'apple'}
dict2 = {'x': 3001, 'y': 200}
dict3={} 

for i in (dict1,dict2):
    dict3.update(i)
print(dict3)    