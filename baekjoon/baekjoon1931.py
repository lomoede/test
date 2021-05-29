import sys
a = []
b = []
n = int(sys.stdin.readline())
for i in range(n): b.append(tuple(map(int, sys.stdin.readline().split())))
b.sort(key = lambda x:x[0])
b.sort(key = lambda x:x[1])
a.append(b.pop(0))
for i in b:
    if a[-1][1] <= i[0]: a.append(i)
print(len(a))