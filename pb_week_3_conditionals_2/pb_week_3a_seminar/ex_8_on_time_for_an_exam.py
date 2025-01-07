exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_in_minutes = exam_hour * 60 + exam_minute
arrival_in_minutes = arrival_hour * 60 + arrival_minute

difference = exam_in_minutes - arrival_in_minutes

status = ""
if difference < 0:
    status = "Late"
elif difference > 30:
    status = "Early"
else:
    status = "On time"

print(status)

hours = abs(difference) // 60
minutes = abs(difference) % 60

message = ""
if hours > 0:
    message = f"{hours}:{minutes:02} hours"
elif hours == 0:
    message = f"{minutes} minutes"

if difference < 0:
    message += f" after the start"
elif difference > 0:
    message += f" before the start"

print(message)