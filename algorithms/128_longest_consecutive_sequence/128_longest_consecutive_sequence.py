from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        l = len(nums)
        for i in nums:
            if i - 1 not in nums:
                cnt = 1
                while i + cnt in nums:
                    cnt += 1
                if ans < cnt:
                    ans = cnt
                if cnt > l // 2:
                    break

        return ans


hello = Solution()
print(hello.longestConsecutive([100, 4, 200, 1, 3, 2]))
