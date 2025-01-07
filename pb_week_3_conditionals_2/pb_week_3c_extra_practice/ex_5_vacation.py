budget = float(input())
season = input()

price = 0
location = ""
accommodations = ""

if budget <= 1000:
    accommodations = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    accommodations = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60

else:
    accommodations = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodations} - {price:.02f}")