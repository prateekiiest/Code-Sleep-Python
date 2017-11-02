class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

##test
def test():
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    q.show()
    q.dequeue()
    q.show()
#test()
