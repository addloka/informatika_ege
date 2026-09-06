from re import *
s = open('24.txt').readline()
num = r'([1-9][0-9]*|0)'
reg = rf'(?=({num}([-*]{num})*))'
res = []
for x in finditer(reg, s):
    res.append(len(x[1]))
print(max(res))