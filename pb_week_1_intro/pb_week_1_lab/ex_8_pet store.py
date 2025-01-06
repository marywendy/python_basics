DOG_FOOD = 2.5
CAT_FOOD= 4

containers_of_dog_food = int(input())
containers_of_cat_food = int(input())

calculations_for_dog_food = DOG_FOOD * containers_of_dog_food
calculations_for_cat_food = CAT_FOOD * containers_of_cat_food

total_pet_items = calculations_for_dog_food + calculations_for_cat_food

print(total_pet_items)
