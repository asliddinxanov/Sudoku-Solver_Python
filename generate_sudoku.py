import random

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, pos):
    row, col = pos
    size = len(board)
    box_size = int(size ** 0.5)

    # 行をチェック
    if num in board[row]:
        return False

    # 列をチェック
    if num in [board[i][col] for i in range(size)]:
        return False

    # 3x3のボックスをチェック
    box_x, box_y = col // box_size, row // box_size
    for i in range(box_y * box_size, box_y * box_size + box_size):
        for j in range(box_x * box_size, box_x * box_size + box_size):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, len(board) + 1):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def generate_board(size):
    board = [[0] * size for _ in range(size)]
    for _ in range(size):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        num = random.randint(1, size)
        if is_valid(board, num, (row, col)):
            board[row][col] = num
    return board


def generate_and_solve_sudoku():
    while True:
        size = int(input("数独のサイズを入力してください（4, 9, 16など）: "))
        if size ** 0.5 == int(size ** 0.5):
            break
        else:
            print("サイズは完全な平方数でなければなりません。もう一度入力してください。")

    board = generate_board(size)
    print("生成された数独パズル:")
    print_board(board)

    if solve(board):
        print("\n解いた数独パズル:")
        print_board(board)
    else:
        print("\n解法が見つかりませんでした。")
