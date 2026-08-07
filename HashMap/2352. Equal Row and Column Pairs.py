"""
Approach 1:
Brute Force Row vs Column Comparison

Problem: 2352. Equal Row and Column Pairs

Difficulty: Medium

Time Complexity:

- O(n³)

Space Complexity:

- O(n)

Pattern:
Matrix Traversal

Approach:

- Initialize count = 0.
- Traverse every row in the matrix.
- For each row, traverse every column.
- Build the current column manually by visiting every row.
- Compare the current row with the constructed column.
- If they are equal, increment the count.
- Return the final count.

Key Insight:

- Every row must be compared with every column.
- Since columns are not stored directly, each column is reconstructed every time.
- Building one column takes O(n), and there are n² row-column comparisons.

Example:

grid =
[
 [3,2,1],
 [1,7,6],
 [2,7,7]
]

Comparisons:

Row 0 = [3,2,1]
Column 0 = [3,1,2] ❌
Column 1 = [2,7,7] ❌
Column 2 = [1,6,7] ❌

Row 1 = [1,7,6]
Column 0 = [3,1,2] ❌
Column 1 = [2,7,7] ❌
Column 2 = [1,6,7] ❌

Row 2 = [2,7,7]
Column 0 = [3,1,2] ❌
Column 1 = [2,7,7] ✅
Column 2 = [1,6,7] ❌

Output:
1

Note:

- Simplest and most intuitive solution.
- Easy to understand but inefficient.
- Rebuilds every column repeatedly, causing O(n³) time.
"""
from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                column = []
                for row in range(len(grid)):
                    column.append(grid[row][c])
                if grid[r] == column:
                    count+=1
        return count
    
    
"""
Approach 2:
Hash Map of Columns

Problem: 2352. Equal Row and Column Pairs

Difficulty: Medium

Time Complexity:

- O(n²)

Space Complexity:

- O(n²)

Pattern:
Hash Map + Matrix

Approach:

- Create an empty dictionary to store the frequency of every column.
- Traverse every column in the matrix.
- Build each column as a list.
- Convert the column into a tuple so it can be used as a dictionary key.
- Store the frequency of each column.
- Traverse every row.
- Convert the row into a tuple.
- If the row exists in the dictionary, add its frequency to the answer.
- Return the final count.

Key Insight:

- Instead of rebuilding and comparing every column repeatedly, preprocess all columns once.
- A tuple is immutable and hashable, allowing it to be used as a dictionary key.
- If multiple identical columns exist, their frequency is stored only once.
- Every matching row simply adds the number of identical columns.

Example:

grid =
[
 [3,2,1],
 [1,7,6],
 [2,7,7]
]

Column Frequency Map:

(3,1,2) → 1
(2,7,7) → 1
(1,6,7) → 1

Row Checks:

(3,2,1) → Not Found
(1,7,6) → Not Found
(2,7,7) → Found → count += 1

Output:
1

Note:

- Much faster than brute force.
- Each column is built only once.
- Uses extra memory to achieve O(n²) time.
- Converting rows and columns into tuples enables efficient dictionary lookups.
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = {}
        count = 0
        for c in range(len(grid[0])):
            column = []
            for r in range(len(grid)):
                column.append(grid[r][c])
            tuple_col = tuple(column)
            freq[tuple_col] = freq.get(tuple_col, 0) + 1
        for row in grid:
            tuple_row = tuple(row)
            if tuple_row in freq:
                count += freq[tuple_row]
                
        return count