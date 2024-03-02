import copy


def print_sudoku(board: list[list[str]]) -> None:
    print()
    for i in range(len(board)):
        print(board[i])
    print()


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def rc2g(i, j):  # row,col to group idx
            return i - i % 3 + j // 3

        def rm(i, j, x, masks):
            mask = 1 << x
            masks[0][i] |= mask
            masks[1][j] |= mask
            masks[2][rc2g(i, j)] |= mask

        def GD():  # Greedy
            nonlocal cur, board, rest
            new = True
            while new:
                new = False
                nxt = [[0] * 9 for i in range(3)]
                for i in range(9):
                    for j in range(9):
                        if isinstance(board[i][j], int):
                            maskr = cur[0][i]
                            maskc = cur[1][j]
                            maskg = cur[2][rc2g(i, j)]
                            board[i][j] &= ~(maskr | maskc | maskg)
                            if board[i][j] == 0:
                                return False
                            if board[i][j].bit_count() == 1:
                                x = board[i][j].bit_length()
                                board[i][j] = str(x)
                                rm(i, j, x - 1, nxt)
                                rm(i, j, x - 1, cur)
                                rest -= 1
                                new = True
                cur = nxt
            if rest:
                return BF()
            return True

        def BF():  # Brute-Force
            nonlocal cur, board, rest
            for i in range(9):
                for j in range(9):
                    if isinstance(board[i][j], int):
                        rest -= 1
                        r = rest
                        org = [row[:] for row in board]
                        for x in range(board[i][j].bit_length()):
                            if not (board[i][j] >> x) & 1:
                                continue
                            board[i][j] = str(x + 1)
                            rm(i, j, x, cur)
                            if GD() is True:
                                return True
                            for ii in range(9):
                                for jj in range(9):
                                    board[ii][jj] = org[ii][jj]
                            cur = [[0] * 9 for i in range(3)]
                            rest = r
                        return False

        rest = 81
        # 1x9 row, 9x1 col, 3x3 group
        cur = [[0] * 9 for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    # bit: 111111111
                    board[i][j] = 511
                else:
                    x = int(board[i][j]) - 1
                    rm(i, j, x, cur)
                    rest -= 1
        GD()


sudoku_board = [
    [".", "7", ".", ".", ".", "5", ".", ".", "."],
    ["1", ".", ".", ".", "3", ".", "5", ".", "8"],
    [".", ".", ".", "2", ".", "9", ".", "6", "."],
    ["9", "1", ".", "5", ".", ".", "4", "2", "."],
    ["6", "8", ".", "3", ".", ".", ".", "1", "."],
    ["2", "5", "4", ".", "9", ".", ".", ".", "3"],
    ["7", ".", "6", "8", ".", "1", ".", "4", "."],
    ["3", "4", "5", ".", ".", "6", ".", "7", "1"],
    [".", ".", "1", ".", "7", ".", "2", ".", "6"],
]

print_sudoku(sudoku_board)

solution = Solution()
solution.solveSudoku(sudoku_board)

print_sudoku(sudoku_board)
