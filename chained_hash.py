from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity: self) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) 
        """ key값을 str형으로 변환후 encode함수에 전달하여 바이트 문자열 생성
            생성된 바이트 문자열을 sha256함수에 전달하여 해시값을 구함
            구한 해시값을 hexdigest함수에 전달하여 16진수 문자열로 꺼낸후 int형으로 변환
            self.capacity 로 나누어 다시 해시값으로 변환 """
    
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash] # p는 포인터

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end =' ')
            while p is not None:
                print(f' -> {p.key}({p.value})', end = ' ')
                p = p.next
            print()


            



