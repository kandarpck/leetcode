class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        for j in range(pos, len(nums)):
            nums[j] = 0


if __name__ == '__main__':
    sol = Solution()
    ip = [9, 0, 9, 9, 0, 9, 9, 9, 9]
    sol.moveZeroes(ip)
    print(ip)
