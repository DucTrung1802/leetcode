import math


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])

        str_list = list(map(str, nums))
        result = ""

        while len(str_list) > 0:
            current_best = str_list[0]
            for index in range(1, len(str_list)):

                # Length is equal, compare magnitude
                if (
                    len(str_list[index]) == len(current_best)
                    and str_list[index] > current_best
                ):
                    current_best = str_list[index]

                # If length is smaller, then multiply the smaller one
                if len(str_list[index]) < len(current_best):
                    length_diff = len(current_best) - len(str_list[index])
                    extend_str_list_index = (
                        str_list[index]
                        + (str_list[index] * (length_diff // len(str_list[index]) + 1))[
                            :length_diff
                        ]
                    )
                    if extend_str_list_index > current_best:
                        current_best = str_list[index]

                elif len(current_best) < len(str_list[index]):
                    length_diff = len(str_list[index]) - len(current_best)
                    extend_current_best = (
                        current_best
                        + (current_best * (length_diff // len(current_best) + 1))[
                            :length_diff
                        ]
                    )
                    if str_list[index] > extend_current_best:
                        current_best = str_list[index]

            result += current_best
            str_list.remove(current_best)

        return result


hello = Solution()
print(hello.largestNumber([432, 43243]))
