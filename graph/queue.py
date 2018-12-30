class Queue:
    def __init__(self):
        self.queue = {
            "value": None,
            "parent": None,
            "child": None
        }
        self.len = 0
        self.start = self.queue
        self.end = self.queue

    def push(self, value):
        if self.len == 0:
            self.queue = {
                "value": value,
                "parent": None,
                "child": None
            }
            self.len = 1
            self.start = self.queue
            self.end = self.queue

        else:
            self.end["child"] = {
                "value": value,
                "parent": self.end,
                "child": None
            }
            self.end = self.end["child"]
            self.len = self.len + 1
        return value

    def pop(self):
        if self.len == 0:
            return None
        else:
            toReturn = self.start["value"]
            self.start = self.start["child"]
            if self.start != None:
                self.start["parent"] = None
            self.queue = self.start
            self.len = self.len - 1
            return toReturn

    def print(self):
        if self.len == 0:
            print(None)
            return
        else:
            self.printer(self.queue)
            return

    def printer(self, queue):
        print(queue["value"])
        if queue["child"] == None:
            return
        else:
            return self.printer(queue["child"])

# q = Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# q.print()
# print("")
# q.pop()
# q.pop()
# q.pop()
# q.pop()
# q.print()