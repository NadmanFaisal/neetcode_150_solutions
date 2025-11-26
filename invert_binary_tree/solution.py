import collections
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1
    
    while i < len(values):
        current = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    q.append(node.left)
                    q.append(node.right)

        return root


if __name__ == "__main__":
    input_list = [4,2,7,1,3,6,9]
    root = build_tree(input_list)
    sol = Solution()
    print(sol.invertTree(root))
