n = [0] * 26
st = input()
st = st.lower()
for i in st:
    n[ord(i)-97] += 1
max = ord(st[0])-97
for i in range(len(n)):
    if n[i] > n[max]:
        max = i
for i in range(len(n)):
    if i == max: continue
    if n[i] == n[max]:
        print('?')
        exit()
print(str(chr(max+97)).upper())

