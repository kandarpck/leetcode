class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        if not s:
            return max_length
        prev = [s[0]]
        for char in s[1:]:
            if char in prev:
                p_idx = prev.index(char)
                max_length = max(max_length, len(prev))
                prev = prev[p_idx + 1:] + [char]
            else:
                prev.append(char)
        return max(max_length, len(prev))


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))
    print(Solution().lengthOfLongestSubstring('dvdk'))
