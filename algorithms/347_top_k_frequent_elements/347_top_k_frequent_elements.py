from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}

        for num in nums:
            if num not in buckets:
                buckets[num] = 1
            else:
                buckets[num] += 1

        keys = [k for (k, v) in sorted(buckets.items(), key=(lambda x: -x[1]))]

        return keys[:k]


hello = Solution()
print(hello.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
