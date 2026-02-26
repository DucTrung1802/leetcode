from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1

        return candidate


hello = Solution()
print(hello.majorityElement([2, 2, 3, 3, 3, 3, 2]))
