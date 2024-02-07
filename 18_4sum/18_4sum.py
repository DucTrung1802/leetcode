# Not my solution


class Solution:
    def fourSum(self, nums: list[int], target: int):
        ans = []

        def nSum(
            l: int, r: int, target: int, n: int, path: list[int], ans: list[list[int]]
        ) -> None:
            """Finds n numbers that add up to the target in [l, r]."""
            # If the number of element in list is smaller than the number of components
            # If the number of components is 1
            # If multiplication of smallest components is still greater than the target
            # If multiplication of largest components is still smaller than the target
            if r - l + 1 < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
                return
            if n == 2:
                while l < r:
                    summ = nums[l] + nums[r]
                    if summ == target:
                        ans.append(path + [nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1
                return

            for i in range(l, r + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue

                nSum(i + 1, r, target - nums[i], n - 1, path + [nums[i]], ans)

        nums.sort()

        nSum(0, len(nums) - 1, target, 4, [], ans)

        return ans


# hello = Solution()
# for item in hello.fourSum([1, 0, -1, 0, -2, 2], 0):
#     print(item)
