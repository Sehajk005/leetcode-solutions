"""
Approach 1:
Brute Force + Remove Duplicates at the End

Problem: 2215. Find the Difference of Two Arrays

Difficulty: Easy

Time Complexity:
- O(n × m)
  (Each `not in` check on a list is O(m))

Space Complexity:
- O(n)

Pattern:
Brute Force

Approach:
- Traverse every element in `nums1`.
- If the current element is not present in `nums2`, append it to `res1`.
- Convert `res1` into a set to remove duplicates.
- Repeat the same process for `nums2` against `nums1`.
- Return both unique result lists.

Key Insight:
- Directly compare every element of one array with the other.
- Since duplicate elements may be collected multiple times, convert the result to a set before returning.
- This approach is simple but inefficient because list membership checking is linear.

Example:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

Traverse nums1:
1 -> present
2 -> present
3 -> absent -> res1 = [3]
3 -> absent -> res1 = [3,3]

Unique:
res1 = [3]

Traverse nums2:
1 -> present
1 -> present
2 -> present
2 -> present

res2 = []

Output:
[[3], []]

Note:
- Uses list membership (`not in`) repeatedly.
- Duplicate values are removed only at the end.
- Simple to understand but the slowest solution.
"""
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = []
        res1 = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                res1.append(nums1[i])
        output.append(list(set(res1)))
        res2= []
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                res2.append(nums2[i])
        output.append(list(set(res2)))
        return output
    
    
"""
Approach 2:
Hash Set Lookup

Problem: 2215. Find the Difference of Two Arrays

Difficulty: Easy

Time Complexity:
- O(n + m)

Space Complexity:
- O(n + m)

Pattern:
Hash Set

Approach:
- Convert both arrays into sets for O(1) average lookup.
- Traverse `nums1`.
- If an element is not present in `set2`, add it to `res1`.
- Traverse `nums2`.
- If an element is not present in `set1`, add it to `res2`.
- Remove duplicates from the results using `set()` before returning.

Key Insight:
- Using sets makes membership checking constant time on average.
- Although duplicates may still be added while traversing the original arrays, they are removed at the end.
- Faster than brute force due to efficient lookups.

Example:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

set1 = {1,2,3}
set2 = {1,2}

Traverse nums1:
1 -> present
2 -> present
3 -> absent -> res1 = [3]
3 -> absent -> res1 = [3,3]

Unique:
res1 = [3]

Traverse nums2:
1 -> present
1 -> present
2 -> present
2 -> present

Output:
[[3], []]

Note:
- Uses extra memory for hash sets.
- Membership testing becomes O(1) average.
- Still removes duplicates only at the end.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        res1 = []
        for num in nums1:
            if num not in set2:
                res1.append(num)

        res2 = []
        for num in nums2:
            if num not in set1:
                res2.append(num)

        return [list(set(res1)), list(set(res2))]


"""
Approach 3:
Hash Map (Frequency Dictionary)

Problem: 2215. Find the Difference of Two Arrays

Difficulty: Easy

Time Complexity:
- O(n + m)

Space Complexity:
- O(n + m)

Pattern:
Hash Map

Approach:
- Build a dictionary for every unique element in `nums1`.
- Build another dictionary for every unique element in `nums2`.
- Traverse keys of the first dictionary.
- If a key is absent in the second dictionary, add it to `res1`.
- Repeat for the second dictionary.
- Return both result lists.

Key Insight:
- Dictionaries automatically keep only unique keys.
- No additional duplicate removal is required.
- Similar efficiency to using sets because dictionary lookup is O(1) average.

Example:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

freq1 = {1:1, 2:1, 3:1}
freq2 = {1:1, 2:1}

Compare keys:
3 not in freq2 -> res1 = [3]

Compare second dictionary:
No unique elements

Output:
[[3], []]

Note:
- Stores only unique values as dictionary keys.
- Duplicate removal happens naturally while building the dictionary.
- Useful when frequencies may be needed in related problems.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq1 = {}
        for num in nums1:
            freq1[num] = 1
        freq2 = {}
        for num in nums2:
            freq2[num] = 1
        res1 = []
        for num in freq1:
            if num not in freq2:
                res1.append(num)
        res2 = []
        for num in freq2:
            if num not in freq1:
                res2.append(num)
        return [res1, res2]
    
    
"""
Approach 4:
Set Difference (Optimal)

Problem: 2215. Find the Difference of Two Arrays

Difficulty: Easy

Time Complexity:
- O(n + m)

Space Complexity:
- O(n + m)

Pattern:
Hash Set

Approach:
- Convert both arrays into sets.
- Compute `set1 - set2` to obtain elements only present in `nums1`.
- Compute `set2 - set1` to obtain elements only present in `nums2`.
- Convert both results to lists and return.

Key Insight:
- Python's set difference operator directly computes unique elements present in one set but not the other.
- Duplicate elements are automatically removed during set creation.
- This is the shortest, cleanest, and most Pythonic solution.

Example:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

set1 = {1,2,3}
set2 = {1,2}

set1 - set2 = {3}
set2 - set1 = {}

Output:
[[3], []]

Note:
- No explicit loops are needed for comparison.
- No duplicate removal step is required.
- This is the optimal and most concise solution.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [
            list(set1-set2),
            list(set2-set1)
        ]
