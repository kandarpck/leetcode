class Solution(object):

    def containsDuplicate(self, nums):
        """ Brute Force Solution
        Time N^2, Space 1
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplciateOptimized(self, nums):
        """
        Time N lg N
        Memory 1
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def containsDuplicateSet(self, nums):
        """
        Time N
        Space N
        :type nums: List[int]
        :rtype: bool
        """
        distinct_nums = set()
        for number in nums:
            if number in distinct_nums:
                return True
            distinct_nums.add(number)
        return False


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 2, 9, 3, 4, 8, 444, 2]
    print(sol.containsDuplicate(ip))
    print(sol.containsDuplciateOptimized(ip))
    print(sol.containsDuplicateSet(ip))
