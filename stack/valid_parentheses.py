class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for parentheses in s:
        stack.append(parentheses)
        if len(stack) >= 1:
          if parentheses == ")" and stack[len(stack)-2] == "(":
            stack.pop()
            stack.pop()
          if parentheses == "]" and stack[len(stack)-2] == "[":
            stack.pop()
            stack.pop()
          if parentheses == "}" and stack[len(stack)-2] == "{":
            stack.pop()
            stack.pop()

      if len(stack) == 0:
        return True
      else:
        return False
    
    
solution = Solution()
solution.isValid("(]")