from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      stack = []
      answer = []
      for i,daily in enumerate(temperatures):
        answer.append(0)
        while stack and stack[-1][1] < daily:
          day,value = stack.pop()
          answer[day] = i - day
        stack.append((i,daily))
        
      return answer
        
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))