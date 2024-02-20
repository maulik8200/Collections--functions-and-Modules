#Q.51 Write a Python function that checks whether a passed string is palindrome or not

def isPalindrome(str): 
    return str[0] == str[-1] 

str=input("Enter a string :")
ans = isPalindrome(str) 
  
if ans: 
    print([str],"string is palindrome")
else:
    print([str],"string is not a palindrome")