from string import *
for x in (digits + ascii_uppercase)[:22]:
    n = int(f'27{x}98876', 22) + int(f'26{x}51', 22) + int(f'711{x}5', 22)
    if n % 21 == 0:
        print(n // 21)
        exit(0)