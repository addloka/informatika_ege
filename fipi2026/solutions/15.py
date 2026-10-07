def f(x):
    if ( (not a1 <= x <= a2) <= ((22 <= x <= 40) == (32 <= x <= 50)) ) == True:
        return 1
    else:
        return 0
minn =[]
for a1 in range(1, 100):
    for a2 in range(1, 100): 
        if all(f(x) == 1 for x in range(1, 10000)):
            minn.append(abs(a2-a1))
print(min(minn))


    