import copy


def print_sudoku(board: list[list[str]]) -> None:
    for i in range(len(board)):
        print(board[i])


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isDuplicate(number: int) -> bool:
            return (
                (number in horizontal_matrix)
                or (number in vertical_matrix)
                or (number in cube_matrix)
            )

        def addNumberToBoard(row: int, col: int, number: int) -> None:
            horizontal_matrix[row][col] = str(number)

            vertical_matrix[col][row] = str(number)

            cube_matrix_row = int(row / 3) * 3 + int(col / 3)
            cube_matrix_col = (row % 3) * 3 + int(col % 3)
            cube_matrix[cube_matrix_row][cube_matrix_col] = str(number)

        horizontal_matrix: list[list[str]] = copy.deepcopy(board)

        vertical_matrix: list[list[str]] = [list(row) for row in zip(*board)]

        cube_matrix: list[list[str]] = []
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                cube_row = []
                for row in board[i : i + 3]:
                    cube_row.extend(row[j : j + 3])
                cube_matrix.append(cube_row)

        # print_sudoku(board)
        # print()
        # print_sudoku(horizontal_matrix)
        # print()
        # print_sudoku(vertical_matrix)
        # print()
        # print_sudoku(cube_matrix)


sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solution = Solution()
solution.solveSudoku(sudoku_board)
