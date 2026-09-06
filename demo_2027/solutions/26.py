f = open('26.txt')
n, k = map(int, f.readline().split())
a = sorted(l.split() for l in f)
data = []
res = []
users = {}
for t, idn, s in a:
    idn, s = int(idn), int(s)
    if sum(data) + s <= k:
        data += [s]
    else:
        if t <= "11:59:59":
            res.append(sum(data))
        data = [s]
    if idn not in users: users[idn] = s
    else: users[idn] += s
max_data = max(users.values())
res.sort()
print([idn for idn in users if users[idn] == max_data], res[-1] + res[-2])

#[7040] 52204