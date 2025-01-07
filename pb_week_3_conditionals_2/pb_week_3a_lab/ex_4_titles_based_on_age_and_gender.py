age = float(input())
gender = input()
title = 0
if gender == "f":
    if age >= 16:
        title = "Ms."
    else:
        title = "Miss"
elif gender == "m":
    if age >= 16:
        title = "Mr."
    else:
        title = "Master"
print(title)