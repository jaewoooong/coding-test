import sys
maximum = -sys.maxsize
minimum = sys.maxsize

def sol():
    n = int(input())
    numbers = list(map(int, input().split()))
    add, sub, multi, div = map(int, input().split())
    dfs(1, numbers[0], add, sub, multi, div, numbers, n)
    print(maximum)
    print(minimum)
    return

def dfs(depth, result, add, sub, multi, div, numbers, n):
    global maximum, minimum
    if depth == n:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return

    if add:
        dfs(depth + 1, result + numbers[depth], add - 1, sub, multi, div, numbers, n)
    if sub:
        dfs(depth + 1, result - numbers[depth], add, sub - 1, multi, div, numbers, n)
    if multi:
        dfs(depth + 1, result * numbers[depth], add, sub, multi - 1, div, numbers, n)
    if div:
        dfs(depth + 1, int(result / numbers[depth]), add, sub, multi, div - 1, numbers, n)
    
sol()