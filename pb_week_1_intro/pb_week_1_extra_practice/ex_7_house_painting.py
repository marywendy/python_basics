GREEN_PAINT_COVERS = 3.4
RED_PAINT_COVERS = 4.3
WINDOW_AREA = 1.5 ** 2
FRONT_DOOR = 1.2 * 2

x = float(input())
y= float(input())
h = float(input())

front_wall = x ** 2 - FRONT_DOOR
back_wall = x ** 2
side_walls = (y * x - WINDOW_AREA) * 2
front_roof_sides = x * h
side_roof_sides = y * x * 2

green_paint_needed = (front_wall + back_wall + side_walls) / GREEN_PAINT_COVERS
red_paint_needed = (front_roof_sides + side_roof_sides) / RED_PAINT_COVERS

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')