fruit = input()
day = input().capitalize()
quantity = float(input())

price = 0

if (day == "Monday"
        or day == "Tuesday"
        or day == "Wednesday"
        or day == "Thursday"
        or day == "Friday"):

    if fruit == "banana":
        price = 2.5 * quantity
    elif fruit == "apple":
        price = 1.20 * quantity
    elif fruit == "orange":
        price = 0.85 * quantity
    elif fruit == "grapefruit":
        price = 1.45 * quantity
    elif fruit == "kiwi":
        price = 2.70 * quantity
    elif fruit == "pineapple":
        price = 5.50 * quantity
    elif fruit == "grapes":
        price = 3.85 * quantity

elif day == "Saturday" or day == "Sunday":

    if fruit == "banana":
        price = 2.70 * quantity
    elif fruit == "apple":
        price = 1.25 * quantity
    elif fruit == "orange":
        price = 0.90 * quantity
    elif fruit == "grapefruit":
        price = 1.60 * quantity
    elif fruit == "kiwi":
        price = 3.00 * quantity
    elif fruit == "pineapple":
        price = 5.60 * quantity
    elif fruit == "grapes":
        price = 4.20 * quantity

if price != 0:
    print(f"{price:.2f}")

else:
    print("error")
