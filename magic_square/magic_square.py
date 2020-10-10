def is_valid(arr):
    for row in arr:
        if None not in row:
            row_sum = [elem for elem in row if elem is not None]
            if len(row_sum) == len(arr) and sum(row_sum) != 15:
                return False

    diag = [arr[i][j]  for i in range(len(arr)) for j in range(len(arr[i])) if i == j and arr[i][j] is not None]
    if len(diag) == len(arr) and sum(diag) != 15:
        return False 



    columns = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            columns[j].append(arr[i][j])
    for column in columns:
        if None not in column and sum(column) != 15:
            return False

    return True

def make_magic_square():
    magic_square = []
    for tl in range(1,10):
        for tm in range(1,10):
            if tl not in [tm] and (15 - (tl+tm)) in range(1,10):
                for ml in range(1,10):
                    if ml not in [tm, tl] and (15 - (tl+ml)) in range(1,10):
                            for mm in range(1,10):
                                if mm not in [tm,tl,ml]:
                                    if len([x for x in [(tm+mm), (tl+mm),(ml+mm)] if 15-x in range(1,10)]) == 3:
                                        tr = 15 - (tl + tm)
                                        bl = 15 - (tl + ml)
                                        if tr+bl+mm == 15:
                                            mr = 15 - (ml + mm)
                                            bm = 15 - (tm + mm)
                                            br = 15 - (tl + mm)
                                            magic_square = [[tl,tm,tr],[ml,mm,mr],[bl,bm,br]]
                                            if is_valid(magic_square):
                                                return magic_square


    
    
            


arr1 = [[1,2,None], [None,3,None], [None,None,None]]
print(is_valid(arr1))
#True    (because no rows, columns, or diagonals are completely filled in) 

arr2 = [[1,2,None], [None,3,None], [None,None,4]] 
print(is_valid(arr2))
#False   (because a diagonal is filled in and it doesn't sum to 15)

arr3 = [[1,2,None], [None,3,None], [5,6,4]] 
print(is_valid(arr3))
#False   (because a diagonal is filled in and it doesn't sum to 15)
        #(it doesn't matter that the bottom row does sum to 15)

arr4 = [[None,None,None], [None,3,None], [5,6,4]] 
print(is_valid(arr4))
#True   (because there is one row that's filled in and it sums to 15)

print(make_magic_square())