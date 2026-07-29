"""
Approach:
Frequency Counting

Problem: 645. Set Mismatch

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
Counting / Frequency Array

Approach:
- Create a frequency array of size (n + 1).
- Traverse the input array and increment the frequency of each number.
- Traverse numbers from 1 to n:
    - If frequency is 2, it is the duplicate number.
    - If frequency is 0, it is the missing number.
- Return [duplicate, missing].

Key Insight:
- Every number from 1 to n should appear exactly once.
- The frequency array directly tells:
    - Frequency = 2 → Duplicate
    - Frequency = 0 → Missing

Example:
nums = [1, 2, 2, 4]

Frequency Array:

Index : 0 1 2 3 4
Count : 0 1 2 0 1

Traverse 1 → count = 1
Traverse 2 → count = 2 → duplicate = 2
Traverse 3 → count = 0 → missing = 3
Traverse 4 → count = 1

Answer = [2, 3]

Note:
- Very easy to understand and implement.
- Requires an extra frequency array of size O(n).
- Suitable when extra space is allowed.
"""
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1

        duplicate = 0
        misssing = 0

        for num in range(1, n + 1):
            if count[num] == 2:
                duplicate = num
            elif count[num] == 0:
                missing = num

        return [duplicate, missing]


"""
Approach:
Negative Marking (In-place Hashing)

Problem: 645. Set Mismatch

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Array as Hash Table / Index Marking

Approach:
- Since every number lies between 1 and n, use each value as an index.
- For every number:
    - Compute index = abs(num) - 1.
    - If nums[index] is already negative:
        - The current number is the duplicate.
    - Otherwise:
        - Negate nums[index] to mark that the number has been seen.
- After the first traversal, iterate through the array:
    - The index whose value is still positive corresponds to the missing number.
- Return [duplicate, missing].

Key Insight:
- The sign of each element acts as a visited marker.
- Negative → Number already seen.
- Positive → Number never visited.

Example:
nums = [1, 2, 2, 4]

Initial:
[1, 2, 2, 4]

Read 1
→ Mark index 0
[-1, 2, 2, 4]

Read 2
→ Mark index 1
[-1, -2, 2, 4]

Read 2
→ Index 1 already negative
→ duplicate = 2

Read 4
→ Mark index 3
[-1, -2, 2, -4]

Second Pass:

Index 0 → Negative
Index 1 → Negative
Index 2 → Positive → missing = 3
Index 3 → Negative

Answer = [2, 3]

Why abs()?
- Elements are turned negative during marking.
- abs(num) retrieves the original value before converting it to an index.
- Without abs(), a negative value would produce an incorrect index.

Note:
- Uses the input array itself as a hash table.
- No extra array is required.
- One of the most common interview techniques for arrays containing
  values in the range [1, n].
- Modifies the input array.
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                duplicate = abs(num)
            else:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]