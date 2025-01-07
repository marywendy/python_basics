flower = (input()).capitalize()
number_of_flowers = int(input())
budget = int(input())

flower_price = 0

if flower == "Roses":
    flower_price = 5
elif flower == "Dahlias":
    flower_price = 3.8
elif flower == "Tulips":
    flower_price = 2.8
elif flower == "Narcissus":
    flower_price = 3
elif flower == "Gladiolus":
    flower_price = 2.5

subtotal = flower_price * number_of_flowers

discount = 0

if flower == "Roses" and number_of_flowers > 80:
    discount = subtotal * 0.10
elif flower == "Dahlias" and number_of_flowers > 90:
    discount = subtotal * 0.15
elif flower == "Tulips" and number_of_flowers > 80:
    discount = subtotal * 0.15
elif flower == "Narcissus" and number_of_flowers < 120:
    discount = subtotal * 0.15
elif flower == "Gladiolus" and number_of_flowers < 80:
    discount = subtotal * 0.20

total = 0

if flower == "Roses" or flower == "Dahlias" or flower == "Tulips":
    total = subtotal - discount
else:
    total = subtotal + discount

money_left = budget - total

if flower == "Roses" or flower == "Dahlias" or flower == "Tulips" or flower == "Narcissus" or flower == "Gladiolus":
    if money_left >= 0:
        print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_left:.2f} leva left.")
    else:
        print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
else:
    print("")