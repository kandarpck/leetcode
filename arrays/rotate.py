class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        1,2,3,4,5
        3
        3,4,5,1,2
        """
        move = k % len(nums)
        nums[:] = nums[-move:] + nums[:-move]
