#python algolithm

x = int(input("input x >>>"))
y = int(input("input y >>>"))

arr = [[0] * y for _ in range(x)]

def Set_Arr(arr, x, y, x2, y2, number):
    for i in range(y - 2 * y2):
        arr[x2][y2 + i] = number + i
        
    for i in range(x - 2 * x2 - 1):
        arr[x2 + i + 1][y - 1 - y2] = number + i + y - 2 * y2

    if (y == 2 * y2 + 1) or (x == 2 * x2 + 1): return
    
    else:
        for i in range(y - 2 * y2 - 1):
            arr[x - x2 - 1][y2 + i] = number + x - 2 * x2 + 2 * y - 4 * y2 - 3 - i

        for i in range(x - 2 * x2 - 2):
            arr[x2 + 1 + i][y2] = number + 2 * x - 4 * x2 + 2 * y - 4 * y2 - 5 - i
    
    if (x >= y and 2 * (y2 + 1) >= y) or (y > x and 2 * (x2 + 1) >= y): pass
    else: Set_Arr(arr, x, y, x2 + 1, y2 + 1, number + 2 * x - 4 * x2 + 2 * y - 4 * y2 - 4)
        
def Print_Arr(arr, x, y):
    for i in range(x):
        for j in range(y):
            print(f"{arr[i][j]:4}", end = "")
        print('\n')
        
Set_Arr(arr, x, y, 0, 0, 0)
Print_Arr(arr, x, y)
