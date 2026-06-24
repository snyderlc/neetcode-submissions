from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
     num_map = defaultdict(int)

     for n in nums:
      if n not in num_map:
        num_map[n] = 0
      else:
        num_map[n] = 1   
     no_dup = [key for key, val in num_map.items() if val == 0]
     return no_dup.pop()

        