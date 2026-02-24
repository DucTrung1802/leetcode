from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            for i in range(len(nums)):
                if nums[i] in nums[i + 1 : i + k + 1]:
                    return True

        return False


hello = Solution()
print(hello.containsNearbyDuplicate([1, 0, 1, 1], 1))
