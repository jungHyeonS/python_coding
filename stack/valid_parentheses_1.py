class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for p in s:
        # stack.append(p)
        # print(p)
        if len(stack) >= 1:
          if p == ")" and stack[len(stack)-1] == "(":
            stack.pop()
          elif p == "]" and stack[len(stack)-1] == "[":
            stack.pop()
          elif p == "}" and stack[len(stack)-1] == "{":
            stack.pop()
        else:
          stack.append(p)
          
      if len(stack) == 0:
        print(True)
      else:
        print(False)
      pass
    


solution = Solution()
solution.isValid("()[]{}")