class Solution:
    def print_board(self, board: list[list[int]]):
        for i in range(len(board)):
            print("[", end="")
            for j in range(len(board[0])):
                print(f" {board[i][j]} ", end="")
            print("]")

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])

        self.board: list[list[str]] = board
        self.word: str = word
        self.mask_board: list[list[int]] = []
        self.is_complete: bool = False

        for i in range(self.m):
            self.mask_board.append([0] * self.n)

        # self.print_board(self.mask_board)

        for i in range(self.m):
            for j in range(self.n):
                self.travel_over_board([], [i, j])

                if self.is_complete:
                    return True

        return False

    def travel_over_board(
        self, current_path: list[list[int, int]], current_cell: list[int, int]
    ):
        # Validate current cell
        row = current_cell[0]
        col = current_cell[1]
        current_index_in_word = len(current_path)

        # Current cell is correct
        if self.board[row][col] == self.word[current_index_in_word]:
            current_path.extend([[row, col]])
            self.mask_board[row][col] = 1
            # Current cell is last character in word string
            if len(current_path) == len(self.word):
                self.is_complete = True
                return

        # If current cell is not correct
        else:
            return

        # Travel right
        if col + 1 < self.n and self.mask_board[row][col + 1] == 0:
            self.travel_over_board(current_path, [row, col + 1])
            if self.is_complete:
                return

        # Travel down
        if row + 1 < self.m and self.mask_board[row + 1][col] == 0:
            self.travel_over_board(current_path, [row + 1, col])
            if self.is_complete:
                return

        # Travel left
        if col - 1 >= 0 and self.mask_board[row][col - 1] == 0:
            self.travel_over_board(current_path, [row, col - 1])
            if self.is_complete:
                return

        # Travel up
        if row - 1 >= 0 and self.mask_board[row - 1][col] == 0:
            self.travel_over_board(current_path, [row - 1, col])
            if self.is_complete:
                return

        self.mask_board[row][col] = 0
        current_path.pop()


my_board = [["a", "b"], ["c", "d"]]
word = "abdc"

hello = Solution()
print(hello.exist(my_board, word))
