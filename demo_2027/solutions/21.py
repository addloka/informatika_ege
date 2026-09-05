def f(s1, s2, m):
    if s1+s2 >= 133: return m % 2 == 0 # условие победы
    if m == 0: return 0
    h = [f(s1 + 4,s2 , m - 1), f(s1,s2 + 4, m - 1), f(s1 * 2,s2, m - 1), f(s1,s2*2, m - 1)] # ходы
    return any(h) if (m - 1)% 2 == 0 else all(h)
print('20)', [s for s in range(1, 116) if (not f(17, s, 2)) and f(17, s, 4)])