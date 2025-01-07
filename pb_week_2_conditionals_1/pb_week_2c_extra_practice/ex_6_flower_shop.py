from math import floor, ceil

MAGNOLIA = 3.25
HYACINTH = 4
ROSE = 3.5
CACTUS = 8
TAX = 0.05

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

total = magnolias * MAGNOLIA + hyacinths * HYACINTH + roses * ROSE + cacti * CACTUS
taxes = total * TAX
profit = total - taxes

diff = abs(profit - gift_price)
if profit >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')