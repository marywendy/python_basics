stadium_capacity = int(input())
fans = int(input())

a = 0
b = 0
v = 0
g = 0

for _ in range(fans):
    sector = input()
    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1

total_fans = a + b + v + g

a_percentile = a / total_fans * 100
b_percentile = b / total_fans * 100
v_percentile = v / total_fans * 100
g_percentile = g / total_fans * 100

fans_to_capacity = total_fans / stadium_capacity * 100

print(f"{a_percentile:.2f}%\n"
      f"{b_percentile:.2f}%\n"
      f"{v_percentile:.2f}%\n"
      f"{g_percentile:.2f}%\n"
      f"{fans_to_capacity:.2f}%")