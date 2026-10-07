class Solution:
    def isValid(self, s: str) -> bool:
       #LIFO - stack
       if len(s) % 2 == 1:
        return False
       stack = []
       for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
                print (stack)
            elif char == ']' and stack and stack.pop() == '[' :
                continue
            elif char == '}' and stack and stack.pop() == '{' :
                continue
            elif char == ')' and stack and stack.pop() == '(':
                continue
            else:
                return False
       if stack:
            return False
       return True

         

            

                
        