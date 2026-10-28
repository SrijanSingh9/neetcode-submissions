class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1 and n != 4:
            total = 0

            while n:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1