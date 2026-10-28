class Solution:
    def isHappy(self, n: int) -> bool:
        squares = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

        while n >= 10:
            total = 0

            while n:
                total += squares[n % 10]
                n //= 10

            n = total

        return n == 1 or n == 7