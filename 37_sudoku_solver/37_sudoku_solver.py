import copy


def print_sudoku(board: list[list[str]]) -> None:
    print()
    for i in range(len(board)):
        print(board[i])
    print()


class Solution:
    empty_mark = "."
    selected_mark = "o"

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isDuplicate(row: int, col: int, number: int) -> bool:
            number = str(number)
            return (
                (number in horizontal_matrix[row])
                or (number in vertical_matrix[col])
                or (number in cube_matrix[int(row / 3) * 3 + int(col / 3)])
            )

        def addToBoard(row: int, col: int, value) -> None:
            horizontal_matrix[row][col] = str(value)

            vertical_matrix[col][row] = str(value)

            cube_matrix_row = int(row / 3) * 3 + int(col / 3)
            cube_matrix_col = (row % 3) * 3 + int(col % 3)
            cube_matrix[cube_matrix_row][cube_matrix_col] = str(value)

        def addEmptyMark(row: int, col: int):
            addNumberToBoard(row, col, self.empty_mark)
            board[row][col] = self.empty_mark

        def addNumberToBoard(row: int, col: int, number) -> None:
            addToBoard(row, col, number)
            board[row][col] = self.selected_mark

        def getCurrentNumber(row: int, col: int) -> int:
            try:
                return int(horizontal_matrix[row][col])
            except ValueError:
                return 0

        def moveToNextNumber(row: int, col: int) -> tuple:
            if col == 8:
                col = 0
                row += 1
            else:
                col += 1

            travel_forward = True

            return (row, col, travel_forward)

        def moveToPreviousNumber(row: int, col: int) -> tuple:
            if col == 0:
                col = 8
                row -= 1
            else:
                col -= 1

            travel_forward = True

            return (row, col, not travel_forward)

        horizontal_matrix: list[list[str]] = copy.deepcopy(board)

        vertical_matrix: list[list[str]] = [list(row) for row in zip(*board)]

        cube_matrix: list[list[str]] = []

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                cube_row = []
                for row in board[i : i + 3]:
                    cube_row.extend(row[j : j + 3])
                cube_matrix.append(cube_row)

        row: int = 0
        col: int = 0
        travel_forward: bool = True

        # Coordinates of the first empty value
        start_row_empty_value = -1
        start_col_empty_value = -1

        while 0 <= row <= 8 and 0 <= col <= 8:
            # Fixed number
            if (
                board[row][col] != self.empty_mark
                and board[row][col] != self.selected_mark
            ):
                if not travel_forward and not (
                    row == start_row_empty_value and col == start_col_empty_value
                ):
                    row, col, travel_forward = moveToPreviousNumber(row, col)
                else:
                    row, col, travel_forward = moveToNextNumber(row, col)

                continue

            # Empty mark
            if board[row][col] == self.empty_mark:
                if start_row_empty_value < 0:
                    start_row_empty_value = row
                    start_col_empty_value = col

                for i in range(1, 10):
                    if isDuplicate(row, col, i):
                        # i reaches max value and still duplicate -> we need to get back a step and change previous value
                        if i == 9:
                            addEmptyMark(row, col)
                            row, col, travel_forward = moveToPreviousNumber(row, col)
                            break
                    else:
                        addNumberToBoard(row, col, i)
                        row, col, travel_forward = moveToNextNumber(row, col)
                        break

            # Selected mark
            elif board[row][col] == self.selected_mark:
                current_value = getCurrentNumber(row, col) + 1

                # Sill available to test this current value
                while 1 <= current_value <= 9:
                    if not isDuplicate(row, col, current_value):
                        addNumberToBoard(row, col, current_value)
                        break
                    current_value += 1

                # Get back a step
                else:
                    addEmptyMark(row, col)
                    row, col, travel_forward = moveToPreviousNumber(row, col)
                    continue

                # Select next value
                row, col, travel_forward = moveToNextNumber(row, col)

        for i in range(0, 9):
            for j in range(0, 9):
                board[i][j] = horizontal_matrix[i][j]

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

print_sudoku(sudoku_board)

solution = Solution()
solution.solveSudoku(sudoku_board)

print_sudoku(sudoku_board)
