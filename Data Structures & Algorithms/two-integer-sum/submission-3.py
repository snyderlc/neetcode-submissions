class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     ## num[i] == target - num[j]
     # if we subtract the target by the first index then we get the value that the other one needs to be. We then need a way of seeing if that value we need is stored. Could create a hashmap with both the index and its value
     seen ={}
     result = []
     for i, num in enumerate(nums):
        num2 = target - num
        if num2 in seen:
            result.append(i)
            result.append(seen.get(num2))
            return sorted(result)
        else:
            seen[num]=i

        