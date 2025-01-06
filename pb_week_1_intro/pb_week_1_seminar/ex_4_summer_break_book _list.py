number_of_pages_to_read = int(input())
rate_per_hour = int(input())
number_of_days_to_complete_reading = int(input())

pages_per_hour = int(number_of_pages_to_read / rate_per_hour)

hours_per_day_to_read = int(pages_per_hour / number_of_days_to_complete_reading)

print(hours_per_day_to_read)
