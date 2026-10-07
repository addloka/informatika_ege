a = [int(x) for x in open('17.txt')]
kolvo = 0
maxx = 0
usl1 = 100001
ans = []
for i in range(len(a)):
    if a[i] % 123 == 0 and a[i] > 0 and a[i] < usl1:
        usl1 = a[i]
for i in range(len(a)-1):
    if (a[i]+a[i+1]) < usl1:
        kolvo +=1
        b = (a[i]+a[i+1])
        ans.append(b)
maxx = max(ans)
print(kolvo, abs(maxx))