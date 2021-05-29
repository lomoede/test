def card_conv(n: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while n > 0:
        d += dchar[n%r]
        n //= r

    return d[::-1]

if __name__ == '__main__':
    print("진수변환합니다.")
    number = int(input('변환할 숫자 입력>>>'))
    division = int(input('몇진수로 변환합니까>>>'))

    print(card_conv(number, division))