class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])

        max_length = len(str(max(nums)))
        str_list = list(map(str, nums))
        result = ""

        for order in range(1, max_length + 1):
            current_best = ""
            for index in range(0, len(str_list)):
                if len(str_list[index]) >= order:
                    if not current_best:
                        current_best = str_list[index]
                        continue
                    else:
                        # Same length
                        if len(current_best) == len(str_list[index]):
                            current_best = "max"

                        # Different length


# hello = Solution()
# hello.largestNumber([3, 30, 34, 5, 9])
