class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    start = 0
    end = len(nums) - 1
    res = []
    while(True):
      sum = nums[start] + nums[end]
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


if __name__ == '__main__':
  solution = Solution()
  solution.twoSum([3,2,4],6)