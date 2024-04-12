class Solution:
    def jump(self, nums: list[int]) -> int:
        list_step: list[int] = []

        current_index = len(nums) - 1
        while current_index >= 0:
            for back_step in range(1, current_index + 1):
                if nums[current_index - back_step] >= back_step:
                    if len(list_step) == 0:
                        list_step = [current_index] + list_step
                    else:
                        can_step_to = current_index + nums[current_index]
                        for i in range(0, len(list_step)):
                            if can_step_to > list_step[i]:
                                list_step = list_step[1:]
                            else:
                                list_step = [current_index] + list_step

                current_index = current_index - back_step


# [2, 1, 3, 0, 3, 0, 4, 0, 5, 5, 3, 2, 3, 5, 4, 4, 2, 2, 1, 1]
hello = Solution()
hello.jump([2, 1, 3, 0, 3, 0, 4, 0, 5, 5, 3, 2, 3, 5, 4, 4, 2, 2, 1, 1])
