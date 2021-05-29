#Spiral Array

class Cursor:
    D = {'right': (0, 1), 'left': (0, -1), 'up': (-1, 0), 'down': (1, 0)}

    def __init__(self, row, col, direction):
        self.col = col
        self.row = row
        self.direction = direction

    def move(self):
        adder = self.D[self.direction]
        next_row = self.row + adder[0]
        next_col = self.col + adder[1]
        return Cursor(next_row, next_col, self.direction)

    def lotate(self):
        l = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}
        self.direction = l[self.direction]
        self.row += self.D[self.direction][0]
        self.col += self.D[self.direction][1]

class Spiral:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.arr = [[-1 for c in range(col)] for r in range(row)]
        self.cursor = Cursor(0, 0, 'right')

    def isEdge(self, cursor):
        if cursor.col >= self.col: return True
        if cursor.row >= self.row: return True
        if cursor.row < 0: return True
        if cursor.col < 0: return True
        if self.arr[cursor.row][cursor.col] != -1: return True
        return False

    def print_Arr(self):
        for i in range(row):
            for j in range(col):
                print(f"{self.arr[i][j]:4}", end = " ")
            print('\n')

    def mark(self, value):
        self.arr[self.cursor.row][self.cursor.col] = value


col = int(input("input column >>>"))
row = int(input("input row >>>"))

spiral = Spiral(col, row)
spiral.arr[0][0] = 0
for value in range(1, col * row):
    next_cursor = spiral.cursor.move()

    if spiral.isEdge(next_cursor):
        spiral.cursor.lotate()
    else:
        spiral.cursor = next_cursor
        
    spiral.mark(value)

spiral.print_Arr()