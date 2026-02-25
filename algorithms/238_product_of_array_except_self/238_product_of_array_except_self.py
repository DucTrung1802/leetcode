from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 1
        right = 1
        output = [1] * n

        for i in range(n):
            output[i] *= left
            left *= nums[i]

        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output


hello = Solution()
print(hello.productExceptSelf([1, 2, 3, 4]))
