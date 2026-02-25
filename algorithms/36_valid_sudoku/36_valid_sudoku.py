from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for i in range(len(board)):
            # Create new bucket for each row
            row[i] = {}

            for j in range(len(board[i])):
                # Create new bucket for each column only if iterating first row
                if i == 0:
                    col[j] = {}

                # Create bucket for each box
                if i % 3 == 0 and j % 3 == 0:
                    box[(i // 3, j // 3)] = {}

                # Double check if existed
                element = board[i][j]
                if element != "." and (
                    element in row[i]
                    or element in col[j]
                    or element in box[(i // 3, j // 3)]
                ):
                    return False

                row[i][element] = 1
                col[j][element] = 1
                box[(i // 3, j // 3)][element] = 1

        return True


hello = Solution()
print(
    hello.isValidSudoku(
        [
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
    )
)
