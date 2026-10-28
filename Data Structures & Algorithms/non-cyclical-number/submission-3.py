class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            cycle = 0

            for i in str(n):
                cycle += int(i) ** 2

            n = cycle

        return n == 1

        