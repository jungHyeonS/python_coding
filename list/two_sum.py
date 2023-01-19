class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    start = 0
    end = len(nums) - 1
    res = []
    while(True):
      sum = nums[start] + nums[end]
      print(sum)
      if sum == target:
        res.append(start)
        res.append(end)
        break

      if sum > target:
        end = end - 1
      
      if sum < target:
        start = start + 1

    res.sort()
    return res

    # res = []
    # for i in range(0,len(nums)-1):
    #   for j in range(i+1,len(nums)):
    #     if nums[i] + nums[j] == target:
    #       res.append(i)
    #       res.append(j)
      
    # return res

    


if __name__ == '__main__':
  solution = Solution()
  solution.twoSum([-1,-2,-3,-4,-5],-8)