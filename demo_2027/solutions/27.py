from math import *

def e(vx, vy, m):
    return (vx ** 2 + vy ** 2) * 0.5 * m

def cntr(cl):
    res = []
    for p1 in cl:
        res.append([sum(abs(p1[2]-p2[2]) for p2 in cl), p1])
    return min(res)[1]

a = [[float(el) if '.' in el else el for el in l.split()] for l in open('27.txt')]
na = []
for p in a:
    x, y, vx, vy, m, h = p
    na.append((x, y, e(vx, vy, m), h))
na.sort(key=lambda x:x[2])
c=[]
i = j = 0
while i < len(na):
    if abs(na[i][2] - na[j][2]) > 2:
        c.append([na[t] for t in range(i, j)])
        i = j
    j+=1
    if j == len(na):
        c.append([na[t] for t in range(i, j)])

        break
cnts = [cntr(cl) for cl in c]
d = []
for cl in c:
    for p1 in cl:
        for p2 in cl:
            if p1[-1] == p2[-1] == 'II':
                d.append(dist(p1[:2], p2[:2]))
print(int(10000*max(d)))
print(int(cnts[-1][2] * 10000))