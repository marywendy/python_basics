chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_holiday = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

if is_holiday == "Y":
    chrysanthemum_price += chrysanthemum_price * 0.15
    rose_price += rose_price * 0.15
    tulip_price += tulip_price * 0.15

bouquet_price = chrysanthemums * chrysanthemum_price + roses * rose_price + tulips * tulip_price

if tulips > 7 and season == "Spring":
    bouquet_price -= bouquet_price * 0.05
if roses >= 10 and season == "Winter":
    bouquet_price -= bouquet_price * 0.10
if chrysanthemums + roses + tulips > 20:
    bouquet_price -= bouquet_price * 0.20

flower_arrangement = 2

final_price = bouquet_price + flower_arrangement

print(f"{final_price:.02f}")
