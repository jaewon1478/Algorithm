"""
Three ways to solve this problem: using reverse function, Recursion, and two pointers.
1. reverse function
def reverseString(self, s: list[str]) -> None:
  s.reverse()

"""
# 2. Recursion
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right - 1)
        helper(0, len(s) - 1)

"""
3. Two Pointers
def reverseString(self, list[str]) -> None:
  left = 0
  right = len(s) - 1
        
  while left < right:
    s[left], s[right] = s[right], s[left]
    left, right = left + 1, right - 1
"""