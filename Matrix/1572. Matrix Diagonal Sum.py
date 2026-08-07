"""
Approach 1:
Brute Force (Check Every Cell)

Problem: 1572. Matrix Diagonal Sum

Difficulty: Easy

Time Complexity: O(n²)
Space Complexity: O(1)

Pattern:
Matrix Traversal

Approach:

- Traverse every cell in the matrix using two nested loops.
- For each cell:
    - If row index equals column index (r == c),
      it belongs to the primary diagonal.
    - If row index + column index equals n - 1
      (r + c == n - 1), it belongs to the secondary diagonal.
- Add the value to the total if either condition is true.
- Return the final sum.

Diagonal Conditions:

Primary Diagonal:
r == c

Secondary Diagonal:
r + c == n - 1

Why it works:

- Every element of the matrix is visited exactly once.
- The OR condition ensures the center element (in odd-sized
  matrices) is counted only once, even though it belongs
  to both diagonals.

Common Mistakes:

- Using two separate if statements instead of one OR condition,
  causing the center element to be counted twice.
- Using len(mat[0]) instead of len(mat)-1 for the secondary
  diagonal condition.
- Forgetting that this approach checks all n² cells even though
  only diagonal elements are needed.
"""
from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if r==c or r+c==len(mat)-1:
                    total += mat[r][c]
        return total


"""
Approach 2:
Diagonal Traversal (Optimal)

Problem: 1572. Matrix Diagonal Sum

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Matrix Traversal

Approach:

- Let n be the size of the matrix.
- Traverse only once from i = 0 to n - 1.
- In each iteration:
    - Add mat[i][i] (primary diagonal).
    - Add mat[i][n - 1 - i] (secondary diagonal).
- If n is odd:
    - Subtract the center element once because it was
      added twice.
- Return the total.

Diagonal Positions:

Primary Diagonal:
(i, i)

Secondary Diagonal:
(i, n - 1 - i)

Center Element (Odd n):
(n // 2, n // 2)

Why it works:

- Every row contributes exactly one element from each diagonal.
- Only diagonal elements are visited instead of every cell.
- The center element is the only overlapping element in an
  odd-sized matrix, so subtracting it once gives the correct sum.

Common Mistakes:

- Forgetting to subtract the center element for odd-sized matrices.
- Using n / 2 instead of n // 2 for the center index.
- Using n - i instead of n - 1 - i for the secondary diagonal.
- Traversing the entire matrix instead of only the diagonal positions.
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n-1-i]
        if n%2==1:
            total -= mat[n//2][n//2]
        return total
