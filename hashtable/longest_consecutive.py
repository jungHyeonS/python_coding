from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      memo = {}
      for num in nums:
        if num in memo:
          pass
        else:
          memo[num] = num
      target = 0
      max = 0
      for num in nums:
        target = memo[num]
        len = 1
        while(True):
          if memo[num] == 0:
            target += 1
          else:
            target += memo[num]
          if target in memo:
            len += 1
          else:
            if len > max:
              max = len
            break
      return max

solution = Solution()
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))