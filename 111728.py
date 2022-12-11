import re
n, m = map(int, re.findall(r"\d+", input()))
a = list(map(int, re.findall(r"\d+", input())))
b = list(map(int, re.findall(r"\d+", input())))

for zn in b:
    l = -1
    r = len(a)
    bruuuh=0
    while abs(r-l)>2:
        m = (r-l)//2
        if a[m] == zn:
            osh1=0
            osh2=0
            l=m
            r=m
            while osh1!=1 and osh2!=1:

                l-=1
                r+=1
                if r<len(a) and l>-1:
                    if a[r]!=zn and osh1!=1:
                        r+=1
                    else:
                        osh1=1
                    if a[l]!=zn and osh2!=1:
                        l-=1
                    else:
                        osh2=1
                break
        else:
            print(a[m], zn)
            if a[m]<zn:
                l=m
            else:
                r=m
        print(l,r)