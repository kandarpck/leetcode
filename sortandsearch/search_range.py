class Solution:

    def search_start(self, nums, start, end):
        g_end = end
        while nums[start] != nums[g_end]:
            mid = (start + end) // 2
            if nums[mid] == nums[g_end]:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def search_end(self, nums, start, end):
        g_start = start
        while nums[end] != nums[g_start]:
            mid = (start + end) // 2
            if nums[mid] == nums[g_start]:
                start = mid + 1
            else:
                end = mid - 1
        return end

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                s = self.search_start(nums, low, mid)
                e = self.search_end(nums, mid, high)
                return [s, e]
        return [-1, -1]
