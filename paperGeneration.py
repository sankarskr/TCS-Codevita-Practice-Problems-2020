from itertools import combinations

x = int(input())
s = int(input())
y = int(input())
m = int(input())
z = int(input())
c = int(input())
k1, k2 = input().split()
k3 = input()

P = []
Q = []
R = []
i = j = count1 = count2 = 0

while j < x:
    P.append(chr(65+i))
    i += 1
    j += 1
j = 0
while j < y:
    Q.append(chr(65+i))
    i += 1
    j += 1
j = 0
while j < z:
    R.append(chr(65+i))
    i += 1
    j += 1


A = combinations(P,s)
B = combinations(Q,m)
C = combinations(R,c)

P = []
Q = []
R = []

for i in A:
    P.append("".join(list(i)))
for i in B:
    Q.append("".join(list(i)))
for i in C:
    R.append("".join(list(i)))

for i in range(len(P)):
    for j in range(len(Q)):
        for k in range(len(R)):
            count1 += 1
            temp = P[i]+Q[j]+R[k]
            if not(k1 in temp and k2 in temp) and k3 not in temp:
                count2 += 1


print(count1)
print(count2+1,end="")
