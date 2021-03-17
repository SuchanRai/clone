a = [1, 4, 5, 8, 9, 5, 3, 7, 6]
b = [9, 8, 4, 2, 7, 1, 1, 9, 2, 1]
i = 0
j = 0
while i>9:
    while j > 9:
        if a(i) == b(j):
            print(a(i))
            j +=1
    i +=1