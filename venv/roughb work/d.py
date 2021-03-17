'''x = 0
for i in range(4):
    x = x + 1
    for j in range(i+1):
        print(x,end=" ")
    print()

s = 0
for a in range(4):
    for b in range(a+1):
        s = s+1
        print(s,end=' ')
    print()

A = 65
for i in range(4):
    for j in range(i+1):
        print(chr(A),end=" ")
    A = A + 1
    print()'''


for i in range(5):
    for j in range(5-i):
        print('*', end=" ")
    print()
