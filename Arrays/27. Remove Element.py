"""
Problem: 27. Remove Element
Difficulty: Easy

Approach 1: Remove Elements by Shifting

Time Complexity: O(n²)

Space Complexity: O(1)

Pattern:

* Array Manipulation
* In-Place Modification
* Element Shifting

Approach:

* Initialize n with the length of nums and i = 0.
* Traverse the array using a while loop.
* If nums[i] equals val, shift all subsequent elements one position to the left.
* Decrease n by 1 because one occurrence has been removed from the valid portion.
* Do not increment i after shifting, because the next element may also equal val.
* If nums[i] does not equal val, increment i.
* Return n as the number of remaining elements.

Why it works:

* Shifting overwrites the element that needs to be removed.
* Decreasing n reduces the valid portion of the array.
* Keeping i unchanged after shifting ensures consecutive occurrences of val are checked.

Limitation:

* Shifting elements takes O(n) time for each removal.
* If many elements need to be removed, the overall time complexity becomes O(n²).
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]

                n -= 1
            else:
                i += 1

        return n


"""
Problem: 27. Remove Element
Difficulty: Easy

Approach 2: Repeated Removal Using Built-in remove()

Time Complexity: O(n²)

Space Complexity: O(1) auxiliary space

Pattern:

* Array Manipulation
* Built-in List Methods
* In-Place Modification

Approach:

* Use a while loop to check whether val exists in nums.
* If val exists, remove its first occurrence using nums.remove(val).
* Repeat until no occurrence of val remains.
* Return the length of the modified list.

Why it works:

* The in operator checks whether val exists in the list.
* The remove() method deletes the first occurrence and shifts subsequent elements to the left.
* Repeating the process removes every occurrence of val.

Limitation:

* Both the membership check and remove() can take O(n) time.
* Repeating these operations for multiple occurrences results in O(n²) time complexity in the worst case.
* It relies on repeated built-in operations rather than a single traversal.
"""

# Using built-in remove() to delete all occurrences
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)
    

"""
Problem: 27. Remove Element
Difficulty: Easy

Approach 3: Two Pointers (Read and Write)

Time Complexity: O(n)

Space Complexity: O(1)

Pattern:

* Two Pointers
* In-Place Array Modification
* Read and Write Pointers

Approach:

* Initialize k = 0 to track the position where the next valid element should be written.
* Use i to traverse every element in nums.
* If nums[i] is not equal to val, copy nums[i] to nums[k].
* Increment k after writing a valid element.
* Skip elements equal to val.
* Return k as the number of elements that are not equal to val.

Why it works:

* Pointer i reads every element exactly once.
* Pointer k tracks the next available position for a valid element.
* Copying valid elements to the front overwrites unwanted elements.
* Since k never exceeds i, no unread elements are overwritten.
* The first k positions contain all elements that are not equal to val, preserving their relative order.

Limitation:

* The remaining positions after index k - 1 are irrelevant and do not need to be modified.
* This approach requires understanding the distinction between the read pointer i and the write pointer k.
"""

# Using two pointers to overwrite unwanted elements
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k