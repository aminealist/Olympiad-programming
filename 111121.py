a = list(map(int, input().replace("\n", "").split(" ")))
b = list(map(int, input().replace("\n", "").split(" ")))
g = list(map(int, input().replace("\n", "").split(" ")))
bb=0
cb=1
im=0
if a[0]==1:
    print(a[1])
    print(-1, -1)
else:
    for i in range(1, len(g)):
            if b[i-1]<b[im]:
                im=i-1
            if g[cb]*b[im]<g[i]*b[bb]:
                cb=i
                bb=im
    if g[cb]-b[bb]<=0:
        print(a[1])
        print(-1, -1)
    else:
        print((g[cb])*a[1])
        print(bb+1, cb+1)
