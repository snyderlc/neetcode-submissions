class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCheck = {}
        for i in nums:
            if i in dupCheck:
                return True
            else:
                dupCheck[i] = 0
        return False
