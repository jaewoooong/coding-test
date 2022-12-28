import sys

def sol():
    ans = 0
    length, summation = map(int, input().split())
    numbers = list(map(int, input().split()))
    ans = get_ans(length, numbers, summation)

    return ans 

def get_ans(length:int, numbers:list, summation:int)->int:
    start, end = 0, 0
    temp_sum = numbers[0]
    ans = sys.maxsize

    while start < length:
        if temp_sum >= summation:
            ans = min(ans, end - start + 1)
            temp_sum -= numbers[start]
            start += 1
        if temp_sum < summation:
            end += 1
            if end == length:
                break
            temp_sum += numbers[end]
            
    if ans == sys.maxsize:
        ans = 0

    return ans

print(sol())