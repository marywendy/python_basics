how_many_numbers_to_add = int(input())

total_sum = 0

for _ in range(how_many_numbers_to_add):
    numbers_to_add = int(input())
    total_sum += numbers_to_add

print(total_sum)

"""
# with list comprehensions (but w/ loops - easier to read):
value = [int(input()) for _ in range(int(input()))]
print(sum(value)
"""
