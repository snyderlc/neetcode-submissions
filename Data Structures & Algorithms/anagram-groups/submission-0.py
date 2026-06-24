from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      gramMap = defaultdict(list)
      result = [] #list

      for s in strs:
        alphaS = tuple(sorted(s))
        gramMap[alphaS].append(s)

      for value in gramMap.values():
        result.append(value)

      return result

        