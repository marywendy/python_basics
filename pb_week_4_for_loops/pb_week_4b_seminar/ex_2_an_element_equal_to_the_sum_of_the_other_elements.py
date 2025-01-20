how_many_numbers = int(input())

from sys import maxsize

max_number = -maxsize

total = 0

for _ in range(how_many_numbers):
    current_number = int(input())
    total += current_number
    if current_number > max_number:
        max_number = current_number
        
if max_number == total - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    total = abs(total - max_number)
    diff = abs(max_number - total)
    print(f"No\nDiff = {diff}")
