'''
This algorithm is the fastest algorithm to search any string
'''

class Trie:
    def __init__(self):
        self.tree = None

    def insert(self, word):
        if self.tree == None:
            self.tree = {
                "keys": [ word[0] ],
                "next": [ { "keys": [], "next": [], "ground": False } ],
                "ground": False
            }
        current = self.tree
        ln = len(word)
        i = 0
        for l in word:
            isLast = True
            if i < ln-1:
                isLast = False
            i+=1
            current = self.letterByLetter(l, current, isLast)
        # print("self.tree: ", self.tree)

    def letterByLetter(self, letter, current, isLast):
        try:
            indx = current["keys"].index(letter)
            if isLast:
                current["next"][indx]["ground"] = True
            return current["next"][indx]
        except:
            current["keys"].append(letter)
            ground = False
            if isLast == True:
                ground = True
            current["next"].append({ "keys": [], "next": [], "ground": ground })
            return current["next"][-1]

    def findWord(self, word):
        ln = len(word)
        i = 0
        current = self.tree
        if current == None:
            return False
        for l in word:
            isLast = True
            if i < ln-1:
                isLast = False
            i+=1
            try:
                indx = current["keys"].index(l)
                if isLast:
                    if current["next"][indx]["ground"] == True:
                        return True
                    else:
                        return False
                else:
                    current = current["next"][indx]
            except:
                return False
    
    def deleteWord(self, word):
        node = self.tree
        self.wordFound = True
        self.wordDeleted = False
        if node == None:
            return False
        res = self.deleter(node, word, 0, len(word))
        if self.wordFound == False:
            return "word not found"
        if self.wordDeleted == True:
            return "word deleted successfully"
        if res["ln"] == 0 or res["ln"] == 1:
            del current["next"][indx]
            del current["keys"][indx]
            return "word deleted successfully"
        else:
            del current["next"][indx]["next"][res["indx"]]
            del current["next"][indx]["keys"][res["indx"]]
            return "word deleted successfully"

    def deleter(self, current, word, i, ln):
        if i == ln-1:
            if len(current["keys"]) == 0:
                return { "doAction": True, "ln": 0, "indx": 0 }
            else:
                current["ground"] = False
                self.wordDeleted = True
                return { "doAction": False }
        indx = 0
        try:
            indx = current["keys"].index(word[i])
        except:
            self.wordFound = False
            return { "doAction": False }
        res = self.deleter(current["next"][indx], word, i+1, ln)
        if self.wordFound == False or self.wordDeleted == True:
            return { "doAction": False }
        if res["doAction"] == False:
            return { "doAction": False }
        if res["ln"] == 0 or res["ln"] == 1:
            del current["next"][indx]
            del current["keys"][indx]
            return { "doAction": True, "ln": len(current["keys"]), "indx": indx }
        else:
            del current["next"][indx]["next"][res["indx"]]
            del current["next"][indx]["keys"][res["indx"]]
            self.wordDeleted = True
            return { "doAction": False }

strTree = Trie()
strTree.insert("Hello")
strTree.insert("Bold")

print("tree: ", strTree.tree)
print(strTree.deleteWord("Bold"))
print("tree: ", strTree.tree)

# print(strTree.findWord('Hello'))