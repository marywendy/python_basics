juniors = int(input())
seniors = int(input())
track = input()

junior_fee = 0
senior_fee = 0

if track == "trail":
    junior_fee = 5.50
    senior_fee = 7
elif track == "cross-country":
    junior_fee = 8
    senior_fee = 9.50
elif track == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
elif track == "road":
    junior_fee = 20
    senior_fee = 21.50

participants = juniors + seniors

if participants >= 50 and track == "cross-country":
    junior_fee -= junior_fee * 0.25
    senior_fee -= senior_fee * 0.25

proceeds = juniors * junior_fee + seniors * senior_fee
expenses = proceeds * 0.05

total_for_charity = proceeds - expenses

print(f"{total_for_charity:.02f}")
