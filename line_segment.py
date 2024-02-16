def is_degenerated(x_1, y_1, x_2, y_2):
    if (x_1 == x_2):
        if (y_1 == y_2):
            return('true')
        else:
            return('false')
    else:
        return('false')

def is_vertical(x_1, y_1, x_2, y_2):
    if (y_1 != y_2):
        if (x_1 == x_2):
            return('true')
        else:
            return('false')
    else:
        return('false')

def is_horizontal(x_1, y_1, x_2, y_2):
    if (x_1 != x_2):
        if (y_1 == y_2):
            return('true')
        else:
            return('false')
    else:
        return('false')

def is_inclined(x_1, y_1, x_2, y_2):
    if (x_1 != x_2):
        if (y_1 != y_2):
            return('true')
        else:
            return('false')
    else:
        return('false')

x_1 = input("Введите x_1: ")
y_1 = input("Введите y_1: ")
x_2 = input("Введите x_2: ")
y_2 = input("Введите y_2: ")

degenerated = is_degenerated(x_1, y_1, x_2, y_2)
vertical = is_vertical(x_1, y_1, x_2, y_2)
horizontal = is_horizontal(x_1, y_1, x_2, y_2)
inclined = is_inclined(x_1, y_1, x_2, y_2)
if degenerated == 'true':
    print('is_degenerated = true')
else:
    print('is_degenerated = false')
if vertical == 'true':
    print('is_vertical = true')
else:
    print('is_vertical = false')
if horizontal == 'true':
    print('is_horizontal = true')
else:
    print('is_horizontal = false')
if inclined == 'true':
    print('is_inclined = true')
else:
    print('is_inclined = false')