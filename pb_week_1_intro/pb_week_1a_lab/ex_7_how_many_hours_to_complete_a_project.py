HOURS_PER_PROJECT = 3

name = input()
number_of_projects = int(input())

total_hours = number_of_projects * HOURS_PER_PROJECT

print(f"The architect {name} will need {total_hours} hours to complete {number_of_projects} project/s.")
