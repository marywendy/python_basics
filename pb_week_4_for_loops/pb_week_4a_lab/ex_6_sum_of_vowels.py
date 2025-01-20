text = input().lower()

addition = 0
for i in range(len(text)):
    if text[i] == "a":
        addition += 1
    if text[i] == "e":
        addition += 2
    if text [i] == "i":
        addition += 3
    if text[i] == "o":
        addition += 4
    if text [i] == "u":
        addition += 5

print(addition)
