height = float(input("Enter the height from which the ball is dropped: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
distance = 0
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
for eachPass in range(bounces):
    distance += height
    height *= bounciness
    distance += height
print('\nTotal distance traveled is:', distance, 'units.')
