class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #iterate through each char in a list of strings
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res