from cgi import MiniFieldStorage


class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int:
    nums.append('inf')
    left, right = 0, len(nums) - 1

    while left < right:
      mid = (left + right) // 2
      if target <= nums[mid]:
        right = mid
      else:
        left = mid + 1
    return right