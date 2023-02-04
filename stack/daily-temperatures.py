from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      stack = []
      answer = []
      for i,daily in enumerate(temperatures):
        answer.append(0)
        while(True):
          if len(stack) >= 1:
            if stack[-1]['value'] < daily:
              answer[stack[-1]['key']] = i - stack[-1]['key']
              stack.pop()
            else:
              stack.append({'key':i,'value':daily})
              break
          else:
            stack.append({'key':i,'value':daily})
            break
      return answer
    

solution = Solution()
# solution.dailyTemperatures([73,74,75,71,69,72,76,73])
print(solution.dailyTemperatures([30,60,90]))
