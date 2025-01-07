while True:
    number = float(input())
    if number < 0:
        print("Negative number!")
        break
    number_multiplied = number * 2
    print(f'Result: {number_multiplied:.2f}')
