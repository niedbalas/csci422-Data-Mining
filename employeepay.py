
# Request the inputs
wage = float(input("Enter the wage: $"))  
regularHours = float(input("Enter the regular hours: "))  
overtimeHours = float(input("Enter the overtime hours: "))  

# Compute the result
totalPay = regularHours * wage + overtimeHours * wage * 1.5

# Display the result
print("The total weekly pay is $" + str(round(totalPay, 2)))
