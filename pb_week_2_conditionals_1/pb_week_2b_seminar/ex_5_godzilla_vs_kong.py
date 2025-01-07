film_budget = float(input())
number_of_extras = int(input())
price_of_costume = float(input())

total_for_costumes = number_of_extras * price_of_costume

decore_percentage = 0.1
decor = film_budget * decore_percentage

costume_discount_percentage = 0.1

if number_of_extras > 150:
    total_for_costumes -= total_for_costumes * costume_discount_percentage

expenses = total_for_costumes + decor
remaining_budget = abs(film_budget - expenses)

if film_budget >= expenses:
    print(f"Action! \n"
          f"Wingard starts filming with {remaining_budget:.2f} leva left.")
elif film_budget < expenses:
    print(f"Not enough money! \n"
          f"Wingard needs {remaining_budget:.2f} leva more.")