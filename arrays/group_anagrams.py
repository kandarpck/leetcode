from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for word in strs:
            res[''.join(sorted(word))].append(word)
        return list(res.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print([
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ])
