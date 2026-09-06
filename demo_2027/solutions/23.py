a = []
for l in open('23.txt'):
    u, v, w = l.split()
    a.append((int(u), int(v), float(w)))

d = [0, 0] + [float("inf")]*1000
for _ in range(200):
    for u, v, w in a:
        d[v] = min(d[v], d[u] + w)
print(d[100])