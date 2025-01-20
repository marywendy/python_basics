VAN = 200
TRUCK = 175
TRAIN = 120

shipments = int(input())

average_price_per_ton = 0
van_tons = 0
truck_tons = 0
train_tons = 0

for _ in range(shipments):
    tons_per_shipment = int(input())
    if tons_per_shipment < 4:
        van_tons += tons_per_shipment
    elif 4 <= tons_per_shipment <= 11:
        truck_tons += tons_per_shipment
    elif tons_per_shipment >= 12:
        train_tons += tons_per_shipment

total_tons = van_tons + truck_tons + train_tons

average_price_per_ton = (van_tons * VAN + truck_tons * TRUCK + train_tons * TRAIN) / total_tons

van_percentage = van_tons / total_tons * 100
truck_percentage = truck_tons / total_tons * 100
train_percentage = train_tons / total_tons * 100

print(f"{average_price_per_ton:.2f}\n"
      f"{van_percentage:.2f}%\n"
      f"{truck_percentage:.2f}%\n"
      f"{train_percentage:.2f}%")