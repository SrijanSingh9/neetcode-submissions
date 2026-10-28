class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            total = 0

            for digit in str(n):
                d = int(digit)
                total += d * d

            n = total

        return n == 1