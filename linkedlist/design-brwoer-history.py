# class Node:
#   def __init__(self,value="",next = None):
#     self.value = value
#     self.next = next

# class BrowserHistory(object):
#   def __init__(self,value):
#     node = Node(value)
#     # head 및 현재 url 위치, 리스트 크기  지정
#     self.head = node
#     self.current = node
#     self.size = 0
#     self.pos = 0
#     pass
  
#   def debug(self):
#     print("-----debug-----")
#     current = self.head
#     while(current.next):
#       print(current.value)
#       current = current.next
#     print(current.value)
  
#   def visit(self,url):
#     # 새로운 노드를 만들고, 링크드리스트 마지막에 노드를 추가(tail 기법)
#     node = Node(url)
#     self.current.next = node
#     self.current = self.current.next
    
#     if self.size > self.pos :
#       self.pos = self.pos
#       self.size = self.pos + 1
#     else:
#       self.size = self.size + 1
#       self.pos = self.pos + 1
#     return None
  
#   def back(self,steps):
#     # 현재 노드 크기에서 steps를 뺀만큼 접근, 접근한 노드를 현재 바라보고있는 노드로 변경
#     hCur = self.head
    
#     if steps > self.pos:
#       self.pos = 0
#       pass
#     else:
#       self.pos = self.pos - steps
      
#     for _ in range(self.pos):
#       hCur = hCur.next
#     self.current = hCur
#     print(self.current.value)
#     return self.current.value 
  
#   def forward(self,steps):
    
#     # 현재 노드 크기에서 steps를 더한만큼 접근, 접근한 노드를 현재 바라보고있는 노드로 변경
#     hCur = self.head
#     if steps > (self.size - self.pos):
#       self.pos = self.pos + (self.size - self.pos)
#       pass
#     else:
#       self.pos = self.pos + steps
   
#     for _ in range(self.pos):
#       hCur = hCur.next
#     self.current = hCur
#     print(self.current.value)
#     pass
  
  
#양방향 linked list
class ListNode(object):
  def __init__(self,val = 0, next = None,prev = None) -> None:
    self.val = val
    self.next = next
    self.prev = prev
    pass
  
class BrowserHistory(object):
  def __init__(self,homepage) -> None:
    node = ListNode(val=homepage)
    self.head = node
    self.current = node
    pass
  def visit(self,url):
    self.current.next = ListNode(val=url,prev=self.current)
    self.current = self.current.next
    return None
  def back(self,steps):
    # 이전 노드가 없을때 까지 반복
    while steps > 0 and self.current.prev != None:
      steps -= 1
      self.current = self.current.prev
    return self.current.val
  def forward(self,steps):
    # 다음 노드가 없을때 까지 반복 
    while steps > 0 and self.current.next != None:
      steps += 1
      self.current = self.current.next
    return self.current.val 
  
  
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)
# browserHistory.debug()
# 
# 
# browserHistory.forward(1)
# browserHistory.visit("linkedin.com")
# browserHistory.forward(2)
# browserHistory.back(2)
# browserHistory.back(7)