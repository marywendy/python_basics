SECONDS_IN_MINUTE = 60

first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time_in_seconds = first_time + second_time + third_time

calc_to_minutes = total_time_in_seconds // SECONDS_IN_MINUTE
remaining_seconds = total_time_in_seconds % SECONDS_IN_MINUTE

if remaining_seconds < 10:
    print(f"{calc_to_minutes}:0{remaining_seconds}")

else:
    print(f"{calc_to_minutes}:{remaining_seconds}")