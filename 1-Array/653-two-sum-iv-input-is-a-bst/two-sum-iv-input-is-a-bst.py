class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()  # To store values we've already visited
        
        def dfs(node):
            if not node:
                return False
            # Check if the complement (k - node.val) is already in the set
            if k - node.val in seen:
                return True
            # Add the current node's value to the set
            seen.add(node.val)
            # Continue DFS on both left and right subtrees
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
