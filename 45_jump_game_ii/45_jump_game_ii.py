class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        list_step: list[int] = []

        current_index = len(nums) - 1
        while current_index >= 0:
            if current_index == 0:
                can_step_to = current_index + nums[current_index]
                skip_step = 0
                for i in range(1, len(list_step)):
                    if can_step_to < list_step[i]:
                        break
                    skip_step += 1
                list_step = list_step[skip_step:]
                list_step = [current_index] + list_step

            else:
                for back_step in range(1, current_index + 1):
                    if nums[current_index - back_step] >= back_step:
                        if len(list_step) == 0:
                            list_step = [current_index] + list_step
                        else:
                            can_step_to = current_index + nums[current_index]
                            skip_step = 0
                            for i in range(1, len(list_step)):
                                if can_step_to < list_step[i]:
                                    break
                                skip_step += 1
                            list_step = list_step[skip_step:]

                            list_step = [current_index] + list_step

                        break

            current_index -= back_step

        return len(list_step) - 1


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [2, 1, 3, 0, 3, 0, 4, 0, 5, 5,  3,  2,  3,  5,  4,  4,  2,  2,  1,  1]
hello = Solution()
print(hello.jump([4, 2, 1, 1]))
