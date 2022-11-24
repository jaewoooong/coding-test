def sol():
    heights = []
    for _ in range(9):
        height = int(input())
        heights.append(height)

    heights = get_heights(heights)
    print_list(heights)
    return

def get_heights(list:list)->list:
    for index1 in range(0, len(list) - 1):
        for index2 in range(index1 + 1, len(list)):
            if list[index1] + list[index2] == sum(list) - 100:
                remove_elem1, remove_elem2 = list[index1], list[index2]
                list.remove(remove_elem1)
                list.remove(remove_elem2)
                list.sort()
                return list

def print_list(list:list):
    for elem in list:
        print(elem)

sol()
