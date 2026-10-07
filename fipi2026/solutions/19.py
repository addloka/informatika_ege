def f(s1, s2, m):
    if s1+s2 >= 154: return m % 2 == 0
    if m == 0: return 0
    h = [ f(s1+4, s2, m-1), f(s1, s2+4, m-1), f(s1*3, s2, m-1), f(s1, s2*3, m-1) ]
    # for 19: return any(h)
    # for 20 n 21:
    return any(h) if (m - 1)% 2 == 0 else all(h)
#19 print([i for i in range(1, 142) if f(11, i, 2)])
#19 - ans 16
#20 print([i for i in range(1, 142) if (not f(11, i, 1) and f(11, i, 3))])
#20 - ans 39,40
#21 - ans 41
print([i for i in range(1, 142) if (not f(11, i, 2) and f(11, i, 4))])
