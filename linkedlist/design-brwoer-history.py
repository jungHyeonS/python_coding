class Node:
  def __init__(self,value="",next = None):
    self.value = value
    self.next = next

class BrowserHistory(object):
  def __init__(self,value):
    node = Node(value)
    # head 및 현재 url 위치, 리스트 크기  지정
    self.head = node
    self.current = node
    self.size = 0
    pass
  
  def visit(self,url):
    # 새로운 노드를 만들고, 링크드리스트 마지막에 노드를 추가(tail 기법)
    node = Node(url)
    self.current.next = node
    self.current = self.current.next
    self.size = self.size + 1
    pass
  
  def back(self,steps):
    # 현재 노드 크기에서 steps를 뺀만큼 접근, 접근한 노드를 현재 바라보고있는 노드로 변경
    hCur = self.head
    self.size = self.size - steps
    for _ in range(self.size):
      hCur = hCur.next
    self.current = hCur
    print(self.current.value)
    return self.current.value 
  
  def forward(self,steps):
    # 현재 노드 크기에서 steps를 더한만큼 접근, 접근한 노드를 현재 바라보고있는 노드로 변경
    hCur = self.head
    self.size = self.size + steps
    for _ in range(self.size):
      hCur = hCur.next
    self.current = hCur
    print(self.current.value)
    pass
  
  
  
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)