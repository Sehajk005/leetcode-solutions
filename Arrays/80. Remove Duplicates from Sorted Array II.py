"""
Problem: 80. Remove Duplicates from Sorted Array II
Difficulty: Medium
Approach 1: Using a While Loop and Counting Consecutive Duplicates

Time Complexity: O(n²)
Space Complexity: O(1)

Pattern:

* Array Manipulation
* Two Pointers / Index Tracking
* In-Place Modification
* Counting Consecutive Elements

Approach:

* Initialize `i = 1` to start checking elements from the second position.
* Initialize `count = 1` because the first element has already appeared once.
* Traverse the array using a `while` loop.
* If `nums[i] == nums[i-1]`:
    * Increment `count` to track consecutive occurrences.
    * If `count > 2`, remove the current element using `nums.pop(i)`.
    * Decrement `i` because removing an element shifts the next element into the current index.
* Otherwise, reset `count = 1` because a new number has been encountered.
* Increment `i` to continue traversal.
* Return `i`, which represents the final length of the modified array.

Why it works:

* Since the array is sorted, duplicate elements appear consecutively.
* The counter tracks how many times the current number appears in a row.
* Whenever a number appears more than twice, the extra occurrence is removed.
* Decrementing `i` ensures that the element shifted into the removed element's position is checked.

Limitation:

* Removing an element using `pop(i)` requires shifting subsequent elements.
* Repeated removals can make the overall time complexity O(n²).
* The approach modifies the array in-place and uses O(1) auxiliary space.
"""

# Using a while loop to count consecutive duplicates and remove occurrences beyond two.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i , count = 1, 1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                if count>2:
                    nums.pop(i)
                    i-=1
            else:
                count = 1
            i+=1
        return i


"""
Problem: 80. Remove Duplicates from Sorted Array II
Difficulty: Medium
Approach 2: Using a Dictionary to Track Frequencies

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:

* Array Manipulation
* Hashing / Dictionary
* Frequency Counting
* In-Place Array Modification

Approach:

* Create an empty dictionary `dic` to store the frequency of each element.
* Traverse `nums` and count the occurrences of every number.
* Initialize `k = 0` to track the next position where an element should be placed.
* Traverse `nums` again.
* For each number:
    * If its frequency is greater than zero and at most two, place it at index `k` and increment `k`.
    * Otherwise, if its frequency is greater than two, decrement its frequency to track the remaining excess occurrences.
* Return `k`, the length of the valid portion of the array.

Why it works:

* The dictionary stores the total frequency of every number.
* Because the array is sorted, each number appears in one consecutive group.
* The second traversal retains at most two occurrences of each number while preserving the original order.
* The retained elements overwrite the beginning of the original array.

Limitation:

* The dictionary requires O(n) extra space in the worst case.
* The frequency-counting approach is more complicated than necessary because the input array is already sorted.
* A direct comparison with the element two positions behind can solve the problem without extra space.
"""

# Using a dictionary to count frequencies and retain at most two occurrences of each number.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        k = 0
        for num in nums:
            if dic[num]>0:
                if dic[num]<=2:
                    nums[k] = num
                    k+=1
                else:
                    dic[num]-=1
        return k


"""
Problem: 80. Remove Duplicates from Sorted Array II
Difficulty: Medium
Approach 3: Using Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Two Pointers
* Array Manipulation
* In-Place Modification
* Sorted Array
* Read and Write Pointers

Approach:

* Initialize `k = 2`, representing the next position where a valid element can be placed.
* The first two elements can always remain because each number is allowed to appear at most twice.
* Iterate through the array starting at index `i = 2`.
* Compare `nums[i]` with `nums[k-2]`.
* If they are different:
    * The current element can be included without causing any number to appear more than twice.
    * Place `nums[i]` at index `k`.
    * Increment `k`.
* If they are equal:
    * Skip the current element because including it would create more than two occurrences of that number in the valid portion.
* Return `k`, the length of the modified array.

Why it works:

* The array is sorted, so equal elements appear consecutively.
* The first `k` positions always contain the valid elements processed so far.
* Comparing `nums[i]` with `nums[k-2]` checks whether the current number would exceed the allowed frequency of two.
* The read pointer `i` scans the original array, while the write pointer `k` tracks the next valid position.
* Every element is processed at most once, and the array is modified in-place.

Advantages:

* Optimal O(n) time complexity.
* O(1) auxiliary space.
* No dictionary, extra array, or element shifting is required.
* This is the preferred solution for sorted arrays when each element can appear at most twice.
"""

# Using two pointers to overwrite invalid duplicates in-place in linear time.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k