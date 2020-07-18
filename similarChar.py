N = int(input())
S = input()

d = {}
for i in range(26):
    d[chr(97+i)] = 0
L = []
for i in range(N):
    L.append(d[S[i]])
    d[S[i]] += 1

Q = int(input())
R = []
for _ in range(Q):
    x = int(input())
    R.append(L[x-1])
for i in range(len(R)):
    if i == len(R)-1:
        print(R[i],end="")
    else:
        print(R[i])