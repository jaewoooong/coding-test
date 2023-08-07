def snail_list(n: int, target: int):
    # d, r, u, l
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    cnt = n * n
    vector = 0
    x, y = 0, -1
    target_index = ()
    for _ in range((n + 1) * (n + 1)):
        nx, ny = x + dx[vector % 4], y + dy[vector % 4]
        can_move = nx < n and ny < n and nx >= 0 and ny >= 0 and matrix[ny][nx] == 0
        if can_move:
            matrix[ny][nx] = cnt
            if cnt == target:
                target_index = (ny + 1, nx + 1)
            cnt -= 1
            x, y = nx, ny
        if not can_move:
            vector += 1

    return matrix, target_index


def print_2d_list(matrix: list):
    for matrix_ in matrix:
        print(*matrix_)


def sol():
    n = int(input())
    target = int(input())
    snail, target_index = snail_list(n, target)
    print_2d_list(snail)
    print(*target_index)


sol()