a = [192, 168, 159, 86, 255, 255, 252, 0]
for i in range(8):
    print(bin(a[i])[2:])
b = ['11000000', '10101000', '10011100', '00000000']
sum = 0
for i in range(4):
    sum += int(b[i], 2)
print(sum)