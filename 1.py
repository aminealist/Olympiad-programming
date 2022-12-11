import re
n, k = map(int, re.findall(r"\d+", input()))
a = list(map(int, re.findall(r"\d+", input())))
s = [a[0]]
for i in range(1, len(a)):
    s.append(s[i-1]+a[i])

for i in range()