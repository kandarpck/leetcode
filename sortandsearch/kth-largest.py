from random import randint


class Solution(object):
    def findKthLargest(self, nums, k):
        low, hi = 0, len(nums) - 1
        while low <= hi:
            rand_pivot = randint(low, hi)
            pivot_idx = self.partition_around_pivot(low, hi, nums, rand_pivot)
            if pivot_idx == k - 1:
                return nums[pivot_idx]
            elif pivot_idx < k - 1:
                low = pivot_idx + 1
            else:
                hi = pivot_idx - 1

    def partition_around_pivot(self, low, hi, nums, rand_pivot):
        pivot_value = nums[rand_pivot]
        pivot_idx = low
        nums[hi], nums[rand_pivot] = nums[rand_pivot], nums[hi]
        for i in range(low, hi):
            if nums[i] > pivot_value:
                nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                pivot_idx += 1

        nums[hi], nums[pivot_idx] = nums[pivot_idx], nums[hi]
        return pivot_idx


nums = [9, 1, 4, 2, 3, 8, 7, 6]
print(Solution().findKthLargest(nums, k=3))
