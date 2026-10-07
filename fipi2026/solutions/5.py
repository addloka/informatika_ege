res = []
for n in range(0, 100):
    d = f'{n:b}'
    if d.count('1') % 2 == 0:
        d = '10' + d[2:] + '0'
    else:
        d = '11' + d[2:] + '1'
    r = int(d, 2)
    if r <= 19:
        res.append(n)
print(max(res))