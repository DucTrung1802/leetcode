class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        for current_index in range(len(nums)):
            if current_index == len(nums) - 1:
                return True

            if nums[current_index] == 0:
                for back_step in range(1, current_index + 1):
                    if nums[current_index - back_step] > back_step:
                        break
                    elif current_index - back_step == 0:
                        return False

        return True


hello = Solution()
print(hello.canJump([2, 0, 0]))
