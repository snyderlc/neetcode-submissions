class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2  # Find the middle integer index
            
            if nums[mid] == target:
                return mid  # Target found!
            elif nums[mid] > target:
                high = mid - 1  # Eliminate the right half
            else:
                low = mid + 1   # Eliminate the left half
                
        return -1  # Target does not exist in the array

