"""
Approach 1:
Nested Loops

Problem: 867. Transpose Matrix

Difficulty: Easy

Time Complexity: O(r × c)
Space Complexity: O(r × c)

Pattern:
Matrix Traversal

Approach:

- Create an empty result list.
- Iterate through the columns of the original matrix.
- For each column, create an empty row.
- Iterate through all rows of the original matrix.
- Append matrix[c][r] to the current row.
- Add the completed row to result.
- Return result.

Loop Structure:

- Outer loop → original columns
- Inner loop → original rows

Example:

Original:
1 2 3
4 5 6

r = 0:
matrix[0][0] → 1
matrix[1][0] → 4
row = [1, 4]

r = 1:
matrix[0][1] → 2
matrix[1][1] → 5
row = [2, 5]

r = 2:
matrix[0][2] → 3
matrix[1][2] → 6
row = [3, 6]

Result:
[
    [1, 4],
    [2, 5],
    [3, 6]
]

Why it works:

- Each column of the original matrix becomes a row
  in the result.
- matrix[c][r] means:
  - c → original row
  - r → original column
- Therefore, the row/column positions are effectively swapped.

Common Mistakes:

- Using range(len(matrix)) for the outer loop.
  The outer loop must represent columns.
- Using range(len(matrix[0])) for the inner loop.
  The inner loop must represent rows.
- Confusing matrix[c][r] with matrix[r][c].
- Modifying the original matrix instead of creating a result matrix.
"""
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        for r in range(len(matrix[0])):
            row = []

            for c in range(len(matrix)):
                row.append(matrix[c][r])

            result.append(row)

        return result
    

"""
Approach 2:
List Comprehension

Problem: 867. Transpose Matrix

Difficulty: Easy

Time Complexity: O(r × c)
Space Complexity: O(r × c)

Pattern:
Matrix Traversal

Approach:

- Store the number of rows in n.
- Store the number of columns in m.
- Build the transposed matrix using nested list comprehensions.
- The outer loop iterates through the original columns.
- The inner loop iterates through the original rows.
- Access matrix[i][j] and place it conceptually at
  result[j][i].
- Return the transposed matrix.

Key Idea:

Original:
matrix[i][j]

Transpose:
result[j][i]

Loop Structure:

- Outer loop → columns
- Inner loop → rows

Example:

Original:
1 2 3
4 5 6

Transpose:
1 4
2 5
3 6

Why it works:

- Each original column becomes a row in the transposed matrix.
- matrix[i][j] is read by fixing the column j and
  traversing all rows i.
- The list comprehension directly constructs each new row.

Common Mistakes:

- Using range(n) for the outer loop instead of range(m).
- Using range(m) for the inner loop instead of range(n).
- Confusing matrix[i][j] with matrix[j][i].
- Trying to modify the original matrix directly, which can
  overwrite values before they are used.
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        return [[matrix[i][j] for i in range(n)] for j in range(m)]