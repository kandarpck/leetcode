class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.calculate(prices, 0)

    def calculate(self, prices, index):
        if index >= len(prices):
            return 0
        maximum = 0
        for start in range(index, len(prices)):
            maxprofit = 0
            for i in range(start + 1, len(prices)):
                if prices[start] < prices[i]:
                    profit = self.calculate(prices, i + 1) + prices[i] - prices[start]
                    if profit > maxprofit:
                        maxprofit = profit
            if maxprofit > maximum:
                maximum = maxprofit
        return maximum


if __name__ == '__main__':
    sol = Solution()
    ip = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(ip))
    print(ip)
