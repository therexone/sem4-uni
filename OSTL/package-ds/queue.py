
from collections import deque


# #queue - FIFO
class queue:
    def __init__(self, size):
        self.size = size
        self.queue = deque([], size)

    def push_to_queue(self, element):
        self.queue.append(element) if (len(self.queue) !=
                                       self.size) else print('Queue Overflow.')

    def dequeue(self):
        try:
            return self.queue.popleft()
        except IndexError:
            print('Queue is empty, try pushing some elements to the queue.')

    def get_queue(self):
        return self.queue
