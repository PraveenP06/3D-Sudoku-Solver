def is_valid_board(board):
    def valid(unit):
        unit = [num for num in unit if num != 0]  # Remove zeros
        return len(unit) == len(set(unit))  # Remove duplicates

    for row in board:
        if not valid(row):
            return False

    for col in zip(*board):
        if not valid(col):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[row + i][col + j])
            if not valid(subgrid):
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve_2d_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True 

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_2d_sudoku(board):
                return True
            else:
                board[row][col] = 0 

    return False

def is_valid_3d_cube(cube):
    def valid(unit):
        unit = [num for num in unit if num != 0]
        return len(unit) == len(set(unit))

    # Check each 2D layer
    for layer in cube:
        if not is_valid_board(layer):
            return False

    # Check columns
    for row in range(9):
        for col in range(9):
            column = [cube[layer][row][col] for layer in range(9)]
            if not valid(column):
                return False

    # Check depths
    for layer in range(9):
        for col in range(9):
            depth = [cube[layer][row][col] for row in range(9)]
            if not valid(depth):
                return False

    # Check 3x3x3 sub-cubes
    for l in range(0, 9, 3):
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sub_cube = []
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            sub_cube.append(cube[l + i][r + j][c + k])
                if not valid(sub_cube):
                    return False

    return True

def solve_3d_sudoku(cube):
    # Solve each 2D layer first
    for layer in range(9):
        if not solve_2d_sudoku(cube[layer]):
            return False

    # Then ensure the 3D constraints
    if is_valid_3d_cube(cube):
        return True
    return "Invalid"   #If I change this line to False, the code does not work

def print_cube(cube):
    for layer in range(9):
        print(f"Layer {layer + 1}:")
        for row in range(9):
            for col in range(9):
                print(cube[layer][row][col], end=" ")
            print()
        print()

# Test cube
cube = [[[0 for _ in range(9)] for _ in range(9)] for _ in range(9)]

# Example to fill some initial values in the cube
cube[0][0][0] = 8
cube[0][1][3] = 2
cube[0][2][7] = 4
cube[0][4][4] = 9

cube[1][0][0] = 5
cube[1][3][1] = 9
cube[1][7][8] = 3

cube[2][0][0] = 2
cube[2][1][5] = 7
cube[2][5][1] = 5
cube[2][6][6] = 8

cube[3][2][0] = 7
cube[3][3][5] = 6
cube[3][7][2] = 1

cube[4][0][2] = 4
cube[4][4][6] = 8
cube[4][8][8] = 5

cube[5][1][2] = 6
cube[5][2][4] = 2
cube[5][6][6] = 4
cube[5][7][8] = 1

cube[6][2][0] = 1
cube[6][3][3] = 3
cube[6][7][5] = 6

cube[7][0][0] = 6
cube[7][1][4] = 8
cube[7][5][8] = 2
cube[7][8][3] = 7

cube[8][1][1] = 3
cube[8][3][5] = 5
cube[8][7][7] = 9


if is_valid_3d_cube(cube):
    if solve_3d_sudoku(cube):
        print("3D Sudoku solved successfully:")
        print_cube(cube)
else:
    print("Given cube is not valid. Please try again.")
