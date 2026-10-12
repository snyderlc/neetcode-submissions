class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while (lower <= upper):
            middle = (lower + upper) // 2
            if target < nums[middle]:
                upper = middle -1
            elif  target > nums[middle]:
                lower = middle + 1
            elif target == nums[middle]:
                return middle
        return -1
            