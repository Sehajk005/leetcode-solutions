"""
Approach:
Brute Force (Nested Loops + Used Array)

Problem: 1679. Max Number of K-Sum Pairs

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Pattern:
Brute Force / Visited Array

Approach:
- Create a boolean array `used` of size `n` to track which elements have
  already been paired.
- Iterate through each element using index `i`.
- If `nums[i]` has already been used, skip it.
- For each unused `nums[i]`, check every subsequent element `nums[j]`
  where `j > i`.
- Skip `nums[j]` if it has already been used.
- If `nums[i] + nums[j] == k`:
    - Mark both indices as used.
    - Increment the operation count.
    - Break the inner loop since `nums[i]` can only be used once.
- Return the total number of valid operations.

Why use a `used` array?
- Prevents reusing the same element in multiple pairs.
- Avoids modifying the input array while iterating.
- Handles duplicate values correctly because indices are tracked
  instead of values.
"""
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        used = [False]*len(nums)
        for i in range(len(nums)):
            if used[i]:
                continue
            for j in range(i+1, len(nums)):
                if used[j]:
                    continue
                if nums[i] + nums[j] == k:
                    used[i] = True
                    used[j] = True
                    count += 1
                    break
        return count


"""
Approach:
Two Pointers (After Sorting)

Problem: 1679. Max Number of K-Sum Pairs

Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(1)

Pattern:
Sorting + Two Pointers

Approach:
- Sort the array in non-decreasing order.
- Initialize two pointers:
    - `left` at the beginning of the array.
    - `right` at the end of the array.
- While `left < right`:
    - Compute the sum of `nums[left] + nums[right]`.
    - If the sum equals `k`:
        - A valid pair is found.
        - Increment the operation count.
        - Move both pointers inward since both elements are used.
    - If the sum is greater than `k`:
        - Move `right` left to decrease the sum.
    - If the sum is less than `k`:
        - Move `left` right to increase the sum.
- Return the total number of valid operations.

Why sort the array?
- Sorting arranges the numbers in ascending order.
- This makes pointer movement meaningful:
    - Moving `left` right always increases the sum.
    - Moving `right` left always decreases the sum.
- Without sorting, there is no way to decide which pointer to move,
  making the two-pointer technique invalid.

Why move both pointers after finding a pair?
- Each element can be used in at most one operation.
- Once a valid pair is formed, both elements are consumed and cannot
  participate in another pair.

Why move only one pointer otherwise?
- If the current sum is too large, decreasing the larger number
  (moving `right`) is the only way to reduce the sum.
- If the current sum is too small, increasing the smaller number
  (moving `left`) is the only way to increase the sum.
- Because the array is sorted, these moves never skip a possible pair.
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left]+nums[right] == k:
                count += 1
                left+=1
                right-=1
            elif nums[left]+nums[right] > k:
                right -= 1
            else:
                left += 1
        return count


"""
Approach:
Hash Map (Frequency Counting)

Problem: 1679. Max Number of K-Sum Pairs

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
Hash Map / Frequency Counting

Approach:
- Initialize an empty hash map `freq` to store the frequency of
  unmatched numbers.
- Traverse the array once.
- For each number:
    - Compute its required complement:
        `need = k - num`
    - If the complement exists in `freq` with a positive frequency:
        - A valid pair is found.
        - Increment the operation count.
        - Decrease the complement's frequency since it has been used.
    - Otherwise:
        - Store the current number by increasing its frequency.
- Return the total number of valid operations.

Why use a frequency hash map?
- It keeps track of numbers that have been seen but not yet paired.
- This allows us to determine in O(1) average time whether the current
  number can complete a valid pair.

Why look for the complement first?
- Every pair must satisfy:
      num + need = k
- Instead of storing every possible pair, we simply check whether the
  required complement has already appeared.
- If it has, we immediately form a pair.

Why decrease the complement's frequency?
- Each element can be used in at most one operation.
- Once a complement is paired, it is consumed and should not be reused.
- Decreasing its frequency marks one occurrence as used.

Why store the current number only when no pair exists?
- If no complement is available, the current number cannot form a pair yet.
- It is saved for future numbers that may complete the pair.

Example:
nums = [1, 2, 3, 4], k = 5

num = 1
need = 4
freq = {1:1}

num = 2
need = 3
freq = {1:1, 2:1}

num = 3
need = 2
Pair found.
count = 1
freq = {1:1, 2:0}

num = 4
need = 1
Pair found.
count = 2
freq = {1:0, 2:0}

Answer = 2

Key Insight:
- Instead of searching the remaining array for a matching value,
  remember unmatched numbers using a hash map.
- Each number is processed exactly once, giving an optimal O(n)
  solution.
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {}
        for num in nums:
            need = k-num
            if freq.get(need, 0) > 0:
                count += 1
                freq[need] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
        
        return count
        