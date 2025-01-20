WATER = 20
INTERNET = 15

months = int(input())

water_total = WATER * months
internet_total = INTERNET * months
electricity_total = 0 * months  # * months has to be here not inside the loop
other_expenses = 0

for _ in range(months):
    electricity = float(input())
    electricity_total += electricity
    other_expenses += (WATER + INTERNET + electricity) * 1.20
    # I can't add these outside the loop. It has to be inside

total = water_total + internet_total + electricity_total + other_expenses
monthly_average = total / months

print(f"Electricity: {electricity_total:.2f} lv\n"
      f"Water: {water_total:.2f} lv\n"
      f"Internet: {internet_total:.2f} lv\n"
      f"Other: {other_expenses:.2f} lv\n"
      f"Average: {monthly_average:.2f} lv")
