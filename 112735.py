a = list(map(int, input().replace("\n", "").split(" ")))
b = list(map(int, input().replace("\n", "").split(" ")))
ib=0
k=a[1]+1
kb=a[1]+1
im=0
for i in range(a[1]+1, a[0]):
    if b[i-k]>b[im]:
        im=i-k
    if b[ib]+b[kb]<b[im]+b[i]:
        ib=im
        kb=i
print(ib+1, kb+1)