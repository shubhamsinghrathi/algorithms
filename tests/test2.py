import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        ln = len(nums)
        if ln==0:
            return None
        return self.treeMaker(nums, 0, ln-1)
        
    def treeMaker(self, arr, sp, lp):
        print("sp: ", sp, "lp: ", lp)
        if sp >= lp:
            return TreeNode(arr[sp])
        mp = math.floor((lp-sp)/2)+sp
        
        leftNode = None
        if not mp==sp:
            leftNode = self.treeMaker(arr, sp, mp-1)
        rightNode = self.treeMaker(arr, mp+1, lp)
        tr = TreeNode(arr[mp])
        tr.left = leftNode
        tr.right = rightNode
        return tr

sl = Solution()
print(sl.sortedArrayToBST([-10,-3,0,5,9]))