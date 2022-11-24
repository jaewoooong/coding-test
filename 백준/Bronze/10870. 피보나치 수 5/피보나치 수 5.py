MAX_NUM = 20
fibo_number = [0] * (MAX_NUM + 1)

def is_calculated(number:int)->bool:
    return number != 0

def fibo(index:int)->int:
    if index == 0:
        return 0
    if index == 1:
        return 1
    if is_calculated(fibo_number[index]):
        return fibo_number[index]
    
    fibo_number[index] = fibo(index - 1) + fibo(index - 2)
    return fibo_number[index]

def sol():
    ans = None
    number = int(input())
    ans = fibo(number)

    return ans

print(sol())
