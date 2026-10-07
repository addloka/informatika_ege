f = open('1_26.txt')
n = int(f.readline())
maxx = 0
items = [
    
]

for i in range(n):
    a, p, s = map(int, f.readline().split())
    items.append((a,p,s))
avg = 0
for i in range(len(items)):
    avg += items[i][1]
avg /= len(items)
count = {}
uncount = {}
price = {}

items = [item for item in items if item[1] > avg]

for a, p, s in items:
    price[a] = p
    if a not in count:
        count[a] = 0
        uncount[a] = 0
    if s == 0:
        count[a] +=1
    else: 
        uncount[a] +=1
maxa = 0
for a in count:
    if maxa == 0: maxa = a
    if count[maxa] < count[a] :
        maxa = a
    elif count[maxa] == count[a]: 
        if price[a] > price[maxa]:
            maxa = a
        elif price[a] == price[maxa]:
            if uncount[a] < uncount[maxa]: maxa = a
print(price[maxa] * count[maxa], uncount[maxa])