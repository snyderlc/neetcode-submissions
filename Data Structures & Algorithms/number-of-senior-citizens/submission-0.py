class Solution:
    def countSeniors(self, details: List[str]) -> int:
        elder_count = 0
        for word in details:
            age = int(word[11:13])
            if age > 60:
                elder_count+= 1
        return elder_count