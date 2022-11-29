k = int(input())
if k==1:
    a = input()
    print(1,1)
else:
    if k != 0:
        s=[0]*k
        a=[0]*k
        a[0] = int(input())
        s[0] = a[0]
        for i in range(1, k):
            a[i] = int(input())
            s[i] = s[i-1]+a[i]
        im=0
        ib=0
        jb=1
        for i in range(1, len(s)):
            if s[i-1]<s[im]:
                im=i-1
            if s[jb]-s[ib]<s[i]-s[im]:
                ib=im
                jb=i
        print(ib+2)
        print(jb+1)