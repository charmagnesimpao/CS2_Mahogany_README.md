import math

# Makes the user input their numbers
x1 = float(input("Enter your x1:"))
x2 = float(input("Enter your x2:"))
y1 = float(input("Enter your y1:"))
y2 = float(input("Enter your y2:"))

# Subtracts the two as the first part of the distance formula
differenceOne = x2 - x1
differenceTwo = y2 - y1

# Adds an exponent on the differences
resultOne = math.pow(differenceOne, 2)
resultTwo = math.pow(differenceTwo, 2)

# Get's the square root of the two numbers we just multiplied
distance = math.sqrt(resultOne + resultTwo)

print("The distance between the two points inputted is", distance, "kilometers.")

#Reflection
"""
A library is more practical rather than doing the operations from scratch so that the code would not be too long and too complicated.
If libraries didn't exist, I would get confused and lost mid way due to the complexity of the code.
I specifically used math.pow and math.sqrt to get the results of exponents and the square root of specific numbers, I ended up using up less time due to these usefull functions.
"""