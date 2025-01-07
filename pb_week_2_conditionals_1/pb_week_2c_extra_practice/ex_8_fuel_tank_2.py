GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93
GASOLINE_DISCOUNT = 0.18
DIESEL_DISCOUNT = 0.12
GAS_DISCOUNT = 0.08
FINAL_DISCOUNT1_PERCENT = 0.08
FINAL_DISCOUNT2_PERCENT = 0.1

fuel_type = input()
fuel_amount = float(input())
discount_card = input()

total = 0

if discount_card == "Yes":
    if fuel_type == 'Gasoline':
        total = fuel_amount * (GASOLINE - GASOLINE_DISCOUNT)
        
    elif fuel_type == "Diesel":
        total = fuel_amount * (DIESEL - DIESEL_DISCOUNT)
        
    elif fuel_type == "Gas":
        total = fuel_amount * (GAS - GAS_DISCOUNT)
        
elif discount_card == "No":
    if fuel_type == 'Gasoline':
        total = fuel_amount * GASOLINE
        
    elif fuel_type == "Diesel":
        total = fuel_amount * DIESEL
        
    elif fuel_type == "Gas":
        total = fuel_amount * GAS

if 20 <= fuel_amount <= 25:
    total = total - total * FINAL_DISCOUNT1_PERCENT
    
elif fuel_amount > 25:
    total = total - total * FINAL_DISCOUNT2_PERCENT

print(f'{total:.2f} lv.')
