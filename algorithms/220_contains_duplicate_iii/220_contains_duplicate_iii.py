from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            # Check same bucket
            if bucket_id in buckets:
                return True

            # Check neighbor buckets
            if (
                bucket_id - 1 in buckets
                and abs(num - buckets[bucket_id - 1]) <= valueDiff
            ):
                return True

            if (
                bucket_id + 1 in buckets
                and abs(num - buckets[bucket_id + 1]) <= valueDiff
            ):
                return True

            # Insert current number
            buckets[bucket_id] = num

            # Remove element outside sliding window
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]

        return False


hello = Solution()
hello.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
