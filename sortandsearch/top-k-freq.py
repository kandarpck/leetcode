from collections import Counter


class Solution(object):
    # one pass dutch partitioning problem
    # Time: O(nlogk)
    # Space: O(n)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_counter = Counter(nums)
        return [val for val, _ in nums_counter.most_common(k)]


class Solution2(object):
    # one pass dutch partitioning problem
    # Time: O(n)
    # Space: O(n)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, count in nums_counter.items():
            buckets[count].append(i)

        res = []
        for i in reversed(range(len(buckets))):
            if buckets[i]:
                for j in range(len(buckets[i])):
                    res.append(buckets[i][j])
                    if len(res) == k:
                        return res
        return res


if __name__ == '__main__':
    nums = [0, 2, 2, 0, 1, 0, 2, 1, 3, 2, 2, 2]
    print(Solution().topKFrequent(nums, k=2))
    print(Solution2().topKFrequent(nums, k=2))
