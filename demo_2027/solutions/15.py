def f(x):
    dell = (x%a==0) or ((70 <= x <= 90) <= (not x%22==0))
    return dell
for a in range(1,10000):
    if all(f(x) == 1 for x in range(1, 100000)):
        maxx = a
print(maxx)
