class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for item in range(len(nums)):
            for check in range(item +1, len(nums)):
                if nums[item] == nums[check]:
                    return True
        return False