BROTHER_TAKES = 1

age = int(input())
washer_price = float(input())
price_per_toy = int(input())

total_money = 0
number_of_toys = 0
each_even_bd = 10

for age in range(1, age + 1):
    
    if age % 2 == 0:
        total_money += each_even_bd - BROTHER_TAKES
        each_even_bd += 10
    else:
        number_of_toys += 1

total_money += number_of_toys * price_per_toy

diff = total_money - washer_price
if washer_price <= total_money:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {abs(diff):.2f}")
