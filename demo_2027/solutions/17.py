a = [int(x) for x in open('17.txt')]
minn = min(a)
colvo = 0
p=[]
for i in range(len(a)-1):
    p1, p2 = a[i:i+2]
    if p1%33==minn or p2%33==minn:
        colvo+=1
        p.append(p1+p2)
print(colvo, max(p))