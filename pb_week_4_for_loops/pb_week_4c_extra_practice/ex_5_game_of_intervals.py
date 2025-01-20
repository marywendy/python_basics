moves = int(input())

result = 0

digits = 0
teens = 0
twenties = 0
thirties = 0
forties = 0
invalid = 0

for _ in range(moves):
    num = int(input())
    if 0 <= num < 10:
        digits += 1
        result += num * 0.20
    elif 10 <= num < 20:
        teens += 1
        result += num * 0.30
    elif 10 <= num < 30:
        twenties += 1
        result += num * 0.40
    elif 30 <= num < 40:
        thirties += 1
        result += 50
    elif 40 <= num <= 50:
        forties += 1
        result += 100
    else:
        invalid += 1
        result /= 2

total = digits + teens + twenties + thirties + forties + invalid

digits_percentile = digits / total * 100
teens_percentile = teens / total * 100
twenties_percentile = twenties / total * 100
thirties_percentile = thirties / total * 100
forties_percentile = forties / total * 100
invalid_percentile = invalid / total * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {digits_percentile:.2f}%\n"
      f"From 10 to 19: {teens_percentile:.2f}%\n"
      f"From 20 to 29: {twenties_percentile:.2f}%\n"
      f"From 30 to 39: {thirties_percentile:.2f}%\n"
      f"From 40 to 50: {forties_percentile:.2f}%\n"
      f"Invalid numbers: {invalid_percentile:.2f}%")
