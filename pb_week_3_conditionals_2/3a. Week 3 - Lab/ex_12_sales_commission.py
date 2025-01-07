city = input().capitalize()
sale_volume = float(input())

commission = 0
error_condition = False

if city == "Sofia":
    if 0 <= sale_volume <= 500:
        commission = 0.05 * sale_volume
    elif 500 < sale_volume <= 1000:
        commission = 0.07 * sale_volume
    elif 1000 < sale_volume <= 10000:
        commission = 0.08 * sale_volume
    elif sale_volume > 10000:
        commission = 0.12 * sale_volume
    else:
        error_condition = True

elif city == "Varna":
    if 0 <= sale_volume <= 500:
        commission = 0.045 * sale_volume
    elif 500 < sale_volume <= 1000:
        commission = 0.075 * sale_volume
    elif 1000 < sale_volume <= 10000:
        commission = 0.1 * sale_volume
    elif sale_volume > 10000:
        commission = 0.13 * sale_volume
    else:
        error_condition = True

elif city == "Plovdiv":
    if 0 <= sale_volume <= 500:
        commission = 0.055 * sale_volume
    elif 500 < sale_volume <= 1000:
        commission = 0.08 * sale_volume
    elif 1000 < sale_volume <= 10000:
        commission = 0.12 * sale_volume
    elif sale_volume > 10000:
        commission = 0.145 * sale_volume
    else:
        error_condition = True

else:
    error_condition = True

if error_condition:
    print("error")
else:
    print(f"{commission:.2f}")