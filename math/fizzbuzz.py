class Solution:
    def fizzBuzz(self, nn):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for n in range(1, nn + 1):
            if n % 3 == 0 and n % 5 == 0:
                res.append("FizzBuzz")
            elif n % 3 == 0:
                res.append("Fizz")
            elif n % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(n))
        return res


if __name__ == "__main__":
    print(Solution().fizzBuzz(100))
    print(Solution().fizzBuzz(1))
