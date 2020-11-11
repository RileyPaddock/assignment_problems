def quicksort(list_):
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
        
print(quicksort([10,2,7,1,8,3,9,6,5,4]))