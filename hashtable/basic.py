# key 값을 유일하다
score = {
  'math': 97,
  'eng':90,
  'kor': 76
}
# 딕셔너리 접근
print(score['math'])

# 딕셔너리 수정
score['math'] = 100
print(score['math'])

# 딕셔너리 추가
score['sci'] = 45
print(score)

# score['music']

# print('music' in score)

# 딕셔너리에 'muic' 이라는 key가 있는지 없는지 체크 O(1)
if 'music' in score:
  print(score['music'])
else:
  score['music'] = 15
  
