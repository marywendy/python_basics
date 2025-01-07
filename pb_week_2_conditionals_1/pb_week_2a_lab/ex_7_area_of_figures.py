from math import pi

geometrical_figure = input()

area = 0

if geometrical_figure == "square":
    a = float(input())
    area = a ** 2
    
elif geometrical_figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    
elif geometrical_figure == "circle":
    r = float(input())
    area = pi * r ** 2
    
elif geometrical_figure == "triangle":
    b = float(input())
    h = float(input())
    area = b * h / 2

print(f"{area:.3f}")
