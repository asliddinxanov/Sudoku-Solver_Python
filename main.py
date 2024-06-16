# 数独解決プログラム（Sudoku solving program）
# BOBURKHONOV ASLIDDIN
# https://github.com/asliddinxanov/Sudoku-Solver_Python

from solve_sudoku import solve_existing_sudoku
from generate_sudoku import generate_and_solve_sudoku

def main():
    while True:
        choice = int(input("ある数独を解きたい場合は”1”,\nランダムで数独を作成したい場合は＝”2”を押してください: "))
        if choice == 1:
            solve_existing_sudoku()
            break
        elif choice == 2:
            generate_and_solve_sudoku()
            break
        else:
            print("無効な選択です。もう一度入力してください。")

if __name__ == "__main__":
    main()
