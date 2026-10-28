from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        # Index = frequency, value = numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        result = []

        # Start with the highest frequency
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result