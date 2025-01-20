FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

number_of_tabs = int(input())
salary = float(input())

result = None

for _ in range(number_of_tabs):
    
    site = input().capitalize()
    
    if site == "Facebook":
        salary -= FACEBOOK_FINE
    elif site == "Instagram":
        salary -= INSTAGRAM_FINE
    elif site == "Reddit":
        salary -= REDDIT_FINE

    if salary <= 0:
        result = "You have lost your salary."
        break

else:
    result = f"{salary:.2f}"

print(result)
