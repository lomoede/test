import sys
n = int(sys.stdin.readline())
a = []
for i in range(n): 
    x, y = map(int, sys.stdin.readline().split())
    a.append((y, x))
print('정렬 전 a')
print(a)
a.sort()
print('정렬 후 a')
print(a)
lst = [[a.pop(0)], []]
for i in a:
    ptr = 0
    while True:
        if len(lst[ptr]) != 0:
            if lst[ptr][-1][0] <= i[1]: 
                lst[ptr].append(i)
                print(lst)
                break
            ptr += 1
        else: 
            lst[ptr].append(i)
            lst.append([])
            print(lst)
            break
print(len(lst) - 1)
# a = [[]]
# b = [1, 2]
# c = [3, 4]
# d = [5, 6]
# a[0].append(b)
# a[0].append(c)
# a.append([])
# a[1].append(d)
# print(a)

# a =[]
# len(a)