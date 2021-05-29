from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print("배열 원소를 역순으로 정렬합니다.")
    nx = int(input('원소 수>>>'))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'{i+1}번째 인수 : '))

    x.reverse()

    print("배열 원소를 역순으로 정렬했습니다.")

    print(x)

        