class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        replace = 0
        for number in nums:
            if number != nums[replace]:
                replace += 1
                nums[replace] = number
        return replace + 1


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 1, 2, 2]
    print(sol.removeDuplicates(ip))
    print(ip)
