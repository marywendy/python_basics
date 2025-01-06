deposit_amount = float(input())
term_of_deposit = float(input())
annual_rate = float(input())/ 100

monthly_rate = deposit_amount * annual_rate / 12
rate_for_term_of_deposit = monthly_rate * term_of_deposit

final_deposit_amount = deposit_amount + rate_for_term_of_deposit

print(final_deposit_amount)
