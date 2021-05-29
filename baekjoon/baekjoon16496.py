import sys
n = sys.stdin.readline()
lst = sys.stdin.readline().split()
newlist = list((int(number + number[0] * (11 - len(number))), int(number + '9' * (11 - len(number))), number) for number in lst)
newlist.sort(reverse=True)
ans = ''
for tup in newlist: ans += tup[2]
if len(ans) == ans.count('0'): ans = 0
print(ans)