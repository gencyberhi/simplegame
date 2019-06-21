'''\
A simple game in Python.
This program illustrates the use of several elements of Python.
'''

print('')
print('Welcome to the simple game.')

hunger = 100
inventory = {
    "apples": 3
    , "bananas": 2
    , "rope": 1
    , "maps": 0
    , "keys": 1
}
print('')


text0 = ''
while text0 != 'q' :
    text = input('command > ')
    text0 = text[0]
    if text0 == 'h':
        print('')
        print('The following commands are recognized:')
        print('    e item : Eat item')
        print('    h      : Display this help.')
        print('    s      : Show hunger & inventory.')
        print('    q      : Quit this game.')
        print('')

    elif text0 == 's':
        print('')
        print('Hunger:', hunger)
        print('INVENTORY')
        for item, qty in inventory.items():
            print('\t', item, ':', qty)
        print('')

    elif text0 == 'e':
        item = text[2:]
        if item not in inventory.keys() or inventory[item] < 1:
            print('OOPS, you do not have any', item, 'to eat!')
        else:
            inventory[item] -= 1
            if item == 'apples':
                hunger += 10
            print('You have', inventory[item], item, 'remaining and your hunger is: ', health)

    hunger -= 2


