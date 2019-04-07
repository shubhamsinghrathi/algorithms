class TrieStr:
    def __init__(self):
        self.branch = {}
        self.result = False
        self.resultsBelow = 0

class Trie:
    def __init__(self):
        self.entries = 0
        self.db = TrieStr()

    def insertData(self, value):
        if value == "":
            return
        pointer = self.db
        for i in value:
            pointer.resultsBelow+=1
            try:
                pointer.branch[i]
            except:
                pointer.branch[i] = TrieStr()
            pointer = pointer.branch[i]
        pointer.resultsBelow+=1
        pointer.result = True
        return

    def findData(self, value):
        if value == "":
            return 0
        pointer = self.db
        found = True
        for i in value:
            try:
                pointer = pointer.branch[i]
            except:
                found = False
                break
        if found == False:
            return 0
        return pointer.resultsBelow

tr = Trie()
tr.insertData('hack')
# tr.insertData('hac1')
# tr.insertData('hac2')
# tr.insertData('hack1')
tr.insertData('hackerrank')
print(tr.findData('hac'))
print(tr.findData('hak'))