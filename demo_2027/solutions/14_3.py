nyzn = 0
for x in range(0, 2030):
    a = 7**170 + 7**100 - x
    cnt = 0
    while a > 0:
        if a%7==0:
            cnt+=1
        a//=7
    if cnt == 71:
        nyzn = x
print(x)