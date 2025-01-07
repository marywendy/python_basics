TRAIN = 0.06
BUS = 0.09
TAXI_INITIAL_FEE = 0.70
TAXI_DAY_FAIR = 0.79
TAXI_NIGHT_FAIR = 0.90

distance = int(input())
time_of_day = input()

best_fair = 0

if distance < 20:
    taxi_fair = 0
    if time_of_day == 'day':
        taxi_fair = TAXI_INITIAL_FEE + distance * TAXI_DAY_FAIR
    elif time_of_day == 'night':
        taxi_fair = TAXI_INITIAL_FEE + distance * TAXI_NIGHT_FAIR
    best_fair = taxi_fair
elif 20 <= distance < 100:
    bus_fair = distance * BUS
    best_fair = bus_fair
elif distance >= 100:
    train_fair = distance * TRAIN
    best_fair = train_fair

print(f'{best_fair:.2f}')


