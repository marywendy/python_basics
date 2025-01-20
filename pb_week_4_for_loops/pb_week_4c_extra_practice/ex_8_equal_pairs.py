pairs = int(input())

max_sum = float('-inf')
min_sum = float('inf')

sums_list = []
diff_list = []

for _ in range(pairs):
    first_num = int(input())
    second_num = int(input())
    sum_num = first_num + second_num
    if sum_num > max_sum:
        max_sum = sum_num
    if sum_num < min_sum:
        min_sum = sum_num
    sums_list.append(sum_num)
for s in range(1, len(sums_list)):
    current_sum = sums_list [s]
    previous_sum = sums_list [s - 1]
    diff = abs(current_sum - previous_sum)
    diff_list.append(diff)

diff_tuple = tuple(diff_list)
if max_sum == min_sum:
    print(f"Yes, value={max_sum}")
else:
    print(f"No, maxdiff={max(diff_tuple)}")
