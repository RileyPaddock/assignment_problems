def split_quicksort(list_):
    midpoint = list_[len(list_)-1]
    del list_[len(list_)-1]
    leq = []
    greater = []
    for elem in list_:
        if elem <= midpoint:
            leq.append(elem)
        else:
            greater.append(elem)
    if len(leq) > 1 and len(greater)>1:
        maybe = quicksort(leq)+[midpoint]+quicksort(greater)
        return maybe
    elif len(leq) > 1 and len(greater)<=1:
        maybe = quicksort(leq)+[midpoint]+greater
        return maybe
    elif len(greater) > 1 and len(leq)<=1:
        maybe = leq+[midpoint]+quicksort(greater)
        return maybe
    elif len(leq) <=1 and len(greater)<=1:
        leq.append(midpoint)
        return leq+greater

def quicksort(_list, i_range):
    midpoint = _list[i_range[0]]
    s_i = i_range[0]
    for i in range(i_range[0]+1,i_range[1]):
        if _list[i] <= midpoint:
            s_i += 1
            switch(_list,s_i,i)
    switch(_list,i_range[0],s_i)
    if len([x for x in range(i_range[0],s_i)]) > 1:
        quicksort(_list, (i_range[0], s_i))
    if len([x for x in range(s_i+1,i_range[1])]) > 1:
        quicksort(_list, (s_i+1,i_range[1]))
    return _list


def switch(arr,i_1,i_2):
    temp = arr[i_1]
    arr[i_1] = arr[i_2]
    arr[i_2] = temp
    return arr

print(quicksort([44,88,77,22,66,11,99,55,0,33],(0,10)))