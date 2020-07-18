n = int(input())
t = int(input())
l = []

for i in range(n):
    x = list(map(int, input().split()))
    v = x.pop()
    for j in range(1,len(x)):
        x[j] += x[j-1]
    x.insert(0,v)
    l.append(x)

d = [0]*(n+1)

for i in range(2,t,2):
    m = 0
    r = [-1]
    for j in range(n):
        f = l[j][i]*l[j][0]
        if f > m:
            m = f
        r.append(f)
        
    for j in range(len(r)):
        if r[j] == m:
            d[j] += 1

res = d.index(max(d))
print(res,end="")
