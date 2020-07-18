t = int(input())
for z in range(t):
    s = list(input())
    p = input()
    d = {}
    for i in range(26):
        d[chr(i+97)] = 0
    for i in p:
        d[i] += 1
    r = ""
    for i in s:
        r += i*d[i]
    if z == t-1:
        print(r,end="")
    else:
        print(r)