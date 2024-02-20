#Q.60 Write a Python program to calculate the area of a trapezoid 

base_1=float(input("Enter base value:"))
base_2=float(input("Enter base value:"))
height=float(input("Enter height value:"))
area = ((base_1 + base_2) / 2) * height 
print(f"area of trapezoid :{area:.2f}")