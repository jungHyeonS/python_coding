from collections import deque

#양방향으로 enqueue,dequeue 를 할수있다
queue = deque()
# enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# dequeue() O(1)
queue.popleft()
queue.popleft()
queue.popleft()