class Solution(object):
    def twoSum(self, nums, target):
        """
        Time: N^2
        Space 1
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        """
        Time: N
        Space: N
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for idx, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], idx]
            lookup[num] = idx


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 1, 2, 9, 2, 4, 5]
    print(sol.twoSum(ip, 3))
    print(sol.twoSum2(ip, 9))
