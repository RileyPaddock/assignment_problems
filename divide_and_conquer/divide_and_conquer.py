
def divide_and_conquer_sort(x):
    if len(x) == 2:
        if x[0] < x[1]:
            return x
        else:
            return [x[1],x[0]]
    elif len(x) == 1:
        return x
    arr1 = [x[i] for i in range(len(x)) if i >= len(x)//2]
    arr2 = [x[i] for i in range(len(x)) if i < len(x)//2]
    x1 = divide_and_conquer_sort(arr1)
    x2 = divide_and_conquer_sort(arr2)
    return compute_sorted_lists(x1, x2)

#divide_and_conquer_sort(input list):
    # if the input list consists of more than one element:
    #     break up the input list into its left and right halves
    #     sort the left and right halves by recursively calling divide_and_conquer_sort
    #     combine the two sorted halves
    #     return the result
    # otherwise, if the input list consists of only one element, then it is already sorted,
    #     and you can just return it.

def compute_sorted_lists(x,y):
    combined_list = []
    index_x = 0
    index_y = 0
    while True:
        if x[index_x] < y[index_y]:
            combined_list.append(x[index_x])
            if index_x + 1<len(x):
                index_x+=1
            else:
                for i in range(len(y)):
                    if i >= index_y:
                        combined_list.append(y[i])
                break
        else:
            combined_list.append(y[index_y])
            if index_y + 1<len(y):
                index_y+=1
            else:
                for i in range(len(x)):
                    if i >= index_x:
                        combined_list.append(x[i])
                break
    return combined_list