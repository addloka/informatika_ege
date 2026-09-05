res = []
for n in range(1,100):
    r = f'{n:b}'
    if n % 2 == 0:
        r = '11' + r + '11'
    else:
        r = '1' + r + '00'
    a = int(r, 2)
    if a > 95:
        res.append(a)
print(min(res))