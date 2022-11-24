def fibo(number:int)->int:
    if number == 0:
        return 0
    if number == 1:
        return 1
        
    return fibo(number - 1) + fibo(number - 2)

def sol():
    ans = None
    number = int(input())
    ans = fibo(number)

    return ans

print(sol())