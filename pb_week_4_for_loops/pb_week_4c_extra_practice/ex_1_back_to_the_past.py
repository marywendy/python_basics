AGE = 18
FIRST_YEAR = 1800
YEARLY_SPENDING = 12000

inheritance = float(input())
final_year = int(input())

amount_spent = 0

for y in range(FIRST_YEAR, final_year + 1):
    if y % 2 == 0:
        amount_spent += YEARLY_SPENDING
    elif y % 2 != 0:
        amount_spent += YEARLY_SPENDING + AGE * 50
    AGE += 1

money_left = inheritance - amount_spent
if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")
