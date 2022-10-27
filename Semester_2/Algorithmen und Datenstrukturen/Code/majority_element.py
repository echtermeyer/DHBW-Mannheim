# from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common(1)[0][0]

        count = {}
        for num in nums:
            if num not in count.keys():
                count[num] = 1
            else:
                count[num] += 1
        print(count)

        for key, value in count.items():
            print("KV", key, value)
            if value >= len(nums) / 2:
                return key

print(Solution().majorityElement([3, 1, 3]))