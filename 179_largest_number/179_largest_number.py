import random


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)
        if nums[0] == "0":
            return "0"
        return "".join(nums)


random.seed(1)

hello = Solution()
# print(hello.largestNumber([random.randint(0, 1000) for _ in range(5)]))
print(hello.largestNumber([999999991, 9]))
