vacation = float(input())

puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

number_of_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

puzzle_price = 2.60 * puzzles
talking_doll_price = 3 * talking_dolls
teddy_bear_price = 4.10 * teddy_bears
minion_price = 8.20 * minions
truck_price = 2 * trucks

total_price = (puzzle_price
               + talking_doll_price
               + teddy_bear_price
               + minion_price + truck_price)

discount = 0

if number_of_toys >= 50:
    discount = total_price * 0.25

price_after_discount = total_price - discount

rent = price_after_discount * 0.1
profit = price_after_discount - rent

money_left_for_vacation = abs(profit - vacation)

if profit >= vacation:
    print(f"Yes! {money_left_for_vacation:.2f} lv left.")
else:
    print(f"Not enough money! "
          f"{money_left_for_vacation:.2f} lv needed.")

