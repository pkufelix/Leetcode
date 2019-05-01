"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    """
    Go through the whole array to check if the sum is increasing. If the previous count is negative, start new count.
    O(n)
    """
        if not nums:
            return Null    
        if len(nums) == 1:
            return nums[0]
        left = 1
        count = nums[0]
        res = nums[0]
        while left < len(nums):
            if count > 0:
                count += nums[left]
            else:
                count = nums[left]
            if count > res:
                res = count
            left += 1
        return res

from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        win = 0
        pivot = 0
        while pivot < len(nums):
            count = 0
            while win < len(nums):
                count += nums[win]
                if count > res:
                    res = count
                if count < 0:
                    win += 1
                    break
                win += 1
            pivot = win
        return res