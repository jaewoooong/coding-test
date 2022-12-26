from itertools import combinations

def char_to_bit(char:str)->int:
    return 1 << (ord(char) - ord('a'))

def sol():
    ans = 0
    word_number, char_number = map(int, input().split())
    words = [0] * word_number
    for index in range(word_number):
        word = input()
        for char in word:
            words[index] |= char_to_bit(char)

    ans = find_ans(words, word_number, char_number)

    return ans 

def find_ans(words:list, word_number:int, char_number:int)->int:
    ans = 0
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    prefix_suffix = ['a', 'c', 't', 'i', 'n']
    candidate = list(set(alphabets) - set(prefix_suffix))

    if char_number < len(prefix_suffix):
        return 0
    if char_number == alphabets:
        return word_number
    for combination in list(combinations(candidate, char_number - len(prefix_suffix))):
        each = 0
        result = 0
        for char in prefix_suffix:
            each |= char_to_bit(char)
        for char in combination:
            each |= char_to_bit(char)
        for word in words:
            if each & word == word:
                result += 1
        if result > ans:
            ans = result

    return ans

print(sol())