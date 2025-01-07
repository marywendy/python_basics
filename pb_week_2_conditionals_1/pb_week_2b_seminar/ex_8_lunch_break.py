name_of_series = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration * 1/8
time_for_rest = break_duration * 1/4

extra_time_left = (break_duration
                   - episode_duration
                   - time_for_lunch
                   - time_for_rest)

from math import ceil

if extra_time_left >= 0:
    print(f"You have enough time to watch {name_of_series} "
          f"and left with {ceil(extra_time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, "
          f"you need {ceil(abs(extra_time_left))} more minutes.")
