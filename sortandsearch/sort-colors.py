class Solution(object):
    # one pass dutch partitioning problem
    # Time: O(n)
    # Space: O(1)
    def sortColors(self, nums):
        c1, c2, c3 = 0, 0, len(nums) - 1
        target = 1
        while c2 <= c3:
            if nums[c2] < target:
                nums[c1], nums[c2] = nums[c2], nums[c1]
                c1 += 1
                c2 += 1
            elif nums[c2] == target:
                c2 += 1
            else:
                nums[c3], nums[c2] = nums[c2], nums[c3]
                c3 -= 1


if __name__ == '__main__':
    nums = [0, 2, 2, 0, 1, 0, 2, 1]
    Solution().sortColors(nums)
    print(nums)
