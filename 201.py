n = int(input())
k = 0
s = 1
for i in range(1, n):
    l = s
    s = s + k
    k = l
print(s)