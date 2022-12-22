def sol():
    ans = 0
    height, weight = map(int, input().split())
    matrix = [[0 for _ in range(weight)] for _ in range(height)]
    blocks = list(map(int, input().split()))
    matrix = fillBlocks(blocks, matrix)
    ans = findPoolSize(matrix)

    return ans 

def fillBlocks(blocks:list, matrix:list)->list:
    row, col = len(matrix[0]), len(matrix)
    for x in range(row):
        for y in range(col-1, -1, -1):
            if blocks[x]:
                matrix[y][x] = 1
                blocks[x] -= 1
    return matrix

def findPoolSize(matrix:list)->int:
    size = 0
    row, col = len(matrix[0]), len(matrix)
    for y in range(col-1, -1, -1):
        for x in range(row):
            if matrix[y][x] == 0 and isPool(matrix[y], x):
                size += 1    
    return size

def isPool(row:list, start:int)->bool:
    if 1 in row[:start] and 1 in row[start + 1:]:
        return True
    return False

print(sol())