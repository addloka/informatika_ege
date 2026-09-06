def f(n):
    mn = []
    d = 2
    while d ** 2 <= n:
        while n% d == 0:
            mn.append(d)
            n //=d
        d+=1
    if n > 1:
        mn.append(n)
    return mn


for n in range(1103285717, 1103400000):
    mn = f(n)
    if len(mn) == 2 and str(mn[0]).count('16') == 1 and str(mn[1]).count('16') == 1: 
        print(n, min(mn))
#1103299319 1693
#1103309477 1693
#1103322107 16187
#1103323021 1693
#1103328547 3169
