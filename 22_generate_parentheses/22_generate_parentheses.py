class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generateParenthesisRecursion(opened: int, closed: int, current_path: str):
            if opened == n and closed == n:
                result.append(current_path)
                return 
            if opened < n:
                generateParenthesisRecursion(opened + 1, closed, current_path + "(")
            if opened > closed:
                generateParenthesisRecursion(opened, closed + 1, current_path + ")")

        if n <= 0:
            return []
        if n == 1:
            return ["()"]

        result = []

        generateParenthesisRecursion(0, 0, "")

        return result


value = 5
solution = Solution()
print(solution.generateParenthesis(value))
