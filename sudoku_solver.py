
def solve_puzzle(puzzle):
    break_cue = False
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                empty_square = (i, j)
                break_cue = True
        if break_cue: 
            break
    else:
        return True

    for possible_num in range(1,7):
        if check(puzzle, possible_num, empty_square):
            puzzle[empty_square[0]][empty_square[1]] = possible_num
            if solve_puzzle(puzzle):
                return True
            else:
                puzzle[empty_square[0]][empty_square[1]] = 0
    else:
        return False


def check(puzzle, possible_num, pos):

    for i in range(6):
        if puzzle[pos[0]][i] == possible_num and pos[1] != i:
            return False

    for i in range(6):
        if puzzle[i][pos[1]] == possible_num and pos[0] != i:
            return False

    for i in range((pos[0] // 2)*2, (pos[0] // 2)*2 + 2):
        for j in range((pos[1] // 3) * 3, (pos[1] // 3)*3 + 3):
            if puzzle[i][j] == possible_num and (i,j) != pos:
                return False

    return True


def print_board(puzzle):
    print("-----------------")
    for row in range(6):
        print("|"+str('  '.join([str(puzzle[row][i]) for i in range(3)]))+"|"+str('  '.join([str(puzzle[row][i]) for i in range(3,6)]))+"|")
        if (row+1)%2 == 0:
            print("-----------------")



puzzle = [[0,0,4,0,0,0],[0,0,0,2,3,0],[3,0,0,0,6,0],[0,6,0,0,0,2],[0,2,1,0,0,0],[0,0,0,5,0,0]]
print(solve_puzzle(puzzle))
print_board(puzzle)