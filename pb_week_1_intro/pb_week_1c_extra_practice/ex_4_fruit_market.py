EURO = 1.94

veggies_price = float(input())
fruit_price = float(input())
veggies = int(input())
fruit = int(input())

total_bgn = veggies_price * veggies + fruit_price * fruit
total_eur = total_bgn / EURO

print(f'{total_eur:.2f}')