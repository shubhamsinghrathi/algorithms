def quickSortAsc(arr):
    tree = treeCreator(arr)
    # print("tree: ", tree)
    sortedArr = depthFirstSearch(tree)
    print("sortedArr: ", sortedArr)

def treeCreator(arr):
    length = len(arr)
    tree = {
        "data": arr[-1],
        "left": None,
        "right": None
    }
    if length == -1:
        return tree
    leftArr = []
    rightArr = []
    lastElement = arr[-1]
    for i in range(length-1):
        if arr[i] > lastElement:
            rightArr.append(arr[i])
        else:
            leftArr.append(arr[i])

    if(len(leftArr)>0):
        tree["left"] = treeCreator(leftArr)
    if(len(rightArr)>0):
        tree["right"] = treeCreator(rightArr)
    return tree

stArr = []
def depthFirstSearch(tree):
    if tree["left"] != None:
        depthFirstSearch(tree["left"])
    stArr.append(tree["data"])
    if tree["right"] != None:
        depthFirstSearch(tree["right"])
    return stArr

quickSortAsc([5,9,10,1,3,8])

'''
QuickSort is based on divide and conquer strategy
'''