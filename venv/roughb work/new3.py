valuee = True
while valuee:
    weight = int(input('enter your weight-'))
    value = input(''''enter the value:
    'k'for kg or'l'for lb''')
    value = value.upper()
    if value == 'K':
        weight_value= weight *2.205
        break
    elif value == 'L':
        weight_value = weight / 2.205
        break
    else:
        print('please enter again')
print(f'the weight converted is {weight_value}')
