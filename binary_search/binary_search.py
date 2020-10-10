def binary_search(entry, sorted_list,true_index = 0):
    mid_index = (len(sorted_list)-1)//2
    if sorted_list[mid_index] == entry:
        return mid_index + true_index
    elif sorted_list[mid_index]>entry:
        return binary_search(entry,[sorted_list[i] for i in range(len(sorted_list)) if i < mid_index], true_index)
    elif sorted_list[mid_index] < entry:
        return binary_search(entry,[sorted_list[i] for i in range(len(sorted_list)) if i > mid_index], true_index+mid_index+1)

        
for x in [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]:
    print(binary_search(x, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]))