hour = int(input())
day = input().capitalize()

status = 0
if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday") and 10 <= hour <= 18:
    status = "open"
else:
    status = "closed"

print(status)