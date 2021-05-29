#python_algorithm
def printstar(n, w):
    for _ in range(n//w):
        print('*' * w, end = "")
        print('\n')

    if n % w:
        print('*' * (n % w))

n = int(input("input n : "))
w = int(input("input w : "))
printstar(n, w)
