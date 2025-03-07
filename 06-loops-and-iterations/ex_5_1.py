count = 0
total = 0.0

while True:
  sval = input('Enter a number: ')
  if sval == 'done':
    break

  try:
    fval = float(sval)
    total += fval
    count += 1
  except:
    print('Invalid input')
    continue

print(f'\nTotal: {total}')
print(f'Count: {count}')
print(f'Average: {total / count}')