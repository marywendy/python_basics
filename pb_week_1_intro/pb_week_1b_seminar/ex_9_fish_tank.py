length = int(input())   # in cm
width = int(input())    # in cm
height = int(input())   # in cm
percent_sand = float(input()) / 100

calculations_to_liters = length * width*height / 1000 # 1 cubic cm is 0.001 cubic dm

water_in_fish_tank = calculations_to_liters - calculations_to_liters * percent_sand

print(water_in_fish_tank)


