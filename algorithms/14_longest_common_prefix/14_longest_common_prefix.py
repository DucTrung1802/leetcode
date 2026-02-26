from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        sample = strs[0]
        for s in strs[1:]:
            if len(s) < len(sample):
                sample = s

        i = 0
        while i < len(strs):
            if len(sample) == 0:
                break

            if sample in strs[i][: len(sample)]:
                i += 1
            else:
                sample = sample[:-1]
                i = 0

        return sample


hello = Solution()
print(hello.longestCommonPrefix(["flower", "flow", "flight"]))
