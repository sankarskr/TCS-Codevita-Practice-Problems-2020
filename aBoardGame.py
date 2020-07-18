import math

def fun(l, n, i, j):
    global d
    if i == 0 and j == 0:
        return l[i][j]
    elif i < 0 or j < 0:
        return math.inf
    if (i,j) in d.keys():
        return d[(i,j)]
    a = fun(l, n, i-1, j)
    b = fun(l, n, i, j-1)
    d[(i,j)] = l[i][j] + min(a, b)//2
    return d[(i,j)]



n = int(input())
l = []
d = {}
for _ in range(n):
    l.append(list(map(int, input().split())))

s = fun(l, n, n-1, n-1)
print(s,end="")
