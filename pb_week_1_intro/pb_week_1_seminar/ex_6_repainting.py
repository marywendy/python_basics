PROTECTIVE_PLASTIC = 1.5
PAINT = 14.5
PAINT_THINNER = 5
BAGS = 0.4

price_for_sq_m_of_protective_plastic = (int(input()) + 2) * PROTECTIVE_PLASTIC
price_for_liters_of_paint = int(input()) * 1.1 * PAINT
price_for_liters_of_paint_thinner = int(input()) * PAINT_THINNER

total_price_of_materials = price_for_sq_m_of_protective_plastic + price_for_liters_of_paint + price_for_liters_of_paint_thinner + BAGS
price_for_work_hours = int(input()) * total_price_of_materials * 0.3

final_amount = total_price_of_materials + price_for_work_hours

print(final_amount)

