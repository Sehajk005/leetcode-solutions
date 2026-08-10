"""
Optimal Approach:
Recursion / Depth-First Search (DFS)

Problem: 104. Maximum Depth of Binary Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Pattern:
Binary Tree + Recursion

Approach:

* Start from the root of the binary tree.
* If the current node is None, return 0 because
  there are no nodes in an empty tree.
* Recursively calculate the maximum depth of the
  left subtree.
* Recursively calculate the maximum depth of the
  right subtree.
* Take the maximum of the left and right subtree depths.
* Add 1 to include the current node.
* Return the result.

Key Insight:

* Every node can be treated as the root of its own subtree.
* To find the depth of the current node, we need the
  maximum depth of its left and right subtrees.
* The deeper subtree determines the maximum depth.
* The current node contributes +1 to the depth.
* Recursion naturally solves the same problem for
  smaller subtrees.

Formula:

depth(node) = max(left_depth, right_depth) + 1

Base Case:

* If node is None:
  return 0

Example:

root = [3,9,20,null,null,15,7]

Tree:

```
    3
   / \
  9   20
     /  \
    15   7
```

Process:

At node 9:

left  → None → 0
right → None → 0

depth(9) = max(0, 0) + 1
= 1

At node 15:

left  → None → 0
right → None → 0

depth(15) = 1

At node 7:

left  → None → 0
right → None → 0

depth(7) = 1

At node 20:

left  → 1
right → 1

depth(20) = max(1, 1) + 1
= 2

At node 3:

left  → 1
right → 2

depth(3) = max(1, 2) + 1
= 3

Final Result:
3

Code:

class Solution:
def maxDepth(self, root: Optional[TreeNode]) -> int:
if root is None:
return 0

```
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(left, right) + 1
```

Note:

* root.left gives the left child of the current node.
* root.right gives the right child of the current node.
* self.maxDepth() recursively calculates the depth
  of a subtree.
* The base case prevents recursion from continuing
  when there is no node.
* max(left, right) selects the deeper subtree.
* +1 accounts for the current node.
* Every node is visited exactly once.
* Therefore, time complexity is O(n).
* The recursion stack depends on the height of the tree,
  so space complexity is O(h).

Important Pattern:

"Find the maximum/minimum value from subtrees"
↓
RECURSION
↓
Solve left subtree
↓
Solve right subtree
↓
Combine both answers
↓
Account for current node
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1