class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain_dup = {}
        for n in nums:
            if n in contain_dup:
                return True
            else:
                contain_dup[n] = 1
        return False