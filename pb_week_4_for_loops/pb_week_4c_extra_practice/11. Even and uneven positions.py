total_num = int(input())

odd_sum = 0
even_sum = 0
odd_max = float('-inf')
odd_min = float('inf')
even_max = float('-inf')
even_min = float ('inf')

for n in range(1, total_num + 1):
    nums = float(input())
    if n % 2 != 0:
        odd_sum += nums
        if nums > odd_max:
            odd_max = nums
        if nums < odd_min:
            odd_min = nums
    elif n % 2 == 0:
        even_sum += nums
        if nums > even_max:
            even_max = nums
        if nums < even_min:
            even_min = nums

print(f"OddSum={odd_sum:.2f},")
if odd_sum == 0:
    print(f"OddMin=No,\nOddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},\nOddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_sum == 0:
    print(f"EvenMin=No,\nEvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")