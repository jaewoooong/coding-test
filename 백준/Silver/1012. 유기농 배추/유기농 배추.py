import sys

sys.setrecursionlimit(10**6)
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def sol():
    test_case = int(input())
    for _ in range(test_case):
        row, col, cabbages = map(int, input().split())
        matrix = [[0 for _ in range(row)] for _ in range(col)]
        for _ in range(cabbages):
            x, y = map(int, input().split())
            matrix[y][x] = 1
        print(getWorms(row, col, matrix))
    return

def getWorms(row:int, col:int, matrix:list)->int:
    worms = 0
    for y in range(col):
        for x in range(row):
            if matrix[y][x] == 1:
                removeRegion(matrix, x, y, row, col)
                worms += 1
    return worms
    
def removeRegion(matrix:list, x:int, y:int, row:int, col:int):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if inRange(nx, ny, row, col) and matrix[ny][nx] == 1:
            matrix[ny][nx] = 0
            removeRegion(matrix, nx, ny, row, col)

def inRange(x, y, row, col):
    return 0 <= x and x < row and 0 <= y and y < col

sol()