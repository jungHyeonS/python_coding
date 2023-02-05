# 시간복잡도를 줄이기 위해 메모리를 사용한다
# 딕셔너리에 in 은 O(1) 의 시간복잡도를 가진다
def two_sum(nums,target):
  memo = {}
  for v in nums:
    memo[v] = 1
    
  for v in nums:
    n = target - v
    if n in memo:
      return True

  return False
