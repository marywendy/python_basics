PRICE_OF_PEN_PACKETS = 5.80
PRICE_OF_MARKER_PACKETS = 7.20
PRICE_OF_CLEANER_BOTTLES = 1.20


number_of_pen_packets = int(input()) * PRICE_OF_PEN_PACKETS
number_of_marker_packets = int(input()) * PRICE_OF_MARKER_PACKETS
number_of_cleaner_bottles = int(input()) * PRICE_OF_CLEANER_BOTTLES
discount = int(input()) / 100

purchase_total_before_discount = number_of_pen_packets + number_of_marker_packets + number_of_cleaner_bottles
discount_price = purchase_total_before_discount * discount
purchase_total_after_discount = purchase_total_before_discount - discount_price

print(purchase_total_after_discount)
