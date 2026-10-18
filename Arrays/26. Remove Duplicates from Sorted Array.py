"""
Problem: 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Approach 1: Using a Dictionary to Track Unique Elements

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:

* Array Manipulation
* Hashing / Dictionary
* In-Place Array Modification

Approach:

* Initialize `k = 0` to track the position where the next unique element will be placed.
* Create an empty dictionary `dic` to keep track of elements encountered.
* Iterate through each element in `nums`.
* If the element is not in the dictionary:
    * Add it to the dictionary.
    * Place it at index `k` in `nums`.
    * Increment `k`.
* If the element already exists, increment its count in the dictionary.
* Return `k`, the number of unique elements.

Why it works:

* The dictionary identifies whether an element has already been encountered.
* Each unique element is copied to the next available position in the array.
* The first `k` positions contain all unique elements in their original order.

Limitation:

* The dictionary requires O(n) extra space in the worst case.
* Since the array is already sorted, using a dictionary is unnecessary because duplicates are adjacent.
"""

# Using a dictionary to track unique elements and overwrite duplicates in-place
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
                nums[k] = num
                k+=1
            else:
                dic[num]+=1
        return k
    
"""
Problem: 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Approach 2: Using Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Two Pointers
* Array Manipulation
* In-Place Modification
* Sorted Array

Approach:

* Initialize `k = 1` because the first element is always unique when the array is non-empty.
* Iterate through the array starting from index `1` using pointer `i`.
* Compare `nums[i]` with `nums[i - 1]`.
* If they are different:
    * Place `nums[i]` at index `k`.
    * Increment `k`.
* If they are equal, skip the duplicate.
* Return `k`, the number of unique elements.

Why it works:

* Since the array is sorted, duplicate elements are always adjacent.
* Comparing the current element with the previous element identifies the start of each new unique value.
* Pointer `k` tracks the position where the next unique element should be written.
* The first `k` positions contain the unique elements in their original sorted order.

Limitation:

* This approach assumes the input array is sorted.
* If the array is empty, `k = 1` would be incorrect; initialize `k = 0` or handle the empty array separately.

"""

# Using two pointers to remove duplicates from a sorted array in-place
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k