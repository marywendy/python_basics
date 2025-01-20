numbers_in_total = int(input())

limit1 = 200
limit2 = 400
limit3 = 600
limit4 = 800

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for n in range(numbers_in_total):
    current_number = int(input())

    if current_number < limit1:
        p1 += 1 / numbers_in_total * 100
    if limit1 <= current_number < limit2:
        p2 += 1 / numbers_in_total * 100
    if limit2 <= current_number < limit3:
        p3 += 1 / numbers_in_total * 100
    if limit3 <= current_number < limit4:
        p4 += 1 / numbers_in_total * 100
    if current_number >= limit4:
        p5 += 1 / numbers_in_total * 100

print(f"{p1:.2f}%\n"
      f"{p2:.2f}%\n"
      f"{p3:.2f}%\n"
      f"{p4:.2f}%\n"
      f"{p5:.2f}%")
