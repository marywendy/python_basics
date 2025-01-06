BONITO_PRICE = 0.6
SCAD_PRICE = 0.8
MUSCLES_PRICE = 7.5

mackerel_price = float(input())
sprat_price = float(input())
bonito_weight = float(input())
scad_weight = float(input())
muscles_weight = int(input())

bonito_price = mackerel_price + mackerel_price * BONITO_PRICE
scad_price = sprat_price + sprat_price * SCAD_PRICE

total = bonito_price * bonito_weight + scad_price * scad_weight + MUSCLES_PRICE * muscles_weight

print(f'{total:.2f}')
