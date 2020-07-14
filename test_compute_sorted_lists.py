from compute_sorted_lists import compute_sorted_lists

x_arrs = [[1,3,4,5,7],[1,3,5,7,9],[-10,-2,0,5],[1,2,2,3,4],[1,2,2,3,4,4]]
y_arrs = [[2,6],[2,4,6,8],[-6.-4,-2,0,2],[1,3,3,4],[1,2,2,3,4,4]]

for i in range(len(x_arrs)):
    print(compute_sorted_lists(x_arrs[i],y_arrs[i]))