WORK_SPACE_L = 120
WORK_SPACE_W = 70
HALLWAY_WIDTH = 100
DOOR_TAKES_UP = 1
DESK_TAKES_UP = 2

length = float(input()) * 100
width = float(input()) * 100

available_width = width - HALLWAY_WIDTH

rows = length // WORK_SPACE_L
desks_per_row = available_width // WORK_SPACE_W

total_work_spaces = rows * desks_per_row - (DOOR_TAKES_UP + DESK_TAKES_UP)

print(total_work_spaces)