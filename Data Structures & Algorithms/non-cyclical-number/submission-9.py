class Solution:
    def isHappy(self, n: int) -> bool:
        squares = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

        while n > 6:
            total = 0

            for digit in str(n):
                total += squares[ord(digit) - 48]

            n = total

        return n == 1 or n == 7