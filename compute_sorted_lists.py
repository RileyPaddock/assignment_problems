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