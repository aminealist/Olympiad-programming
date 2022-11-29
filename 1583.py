import re
a = list(map(int, re.findall(r"\S+", input())))
b = list(map(int, re.findall(r"\S+", input())))
summ=[0]*1
summ[0]=b[0]
for i in range(len(b)-1):
    summ.append(summ[i]+b[i+1])
bruh=0
a0=0
a1=a[1]
bz=summ[a[1]]
if bz==a[2]:
    print(1)
else:
    for i in range(a[1]+1, len(summ)):
        if summ[i]- summ[i-a[1]-1]==a[2]:
            bz=i
            bruh=1
            break
    if bruh == 0:
        print(0)
    else:
        print(i-a[1]+1)

