pool_volume = int(input())
first_pipe_flow_rate = int(input())
second_pape_flow_rate = int(input())
amount_of_time_employee_out = float(input())

combined_flow_rate = first_pipe_flow_rate + second_pape_flow_rate

volume_filled_while_employee_out = combined_flow_rate * amount_of_time_employee_out
percentage_of_pool_filled_while_employee_out = volume_filled_while_employee_out / pool_volume * 100

liters_extra_or_needed = abs(pool_volume - volume_filled_while_employee_out)
percentage_of_water_delivered_by_first_pipe = first_pipe_flow_rate / combined_flow_rate * 100
percentage_of_water_delivered_by_second_pipe = second_pape_flow_rate / combined_flow_rate * 100

if volume_filled_while_employee_out <= pool_volume:
    print(f"The pool is {percentage_of_pool_filled_while_employee_out:.2f}% full."
          f"Pipe 1: {percentage_of_water_delivered_by_first_pipe:.2f}%. "
          f"Pipe 2: {percentage_of_water_delivered_by_second_pipe:.2f}%.")
else:
    print(f"For {amount_of_time_employee_out} hours the pool overflows with {liters_extra_or_needed} liters.")
