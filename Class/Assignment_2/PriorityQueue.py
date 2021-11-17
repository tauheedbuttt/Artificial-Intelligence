# Priority Queue class taken from https://www.geeksforgeeks.org/priority-queue-in-python/
# to make the assignment faster

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i].hn == self.queue[max].hn:
                    if self.queue[i].data > self.queue[max].data and len(self.queue[i].data)==1 and len(self.queue[max].data)==1:
                        max = i
                if self.queue[i].hn < self.queue[max].hn:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()