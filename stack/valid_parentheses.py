class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for parentheses in s:
        if len(stack) >= 1:
          if parentheses == ")" and stack[len(stack)-1] == "(":
            stack.pop()
          elif parentheses == "]" and stack[len(stack)-1] == "[":
            stack.pop()
          elif parentheses == "}" and stack[len(stack)-1] == "{":
            stack.pop()
          else:
            stack.append(parentheses)
        else:
          stack.append(parentheses)
        
      if len(stack) == 0:
        return True
      else:
        return False
    
    
solution = Solution()
print(solution.isValid("(]"))