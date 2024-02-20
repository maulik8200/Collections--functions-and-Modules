#Q.62 Write a Python program to calculate surface volume and area of a cylinder

pi=3.14
height = float(input('Height of cylinder: '))
radius = float(input('Radius of cylinder: '))
volume = pi * radius * radius * height
sur_area = ((2*pi*radius) * height) + ((pi*radius**2)*2)  
print(f"voluam is:{volume:.2f}")
print(f"area of a cylinder:{sur_area:.2f}")