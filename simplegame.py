'''\
A simple game in Python.
This program illustrates the use of several elements of Python.
'''

def init():
    '''Initialize'''
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
    return hunger, inventory

def show(hunger, inventory):
    print('')
    print('Hunger:', hunger)
    print('INVENTORY')
    for item, qty in inventory.items():
        print('\t', item, ':', qty)
    print('')

def showhelp():
    print('')
    print('The following commands are recognized:')
    print('    e item : Eat item')
    print('    h      : Display this help.')
    print('    s      : Show hunger & inventory.')
    print('    q      : Quit this game.')
    print('')


def eat(item, inventory, hunger):
    if item not in inventory.keys() or inventory[item] < 1:
        print('OOPS, you do not have any', item, 'to eat!')
        return
    
    inventory[item] -= 1
    if item == 'apples':
        hunger += 10
    
    print('You have', inventory[item], item, 'remaining and your hunger is: ', health)


if __name__ == '__main__':
    hunger, inventory = init()
    show(hunger, inventory)

    text0 = ''
    while text0 != 'q' :
        text = input('command > ')
        text0 = text[0]
        if text0 == 'h':
            showhelp()
        elif text0 == 's':
            show(hunger, inventory)
        elif text0 == 'e':
            eat(text[2:], inventory, hunger)
        hunger -= 2

