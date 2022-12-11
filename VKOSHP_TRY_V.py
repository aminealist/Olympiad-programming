n=int(input())
x1 = 0
x2 = n
y1 = 0
y2 = n
for h in range(2):
    while 1:
        print(0, 1, "L")
        otv=int(input())
        if otv == 0:
            break
        else:
            x1 += 1
    while 1:
        print(0, 2, "R")
        otv=int(input())
        if otv == 0:
            break
        else:
            x2 -= 1
    while 1:
        print(0, 2, "U")
        otv=int(input())
        if otv == 0:
            break
        else:
            y2 -= 1
    while 1:
        print(0, 1, "D")
        otv=int(input())
        if otv == 0:
            break
        else:
            y1 += 1
print(1, x1+1, y1+1, x2, y2)