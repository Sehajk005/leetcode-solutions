"""
Problem: 169. Majority Element
Difficulty: Easy
Approach 1: Brute Force Using Nested Loops

Time Complexity: O(n²)
Space Complexity: O(1)

Pattern:

* Array Traversal
* Brute Force
* Frequency Counting

Approach:

* Calculate `n = len(nums)`.
* Iterate through each element using the outer loop.
* Initialize `k = 0` to count the occurrences of the current element.
* Use the inner loop to compare the current element with every element in the array.
* If `nums[i] == nums[j]`, increment `k`.
* If `k > n/2`, return `nums[i]` as the majority element.

Why it works:

* Every element is checked against all elements in the array.
* The count represents the total frequency of the current element.
* An element occurring more than n/2 times is the majority element.

Limitation:

* The nested loops result in O(n²) time complexity.
* The same element may be counted repeatedly.
* Inefficient for large arrays compared to hashing or Boyer-Moore Voting.
"""

# Brute force: Count the frequency of every element using nested loops.
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        for i in range(n):
            k = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    k += 1
            if k > n/2:
                return nums[i]


"""
Problem: 169. Majority Element
Difficulty: Easy
Approach 2: Using a Dictionary (Hash Map)

Time Complexity: O(n) — average case
Space Complexity: O(n)

Pattern:

* Array Traversal
* Hashing / Dictionary
* Frequency Counting

Approach:

* Initialize an empty dictionary `dic` to store element frequencies.
* Calculate `n = len(nums)`.
* Iterate through each element in `nums`.
* Update its frequency using `dic[num] = dic.get(num, 0) + 1`.
* After updating the frequency, check whether `dic[num] > n/2`.
* If the condition is satisfied, return `num` immediately.

Why it works:

* The dictionary stores the frequency of each element encountered.
* `dic.get(num, 0)` returns the existing count or 0 if the element is new.
* Once an element occurs more than n/2 times, it must be the majority element.
* Returning immediately avoids unnecessary iterations.

Limitation:

* The dictionary can require O(n) extra space.
* Hash-map operations take O(1) time on average, but their worst-case performance can differ.
* The extra space can be avoided using Boyer-Moore Voting Algorithm.
"""

# Hash map: Track element frequencies and return once the majority threshold is reached.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic = {}
        n = len(nums)
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num]>(n/2):
                return num


"""
Problem: 169. Majority Element
Difficulty: Easy
Approach 3: Boyer-Moore Voting Algorithm

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Traversal
* Greedy Algorithm
* Candidate Elimination
* Boyer-Moore Voting

Approach:

* Initialize `candidate = nums[0]` and `count = 0`.
* Iterate through every element in `nums`.
* If `count == 0`, select the current element as the new candidate.
* If the current element equals the candidate, increment `count`.
* Otherwise, decrement `count`.
* Return `candidate` after completing the traversal.

Why it works:

* Each occurrence of the candidate adds one vote.
* Each different element cancels one vote.
* Since the majority element occurs more than n/2 times, it cannot be completely eliminated by all other elements.
* Therefore, the majority element remains the final candidate.

Limitation:

* This algorithm assumes that a majority element is guaranteed to exist.
* If no majority element is guaranteed, a second pass is required to verify the candidate.

Important:

* `count` represents the candidate's remaining votes, not its actual frequency in the entire array.
* The candidate is replaced whenever `count == 0`.

"""

# Boyer-Moore Voting: Find the majority candidate using cancellation of opposing votes.          
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        n = len(nums)
        count = 0
        for i in range(n):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate


"""
Problem: 169. Majority Element
Difficulty: Easy
Approach 4: Sorting the Array

Time Complexity: O(n log n)
Space Complexity: Depends on the sorting implementation

Pattern:

* Array Sorting
* Index-Based Selection
* Mathematical Observation

Approach:

* Calculate `n = len(nums)`.
* Sort the array using `nums.sort()`.
* Return the element at index `n // 2`.

Why it works:

* The majority element occurs more than n/2 times.
* After sorting, all occurrences of the same element appear consecutively.
* Because the majority element occupies more than half the array, its consecutive block must contain the middle index.
* Therefore, `nums[n // 2]` is guaranteed to be the majority element.

Limitation:

* Sorting takes O(n log n) time.
* The array is modified in-place.
* Python's sorting implementation may require additional memory.
* Boyer-Moore Voting achieves O(n) time and O(1) auxiliary space.

"""

# Sorting: Place equal elements together and return the middle element. 
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n//2]