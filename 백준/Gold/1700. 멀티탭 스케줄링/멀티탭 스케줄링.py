import sys

def sol():
    ans = 0
    multitab = []
    tab_number, use_number = map(int, input().split())
    electrics = list(map(int, input().split()))
    
    for index, electric in enumerate(electrics):
        
        if electric in multitab:
            continue
        if len(multitab) == tab_number:
            multitab.remove(get_elem_to_pop(multitab, electrics, index))
            ans += 1
        if len(multitab) < use_number:
            multitab.append(electric)

    return ans 

def get_elem_to_pop(stack:list, electrics:list, index:int):
    dists = []
    for elem in stack:
        dists.append(get_dist(elem, index, electrics))
    return stack[dists.index(max(dists))]

def get_dist(elem_to_find:int, index:int, electrics:list)->int:
    dist = 0
    electrics = electrics[index + 1:]
    for electric in electrics:
        dist += 1
        if electric == elem_to_find:
            return dist
    return sys.maxsize

print(sol())