# Not my solution


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        special_chars = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in special_chars:
                opposite_char = special_chars[c]
                if len(stack) > 0 and stack[-1] == opposite_char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        return False


# hello = Solution()
# print(hello.isValid("{}()"))
