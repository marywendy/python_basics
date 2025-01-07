from math import floor, ceil

days = int(input())
food_left = int(input())
dog_food_daily = float(input())
cat_food_daily = float(input())
turtle_food_daily = float(input()) / 1000

food_needed = (dog_food_daily + cat_food_daily + turtle_food_daily) * days

diff = abs(food_left - food_needed)

if food_needed <= food_left:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')