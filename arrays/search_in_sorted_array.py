class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if left < mid < right:


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    print(sol.search(nums, 0))
    print(sol.search(nums2, 3))
