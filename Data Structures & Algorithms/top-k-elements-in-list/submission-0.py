from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNum = defaultdict(int)
        result = []

        for n in nums:
            freqNum[n] += 1

        while k != 0:
            maxVal = max(freqNum.values())

            for n in freqNum:
                if freqNum[n] == maxVal:
                    maxKey = n
                    break

            result.append(maxKey)
            del freqNum[maxKey]
            k -= 1

        return result