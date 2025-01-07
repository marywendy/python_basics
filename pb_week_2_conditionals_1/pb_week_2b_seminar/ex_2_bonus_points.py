bonus_up_to_100 = 5
bonus_between_100_and_1000_in_percent = 0.2
bonus_above_1000_in_percent = 0.1

additional_points_for_even_number = 1
additional_points_for_number_ending_in_5 = 2

initial_points = int(input())
bonus_points = 0

if initial_points <= 100:
    bonus_points += bonus_up_to_100
elif 100 < initial_points <= 1000:
    bonus_points += initial_points * bonus_between_100_and_1000_in_percent
elif initial_points > 1000:
    bonus_points += initial_points * bonus_above_1000_in_percent

if initial_points % 2 == 0:
    bonus_points += additional_points_for_even_number
elif initial_points % 10 == 5:
    bonus_points += additional_points_for_number_ending_in_5

print(bonus_points)
print (initial_points + bonus_points)

