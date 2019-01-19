class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time: O(log n)
        Space: O(1)
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            m1 = (low + high) // 2
            m2 = m1 + 1
            if nums[m1 - 1] < nums[m1] and nums[m1] > nums[m2]:
                return m1
            if nums[m1] > nums[m2]:
                high = m1
            else:
                low = m2
        return low


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 7, 9, 11, 13, 12, 10, 8, 6, 4]))
