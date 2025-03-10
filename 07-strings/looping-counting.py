fruit = input('Enter a word: ')
count = 0

for letter in fruit:
  if(letter == 'r'):
    count += 1
print(f"Number of 'r' in {fruit} is {count}")