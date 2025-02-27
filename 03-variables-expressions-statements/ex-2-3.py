"""
2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data.
"""

# Prompt the user for hours worked
hrs = input("Enter Hours: ")

# Prompt the user for the rate per hour
rate = input("Enter Rate: ")

# Convert both inputs to floats
hrs = float(hrs)
rate = float(rate)

# Calculate the pay
pay = hrs * rate

# Print the result using an f-string
print(f"Pay: {pay}")