class Queue:
    def __init__(self):
        self.antrian = []

    def Enqueue(self, data):
        self.antrian.append(data)

    def Dequeue(self):
        if not self.IsEmpty():
            return self.antrian.pop(0)
        return None

    def IsEmpty(self):
        return len(self.antrian) == 0