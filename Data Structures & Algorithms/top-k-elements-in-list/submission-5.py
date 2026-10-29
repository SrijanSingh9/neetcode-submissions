class Solution:
    def topKFrequent(self, nums, k):
        counts = {}

        # 1. Count frequencies
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # 2. Group numbers by frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        # 3. Collect the k most frequent numbers
        result = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        return result