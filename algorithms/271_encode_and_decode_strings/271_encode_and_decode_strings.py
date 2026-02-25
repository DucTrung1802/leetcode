from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        output = []
        current_len_s = ""
        current_len_n = 0
        i = 0
        while i < len(s):
            if s[i] in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "0",
            ] and i + 1 < len(s):
                current_len_s += s[i]
                i += 1
            else:
                current_len_n = int(current_len_s)

                output.append(s[i + 1 : i + current_len_n + 1])

                current_len_s = ""
                i += current_len_n + 1

        return output


hello = Solution()
print(hello.decode(hello.encode(["we", "say", ":", "yes", "!@#$%^&*()"])))
