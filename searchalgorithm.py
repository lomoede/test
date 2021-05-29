#search_algorithm

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    i = 0
    a = copy.deepcopy(seq)
    a.append(key)
    while True:
        if a[i] == key: break
        i += 1
    return -1 if i == len(seq) else i

def bin_search(seq: Sequence, key: Any) -> int:
    pl = 0
    pr = len(seq)
    while True:
        pc = (pl + pr)//2

        if seq[pc] == key: return pc
        elif seq[pc] > key: pr = pc - 1
        else: pl = pc + 1

        if pl > pr: break

    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 >>>'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요 >>>'))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')


