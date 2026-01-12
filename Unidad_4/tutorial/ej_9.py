from collections import deque
deq = deque()
for i in range(1, 4):
    deq.append(i)
deq.popleft()
print(deq)