"""
Approach 1:
Recursion / Depth-First Search (DFS)

Problem: 872. Leaf-Similar Trees

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Pattern:
Binary Tree + Recursion + List Collection

Approach:

- Create a helper function called traverse().
- The helper function traverses one binary tree recursively.
- Maintain a local list called arr to store leaf values.
- If the current node is None, return an empty list.
- A leaf node is a node whose:
  - left child is None
  - right child is None
- If the current node is a leaf, append its value to arr.
- Recursively traverse the left subtree.
- Recursively traverse the right subtree.
- Add the leaf values returned by both recursive calls
  to the current arr.
- Return arr after the entire subtree has been traversed.
- Generate the leaf sequence for both trees.
- Compare the two sequences.
- If both sequences are identical, return True.
- Otherwise, return False.

Key Insight:

- We only care about leaf nodes, not internal nodes.
- Recursion allows us to visit every node in the tree.
- Each recursive call returns the leaf values found
  in its subtree.
- The parent combines the results from its left and
  right subtrees.

Base Case:

- If root is None:
  return []

Leaf Condition:

- If root.left is None and root.right is None:
  append root.val

Example:

root1:

        3
       / \
      5   1
     / \ / \
    6  2 9  8

Leaf sequence:

[6, 2, 9, 8]

root2:

        3
       / \
      5   1
     / \ / \
    6  2 9  8

Leaf sequence:

[6, 2, 9, 8]

Comparison:

[6, 2, 9, 8] == [6, 2, 9, 8]

Final Result:

True

Code:

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:

        def traverse(root):
            arr = []

            if root is None:
                return arr

            if root.left is None and root.right is None:
                arr.append(root.val)

            arr += traverse(root.left)
            arr += traverse(root.right)

            return arr

        arr1 = traverse(root1)
        arr2 = traverse(root2)

        return arr1 == arr2

Note:

- traverse(root) solves the same problem for each subtree.
- arr stores the leaf values found in the current subtree.
- traverse(root.left) returns leaf values from the left subtree.
- traverse(root.right) returns leaf values from the right subtree.
- += combines the returned leaf values with arr.
- The leaves are collected from left to right.
- Therefore, the resulting list represents the leaf-value sequence.
- Both trees are traversed independently.
- Finally, their leaf sequences are compared.

Important Pattern:

"Collect information from subtrees"
↓
RECURSION
↓
Solve left subtree
↓
Solve right subtree
↓
Combine returned results
↓
Compare final results
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root):
            arr = []
            if root is None:
                return arr
            if root.left is None and root.right is None:
                arr.append(root.val)
            arr += traverse(root.left)
            arr += traverse(root.right)
            return arr
        arr1 = traverse(root1)
        arr2 = traverse(root2)
        return arr1 == arr2 
    
    
"""
Approach 2:
Recursion / Depth-First Search (DFS) + Shared State

Problem: 872. Leaf-Similar Trees

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Pattern:
Binary Tree + Recursion + Shared List

Approach:

- Create a list self.arr to store leaf values.
- Define a helper function called traverse().
- If the current node is None, stop the recursion.
- Check whether the current node is a leaf.
- If it is a leaf, append its value to self.arr.
- Recursively traverse the left subtree.
- Recursively traverse the right subtree.
- Because self.arr is shared by all recursive calls,
  every leaf value is added to the same list.
- Traverse the first tree and store its leaf sequence.
- Reset self.arr to an empty list.
- Traverse the second tree.
- Compare the two leaf sequences.
- Return True if they are identical.

Key Insight:

- Unlike the first approach, every recursive call does
  NOT create and return its own list.
- All recursive calls modify the same self.arr list.
- self.arr acts as shared state during the traversal.
- This avoids combining returned lists from each subtree.

Base Case:

- If root is None:
  return

Leaf Condition:

- If root.left is None and root.right is None:
  append root.val to self.arr

Example:

root1:

        3
       / \
      5   1
     / \ / \
    6  2 9  8

During traversal:

self.arr = []

Visit 6:
self.arr = [6]

Visit 2:
self.arr = [6, 2]

Visit 9:
self.arr = [6, 2, 9]

Visit 8:
self.arr = [6, 2, 9, 8]

First sequence:

arr1 = [6, 2, 9, 8]

Reset:

self.arr = []

Traverse root2.

Second sequence:

self.arr = [6, 2, 9, 8]

Comparison:

arr1 == self.arr

Final Result:

True

Code:

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:

        self.arr = []

        def traverse(root):
            if root is None:
                return

            if root.left is None and root.right is None:
                self.arr.append(root.val)

            traverse(root.left)
            traverse(root.right)

        traverse(root1)

        arr1 = self.arr

        self.arr = []

        traverse(root2)

        return arr1 == self.arr

Note:

- self.arr belongs to the Solution object.
- Every recursive call accesses the same self.arr.
- No list needs to be returned from traverse().
- The order of traversal is:
  left subtree → current leaf → right subtree.
- This produces the leaf sequence from left to right.
- self.arr must be reset before traversing root2.
- arr1 keeps the first tree's leaf sequence.
- The second traversal fills self.arr with root2's leaf sequence.
- Finally, both sequences are compared.

Important Pattern:

"Collect information from all nodes using shared state"
↓
CREATE SHARED LIST
↓
RECURSION
↓
Visit left subtree
↓
Process current node
↓
Visit right subtree
↓
MODIFY SHARED LIST
↓
Compare collected results
"""
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.arr = []
        def traverse(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                self.arr.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root1)
        arr1 = self.arr
        self.arr = []
        arr2 = traverse(root2)
        return arr1 == self.arr 