from collections import defaultdict
class Solution:
    def hammingWeight(self, n: int) -> int:

      binary_str = f"{n:b}"
      print (binary_str)
      count = 0
      for i in binary_str:
        if i == "1":
          count+=1
      return count

        