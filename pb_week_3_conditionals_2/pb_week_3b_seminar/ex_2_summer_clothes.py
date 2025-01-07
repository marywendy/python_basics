temperature =  int(input())
time_of_day = input().capitalize()

clothes = ''
shoes = ''

if 10 <= temperature <= 18:
    if time_of_day == "Morning":
        clothes = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        clothes = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Evening":
        clothes = "Shirt"
        shoes = "Moccasins"

elif 18 < temperature <= 24:
    if time_of_day == "Morning":
        clothes = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        clothes = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Evening":
        clothes = "Shirt"
        shoes = "Moccasins"

else:
    if time_of_day == "Morning":
        clothes = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        clothes = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        clothes = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {clothes} and {shoes}.")