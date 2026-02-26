from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_len = len(nums)

        i = 0
        while i < current_len:
            if nums[i] != val:
                i += 1
            else:
                nums.remove(val)
                current_len -= 1

        return current_len


hello = Solution()
print(hello.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
