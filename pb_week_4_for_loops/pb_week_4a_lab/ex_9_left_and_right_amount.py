numbers_for_each_side = int(input())
left_sum = 0
right_sum = 0

for _ in range(numbers_for_each_side):
    left_numbers = int(input())
    left_sum += left_numbers

for _ in range(numbers_for_each_side):
    right_numbers = int(input())
    right_sum += right_numbers

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
