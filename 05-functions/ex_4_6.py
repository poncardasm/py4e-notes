"""
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
Do not name your variable sum or use the sum() function.
"""

def computepay(h, r):
    if h > 40:
        reg = h * r
        oth = (h - 40.0) * (r * 0.5)
        return reg + oth
    else:
        return h * r

# Function to validate numeric input
def get_valid_input(prompt):
    while True:
        try:
            # Try to convert the input to a float
            value = float(input(prompt))
            return value
        except ValueError:
            # If conversion fails, print an error message and prompt again
            print("Invalid input. Please enter a numeric value.")

# Get valid inputs for hours and rate
hr = get_valid_input("Enter Hours: ")
rate = get_valid_input("Enter Rate: ")

# Compute and print the pay
p = computepay(hr, rate)
print("Pay", p)