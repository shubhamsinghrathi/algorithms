class BLL:
    def __init__(self, data, parent=None):
        self.back = parent
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.queue = None
        self.last = None

    def push(self, data):
        crr = self.queue
        if not self.queue:
            self.queue = BLL(data)
            self.last = self.queue
            return
        self.queue = BLL(data)
        self.queue.next = crr
        crr.back = self.queue
        return

    def pop(self):
        if not self.queue:
            return None
        last = self.last
        try:
            self.last = self.last.back
            self.last.next = None
        except:
            self.last = None
            self.queue = None
        return last.data