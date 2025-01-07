water_resistance = 15
water_resistance_delay = 12.5

world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

delay = ((distance_in_meters
          // water_resistance)
         * water_resistance_delay)
johns_time = ((distance_in_meters * time_in_seconds_per_meter)
              + delay)

if world_record_in_seconds > johns_time:
    print(f"Yes, he succeeded! "
          f"The new world record is {johns_time:.2f} seconds.")
else:
    difference = abs(world_record_in_seconds - johns_time)
    print(f"No, he failed! "
          f"He was {abs(difference):.2f} seconds slower.")