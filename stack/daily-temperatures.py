from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      # print(temperatures)
      stack = []
      answer = []
      for i,daily in enumerate(temperatures):
        # print(daily)
        if len(stack) < 1:
          stack.append({'key':i,'value':daily})
        else:
          # if i < 3:
          while(True):
            if len(stack) < 1:
              break
              
            if stack[-1]['value'] < daily:
              answer.append(i - stack[-1]['key'])
              stack.pop()
              stack.append({'key':i,'value':daily})
            else:
              stack.append({'key':i,'value':daily})
              break
              # print(i - stack[-1]['key'])
        #   # print(stack[-1])
        #   while(True):
        #     count = 0
        #     if stack[-1] < daily:
        #       count += 1
        #       stack.pop()
        #       stack.append(daily)
        #       answer.append(count)
        #       break
        #     else:
        #       stack.append(daily)
        #       break
            
          # while(True):
          #   if stack[-1] < daily:
          #     stack.pop()
          #     break
          #   else:
          #     stack.append(daily)
          #     break
            
      print(stack)
      print(answer)
      pass
    

solution = Solution()
solution.dailyTemperatures([73,74,75,71,69,72,76,73])