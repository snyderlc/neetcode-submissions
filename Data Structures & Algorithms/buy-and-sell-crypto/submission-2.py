class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to find smallest num and biggest num to the right of small num
        left = 0
        right = 1
        MaxP = 0
        for right in range(len(prices)):
            print(left,right)
            if prices[left] > prices[right]:
                left = right
            if prices[right] - prices[left] > MaxP:
                MaxP = prices[right] - prices[left]
            right+=1
        return MaxP

            


                    

            
