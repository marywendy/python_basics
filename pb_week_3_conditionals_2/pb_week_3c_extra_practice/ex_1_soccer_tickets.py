budget = float(input())
category = input()
number_people = int(input())

ticket_price = 0
if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

transportation = 0
if 1 <= number_people <= 4:
    transportation = budget * 0.75
elif 5 < number_people <= 9:
    transportation = budget * 0.60
elif 10 < number_people <= 24:
    transportation = budget * 0.50
elif 25 < number_people <= 49:
    transportation = budget * 0.40
else:
    transportation = budget * 0.25

tickets = number_people * ticket_price

money_left = budget - transportation - tickets

if money_left >= 0:
    print(f"Yes! You have {money_left:.02f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.02f} leva.")
