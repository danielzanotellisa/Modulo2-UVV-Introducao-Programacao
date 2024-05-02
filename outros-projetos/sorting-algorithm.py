list = [23, 10, 2, 6, 8, 5, 1]

def lowest(list):

    lowest = list[0]
    lowest_index = 0

    for i in range(1,len(list)):

        if list[i] < lowest:

            lowest = list[i]
            lowest_index = i
    return lowest_index

print(lowest(list))

def sorting(arr):

    new_list = []

    for i in range(len(arr)):

        menor = lowest(arr)
        new_list.append(arr.pop(menor))
    return new_list

print(sorting(list))