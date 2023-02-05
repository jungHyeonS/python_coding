from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      stack = []
      answer = [0] * len(temperatures)
      for curDay,curValue in enumerate(temperatures):
        while stack and stack[-1][1] < curValue:
          prevDay,_ = stack.pop()
          answer[prevDay] = curDay - prevDay
        stack.append((curDay,curValue))
      
      return answer
    
    
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))