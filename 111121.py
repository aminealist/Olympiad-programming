import re
a = list(map(int, re.findall(r"\d+", input())))
b = list(map(int, re.findall(r"\d+", input())))
g = list(map(int, re.findall(r"\d+", input())))
bb=0
cb=1
im=0
if a[0]==1 or a[1]==0:
    print(a[1])
    print(-1, -1)
else:
    for i in range(1, len(g)):
        if b[im]>b[i-1]:
            im=i-1
        if b[im]*g[cb]<b[bb]*g[i]:
            bb=im
            cb=i
    if b[bb]-g[cb]<0:
        print((a[1]//b[bb])*(g[cb])+a[1]%b[bb])
        print(bb+1,cb+1)
    else:
        print(a[1])
        print(-1, -1)

