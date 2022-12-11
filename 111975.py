from re import findall


a = list(map(int, findall(r"\d+", input())))
ch = list(map(int, findall((r"\d+"), input())))
n, rule = a[0], a[1]

r = 1
l = 0
k = 0


while 1:
    try:
        if ch[r]-ch[l]<=rule:
            r+=1
        else:
            l+=1
            k+=n-r
    except:
        break

print(k)
