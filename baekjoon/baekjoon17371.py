import sys
def distance(a, b): return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) 
n = int(sys.stdin.readline())
a = []
for i in range(n): a.append(list(map(int, sys.stdin.readline().split())))
dis2 = 800000000
ans = 0
for i in a:
    dis1 = -1
    for j in a:
        if a == j: continue
        if distance(i, j) > dis1:
            dis1 = distance(i, j)
            temp = i
    if dis1 < dis2: 
        ans = i
        dis2 = dis1
print(ans[0],ans[1])