name = input('enter your name-')
character = len(name)
if character<3:
    print('name must be at least 3 character')
elif character<50:
    print('name is perfect')
else:
    print('name has more than 50 character')