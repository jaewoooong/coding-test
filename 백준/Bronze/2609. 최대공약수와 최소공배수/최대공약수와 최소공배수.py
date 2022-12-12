def sol():
    num1, num2 = map(int, input().split())
    print(getGCD(num1, num2))
    print(getLCM(num1, num2))
    return

def getGCD(num1:int, num2:int)->int:
    num1_divisors, num2_divisors = getDivisors(num1), getDivisors(num2)
    common_divisors = []
    for num1_divisor in num1_divisors:
        if num1_divisor in num2_divisors:
            common_divisors.append(num1_divisor)
            num2_divisors.remove(num1_divisor)
    return getMulti(common_divisors)

def getMulti(list:list)->int:
    multi = 1
    for elem in list:
        multi *= elem
    return multi

def getDivisors(num:int)->list:
    divisors = []
    i = 2
    while (num != 1):
        if isPrime(i) and num % i == 0:
            divisors.append(i)
            num /= i
            continue
        i += 1
    return divisors

def isPrime(num:int)->bool:
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def getLCM(num1:int, num2:int)->int:
    num1_multi, num2_multi = getMulti(getDivisors(num1)), getMulti(getDivisors(num2))
    GCD = getGCD(num1, num2)
    return int(GCD * (num1_multi / GCD) * (num2_multi / GCD))

sol()