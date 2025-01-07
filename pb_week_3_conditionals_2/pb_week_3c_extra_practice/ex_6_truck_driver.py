MONTHS_IN_SEASON = 4
TAXES = 0.10

season = input()
km = float(input())

pay = 0

if km <= 5000:
    if season == "Spring" or season == "Autumn":
        pay = 0.75 * km * MONTHS_IN_SEASON
    elif season  == "Summer":
        pay = 0.90 * km * MONTHS_IN_SEASON
    elif season == "Winter":
        pay = 1.05 * km * MONTHS_IN_SEASON

elif 5000 < km <= 10000:
    if season == "Spring" or season == "Autumn":
        pay = 0.95 * km * MONTHS_IN_SEASON
    elif season  == "Summer":
        pay = 1.10 * km * MONTHS_IN_SEASON
    elif season == "Winter":
        pay = 1.25 * km * MONTHS_IN_SEASON

elif 1000 < km <= 20000:
    pay = 1.45 * km * MONTHS_IN_SEASON

pay -= pay * TAXES

print(f"{pay:.02f}")

