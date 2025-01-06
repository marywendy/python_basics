CHICKEN_MEAL = 10.35
FISH_MEAL = 12.40
VEGETARIAN_MEAL = 8.15
DELIVERY = 2.5

chicken_meal_total = int(input()) * CHICKEN_MEAL
fish_meal_total = int(input()) * FISH_MEAL
vegetarian_meal_total = int(input()) * VEGETARIAN_MEAL

food_total = chicken_meal_total + fish_meal_total+vegetarian_meal_total
dessert = food_total * 0.2

total_bill = food_total + dessert + DELIVERY

print(total_bill)
