season = input()
group = input()
students = int(input())
nights = int(input())

price = 0

if group == "girls" or group == "boys":
    if season == "Winter":
        price = students * 9.60 * nights
    elif season == "Spring":
        price= students * 7.20 * nights
    elif season == "Summer":
        price= students * 15.00 * nights

elif group == "mixed":
    if season == "Winter":
        price= students * 10.00 * nights
    elif season == "Spring":
        price= students * 9.5 * nights
    elif season == "Summer":
        price= students * 20 * nights


if students >= 50:
    price -= price * 0.50
elif 20 <= students < 50:
    price -= price * 0.15
elif 10 <= students < 20:
    price -= price * 0.05

sport = ''

if group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"

elif group == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"

elif group == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {price:.02f} lv.")

