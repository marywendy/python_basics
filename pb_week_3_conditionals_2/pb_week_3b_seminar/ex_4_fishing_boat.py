budget = int(input())
season = input().capitalize()
number_of_fishers = int(input())

regular_price = 0

if season == "Spring":
    regular_price = 3000
elif season == "Summer" or season == "Autumn":
    regular_price = 4200
elif season == "Winter":
    regular_price = 2600

discount = 0

if number_of_fishers <= 6:
    discount = regular_price * 0.1
elif 7 <= number_of_fishers <= 11:
    discount = regular_price * 0.15
else:
    discount = regular_price * 0.25

price_after_discount = regular_price - discount

additional_discount = 0

if number_of_fishers % 2 == 0 and season != "Autumn":
     additional_discount = price_after_discount * 0.05

final_price = price_after_discount - additional_discount

money_left = budget - final_price

if budget >= final_price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")
