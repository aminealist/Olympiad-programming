n =int(input())
a = []
for i in list(map(int, input().split(" "))):
    a.append(i)
p = [a[n-1]]
sc = n-1
for i in range(n-1, 0, -1):
    if a[sc]