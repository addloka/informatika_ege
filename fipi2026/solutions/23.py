def f(x):
    if x == 14:
        return 0
    if x == 39:
        return 1
    if x > 39:
        return 0
    return f(x+1) + f(x*2) + f(x*3)
print(f(2))