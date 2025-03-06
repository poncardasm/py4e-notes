"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 

https://www.py4e.com/tools/pythonauto/?PHPSESSID=fa0eaeade8b5d426587b03437148723d
"""
largest = None
smallest = None

while True:
  num = input("Enter a number: ")
  if num == "done":
    break

  try:
    n = int(num)
    if largest is None or n > largest:
      largest = n
    if smallest is None or n < smallest:
      smallest = n
  except:
    print("Invalid input")
    continue

print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")