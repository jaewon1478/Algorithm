class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] * nums[i]
        nums = sorted(nums)
        return nums