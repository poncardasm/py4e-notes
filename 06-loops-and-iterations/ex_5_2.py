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