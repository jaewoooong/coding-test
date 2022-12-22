def sol():
    string = ''
    string = input()
    stack = []
    ans = 0
    tmp = 1

    for index in range(len(string)):
        if string[index] == '(':
            stack.append('(')
            tmp *= 2
        if string[index] == '[':
            stack.append('[')
            tmp *= 3
        if string[index] == ')':
            if not len(stack):
                return 0
            if string[index - 1] == '(':
                ans += tmp
            if stack[-1] == '(':
                stack.pop()
            tmp //= 2
        if string[index] == ']':
            if not len(stack):
                return 0
            if string[index - 1] == '[':
                ans += tmp
            if stack[-1] == '[':
                stack.pop()
            tmp //= 3
            
    if len(stack):
        return 0

    return ans

print(sol())