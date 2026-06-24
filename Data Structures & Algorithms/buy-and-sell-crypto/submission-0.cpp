class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int difference =0;
      for (int i=0; i<prices.size(); i++){
        for (int j=i+1; j<prices.size();j++){
          if (prices[j]-prices[i] > difference){
            difference = prices[j]-prices[i];
          }
        }
      }
      if (difference < 0){
        return 0;
      }
      return difference;
    }
};
// need to obtain the smallest number with the furthest left position first
// obtain the largest number that is the furthest right of the smallest number
// If the smallest number is at the end of the vector, output 0
// largest_num - smallest_num = profit
// really just need to find which number has the biggest difference