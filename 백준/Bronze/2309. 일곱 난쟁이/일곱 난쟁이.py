def sol():
    heights = []
    for _ in range(9):
        height = int(input())
        heights.append(height)
    
    sum_heights = sum(heights)

    for index1 in range(0, len(heights) - 1):
        for index2 in range(index1 + 1, len(heights)):
            if heights[index1] + heights[index2] == sum_heights - 100:
                remove_elem1, remove_elem2 = heights[index1], heights[index2]
                heights.remove(remove_elem1)
                heights.remove(remove_elem2)
                heights.sort()
                print_list(heights)
                return

def print_list(list:list):
    for elem in list:
        print(elem)

sol()