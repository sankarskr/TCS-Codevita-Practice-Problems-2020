import math
def calculate(den,cnt,i,amt,n,sel):
    global d

    if sel > n:
        return -math.inf
    if amt == 0:
        return 0
    if amt < 0:
        return -math.inf
    if amt > 0 and i == len(den):
        return -math.inf

    if (i,amt,sel) in d.keys():
        return d[(i,amt,sel)]
    
    if amt > 0 and cnt[i] == 0:
        d[(i,amt,sel)] = calculate(den,cnt,i+1,amt,n,sel)
        return d[(i,amt,sel)]

    tmp = cnt[:]
    cnt[i] -= 1
    p = 1 + calculate(den,cnt,i,amt-den[i],n,sel+1)
    q = calculate(den,tmp,i+1,amt,n,sel)
    d[(i,amt,sel)] = max(p,q)
    return d[(i,amt,sel)]


n = int(input())
amt = int(input())
den = [100,200,500,1000]
cnt = []
d = {}
for _ in range(4):
    cnt.append(int(input()))
res = calculate(den,cnt,0,amt,n,0)
if res == -math.inf:
  print(0,end="")
else:
  print(res,end="")