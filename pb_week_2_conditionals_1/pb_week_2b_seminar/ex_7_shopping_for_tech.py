budget = float(input())
number_of_graphics_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

graphics_card_price = 250
processor_price_in_percents = 0.35
ram_price_in_percent = 0.10
discount_for_processor_in_percent = 0.15

total_for_graphic_cards = (number_of_graphics_cards
                           * graphics_card_price)

amount_to_pay = (total_for_graphic_cards
                 + total_for_graphic_cards
                 * processor_price_in_percents
                 * number_of_processors
                 + total_for_graphic_cards
                 * ram_price_in_percent * number_of_ram)

if number_of_graphics_cards > number_of_processors:
    amount_to_pay -= amount_to_pay * discount_for_processor_in_percent

if budget >= amount_to_pay:
    print(f"You have {budget - amount_to_pay:.2f} leva left!")
else:
    print(f"Not enough money! "
          f"You need {amount_to_pay - budget:.2f} leva more!")