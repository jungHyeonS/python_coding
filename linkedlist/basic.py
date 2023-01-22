class Node:
  def __init__(self,value=0,next = None):
    self.value = value
    self.next = next


class LinkedList(object):
  def __init__(self):
    self.head = None
  def append(self,value):
    new_node = Node(value)
    if self.head is None:
      # 헤드가 지정이 안되어있을때만 신규 노드를 가리킨다(노드가 처음 들어올때)
      self.head = new_node
    else:
      # linked list는 헤드를 통해서 접근해야된다
      current = self.head
      # 마지막 노드까지 간다
      while(current.next):
        current = current.next
      # 마지막 노드까지 오면 해당 노드에 next_node를 지정해준다
      current.next = new_node
      pass


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