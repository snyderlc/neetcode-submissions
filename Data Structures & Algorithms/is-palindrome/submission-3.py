class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_txt=''.join(filter(str.isalnum,s)).lower()
        print(clean_txt)
        left = 0
        right = len(clean_txt) - 1
        while (left <= right):
            if clean_txt[left]!=clean_txt[right]:
                return False
            else:
                left +=1
                right -=1
        return True
