hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes
increased_minutes =  total_minutes + 15
new_hours = increased_minutes // 60

if new_hours == 24:
    new_hours = 0

new_minutes = increased_minutes % 60

if new_minutes < 10:
    new_minutes = f"0{new_minutes}"

print(f"{new_hours}:{new_minutes}")