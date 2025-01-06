PRICE_PER_SQ_M = 7.61
DISCOUNT_RATE = 0.18

sq_meters = float(input())

price_before_discount = sq_meters * PRICE_PER_SQ_M
discount_price = price_before_discount * DISCOUNT_RATE

price_after_discount = price_before_discount - discount_price

print(f"The final price is: {price_after_discount} lv.")
print(f"The discount is: {discount_price}")
