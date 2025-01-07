item = input()

item_type = ''

if (item == 'banana'
        or item == 'apple'
        or item == 'kiwi'
        or item == 'cherry'
        or item == 'lemon'
        or item == 'grapes'):
    item_type = 'fruit'

elif (item == 'tomato'
      or item == 'cucumber'
      or item == 'pepper'
      or item == 'carrot'):
    item_type = 'vegetable'

else:
    item_type = 'unknown'

print(item_type)