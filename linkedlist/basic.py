class Node:
  def __init__(self,value=0,next = None):
    self.value = value
    self.next = next


class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  def append(self,value):
    # 시간 복잡도 O(n)
    new_node = Node(value)
    if self.head is None:
      # 헤드가 지정이 안되어있을때만 신규 노드를 가리킨다(노드가 처음 들어올때)
      self.head = new_node
      
      # tail 추가
      self.tail = new_node
    else:
      # linked list는 헤드를 통해서 접근해야된다
      #current = self.head
      # 마지막 노드까지 간다
      #while(current.next):
        #current = current.next
      # 마지막 노드까지 오면 해당 노드에 next_node를 지정해준다
      #current.next = new_node
      
      # tail 버전 시간복잡도 - O(1)
      self.tail.next = new_node
      self.tail = self.tail.next
      pass
  def get(self,idx):
    # 시간 복잡도 O(n)
    # 헤드에 접근
    current = self.head
    # 인덱스만큼 접근
    for _ in range(idx):
      current = current.next
    return current.value
  def insert_at(self,idx,value):
    current = self.head
    new_node = Node(value)
    # 인덱스 까지 접근한다
    for _ in range(idx):
      current = current.next
    
    #새로 생성한 노드의 주소와 연결해준다
    new_node.next = current.next
    current.next = new_node
  def remove_at(self,idx):
    if idx == 0:
      self.head = self.head.next
    # 노드를 참조하는게 없다면 가비지 컬렉션이 자동으로 삭제처리해준다
    else:
      current = self.head
      for _ in range(idx-1):
        current = current.next
      current.next = current.next.next


# first = Node(1)
# second = Node(2)
# third = Node(3)
# first.next = second
# second.next = third
# first.value = 6
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)