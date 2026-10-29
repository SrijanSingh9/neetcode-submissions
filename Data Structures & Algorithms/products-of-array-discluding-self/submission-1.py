
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prd = [1] * n

        # Pass 1: Product of all elements to the left
        left = 1
        for i in range(n):
            prd[i] = left
            left *= nums[i]

        # Pass 2: Multiply by product of all elements to the right
        right = 1
        for i in range(n - 1, -1, -1):
            prd[i] *= right
            right *= nums[i]

        return prd
