# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        Time: O(n log n) if not sorted else O(n)
        Space: O(1)
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        idx = 0
        while idx < len(intervals) - 1:
            current = intervals[idx]
            next = intervals[idx + 1]
            if current.end >= next.start:
                current.end = max(current.end, next.end)
                del intervals[idx + 1]
            else:
                idx += 1
        return intervals


if __name__ == '__main__':
    ip = [Interval(1, 2), Interval(2, 4), Interval(4, 6), Interval(7, 9)]
    print(Solution().merge(ip))
    ip = []
    print(Solution().merge(ip))
