class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Time: O(logn)
        Space: O(1)
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


class Solution2:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Time: O(logn)
        Space: O(1)
        """
        # Find the smallest element
        # Which is the rotation index
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        # take into account rotation and
        # run normal binary search
        rot = low
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            real_mid = (mid + rot) % len(nums)
            if nums[real_mid] < target:
                low = mid + 1
            elif nums[real_mid] > target:
                high = mid - 1
            else:
                return real_mid
        return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 8, 1], 1))
    print(Solution2().search([4, 5, 6, 7, 8, 1], 1))
