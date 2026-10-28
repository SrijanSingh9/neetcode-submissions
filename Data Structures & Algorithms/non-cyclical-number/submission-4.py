class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total
# Floyd’s Cycle Detection Algorithm
        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1