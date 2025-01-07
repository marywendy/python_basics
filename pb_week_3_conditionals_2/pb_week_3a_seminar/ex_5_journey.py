budget = float(input())
season = input()

destination = ""
place_to_stay = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_to_stay = "Camp"
        money_spent = budget * 0.30
    elif season == "winter":
        place_to_stay = "Hotel"
        money_spent = budget * 0.70

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place_to_stay = "Camp"
        money_spent = budget * 0.40
    elif season == "winter":
        place_to_stay = "Hotel"
        money_spent = budget * 0.80

else:
    destination = "Europe"
    place_to_stay = "Hotel"
    money_spent = budget * 0.90

print(f"Somewhere in {destination}\n"
      f"{place_to_stay} - {money_spent:.2f}")