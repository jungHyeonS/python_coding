class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    res = []
    for i in range(0,len(nums)-1):
      for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
          res.append(i)
          res.append(j)
      
    return res

    


if __name__ == '__main__':
  solution = Solution()
  solution.twoSum([3,2,4],6)