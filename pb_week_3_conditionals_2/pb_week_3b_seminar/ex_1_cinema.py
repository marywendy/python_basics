type_of_showing = input().capitalize()
rows = int(input())
columns = int(input())

full_house = rows * columns

revenue = 0

if type_of_showing == "Premiere":
    revenue = 12 * full_house

elif type_of_showing == "Normal":
    revenue = 7.50 * full_house

elif type_of_showing == "Discount":
    revenue = 5.00 * full_house

print(f"{revenue:.2f} leva")


