def sol():
    ans = None
    divisor = []
    number, index = map(int, input().split())
    for num in range(1, number + 1):
        if number % num == 0:
            divisor.append(num)
    if len(divisor) < index:
        ans = 0
    if len(divisor) >= index:
        ans = divisor[index - 1]
    return ans

print(sol())