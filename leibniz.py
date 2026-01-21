import math
iterations = int(input("Enter the number of iterations: "))
pioverfour = 0
numerator = 1
denominator = 1
for count in range(iterations):
    pioverfour += numerator / denominator
    numerator = -numerator
    denominator += 2
print("The approximation of pi is", pioverfour * 4)
print("Compare this to the computer's estimation: ", math.pi)
