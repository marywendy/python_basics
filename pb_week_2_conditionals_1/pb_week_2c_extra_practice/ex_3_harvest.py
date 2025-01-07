from math import floor, ceil

GRAPES_FOR_WINE_PERCENT = 0.4
GRAPES_NEEDED_FOR_LITER_WINE = 2.5

sq_m = int(input())
grapes_yield_per_sq_m = float(input())
wine_needed = int(input())
workers = int(input())

total_grapes = grapes_yield_per_sq_m * sq_m
grapes_for_wine = total_grapes * GRAPES_FOR_WINE_PERCENT
wine_produced = grapes_for_wine / GRAPES_NEEDED_FOR_LITER_WINE
diff = abs(wine_needed - wine_produced)

if wine_produced < wine_needed:
    print(f'It will be a tough winter! '
          f'More {floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! '
          f'Total wine: {floor(wine_produced)} liters.')
    print(f'{abs(ceil(diff))} liters left -> '
          f'{ceil(diff / workers)} liters per person.')