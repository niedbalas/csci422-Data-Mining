"""
Author: S. Niedbala
Date Created: 1/21/26
Purpose: To take user input and calculate the diameter, circumference, and area of a circle
"""

#Welcome and User Input

radius = float(input("Enter the radius of the circle: "))
diameter = 2 * radius
circumference = 2 * radius * 3.14
area = 3.14 * radius ** 2

print("Diameter:      ", diameter)
print("Circumference: ", circumference)
print("Area:          ", area)
