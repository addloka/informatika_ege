f = open('1_24.txt').readline()
maxl = 0
k = 0
l = 0
for i in range(1, len(f)):
    if f[i-1:i+1] == 'BC':
        k+=1
    while k>190:
        if f[l] == 'B' and f[l+1] == 'C':
            k-=1
        l+=1
    if k == 190:
        cur = i - l 
        if cur > maxl: maxl = cur
print(maxl)