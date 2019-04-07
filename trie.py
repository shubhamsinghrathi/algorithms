class TrieStr:
    def __init__(self):
        self.keys = []
        self.branch = {}
        self.result = False

class Trie:
    def __init__(self):
        self.entries = 0
        self.db = TrieStr()

    def insertData(self, value):
        if value == "":
            return
        pointer = self.db
        # print("value: ", value)
        for i in value:
            try:
                pointer.branch[i]
            except:
                pointer.keys.append(i)
                # print("pointer.keys: ", pointer.keys)
                pointer.branch[i] = TrieStr()
            pointer = pointer.branch[i]
        pointer.result = True
        return

    def findings(self, pointer, res=0):
        if pointer.result == True:
            res+=1
        for ele in pointer.keys:
            res = self.findings(pointer.branch[ele], res)
        return res

    def findData(self, value):
        if value == "":
            return 0
        pointer = self.db
        found = True
        for i in value:
            try:
                pointer = pointer.branch[i]
                # print("pointer.keys: ", pointer.keys)
            except:
                found = False
                break
        if found == False:
            return 0
        return self.findings(pointer)

tr = Trie()
tr.insertData('hack')
# tr.insertData('hac1')
# tr.insertData('hac2')
# tr.insertData('hack1')
tr.insertData('hackerrank')
print(tr.findData('hac'))
print(tr.findData('hak'))