"""
Problem: 88. Merge Sorted Array
Difficulty: Easy
Approach 1: Merge Two Arrays and Sort Using Bubble Sort

Time Complexity: O((m + n)²)

Space Complexity: O(1)

Pattern:

* Array Manipulation
* Bubble Sort
* In-Place Sorting

Approach:

* Copy all elements of `nums2` into the empty positions at the end of `nums1`.
* Use nested loops to compare adjacent elements.
* Swap elements if the current element is greater than the next element.
* Repeat until the entire array is sorted.

Why it works:

* Copying combines both arrays into `nums1`.
* Bubble sort repeatedly moves the largest unsorted element to its correct position.
* After all passes, the merged array is sorted in ascending order.

Limitation:

* Bubble sort takes O((m + n)²) time, making it inefficient for large arrays.
"""
# Using merging to merge 2 arrays then sorting using bubble sort
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        for i in range(m+n):
            for j in range(0, m+n-i-1):
                if nums1[j] > nums1[j+1]:
                    temp = nums1[j]
                    nums1[j] = nums1[j+1]
                    nums1[j+1] = temp
        return nums1

"""
Problem: 88. Merge Sorted Array

Difficulty: Easy

Approach 2: Merge Two Arrays and Sort Using Python's Built-in Sort

Time Complexity: O((m + n) log(m + n)) in the general case

Space Complexity: O(m + n) worst case for Python's sorting implementation

Pattern:

* Array Manipulation
* Built-in Sorting
* In-Place Sorting

Approach:

* Copy all elements of `nums2` into the empty positions at the end of `nums1`.
* Use Python's built-in `sort()` method to sort the combined array.

Why it works:

* Copying combines both arrays into `nums1`.
* The `sort()` method arranges all elements in ascending order.
* Python's built-in sorting algorithm, Timsort, is generally more efficient than bubble sort.

Limitation:

* This approach does not take advantage of the fact that both arrays are already sorted.
"""
# Using merging to merge 2 arrays then sorting using python's built-in sort function
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()
        return nums1
    
    
"""
Problem: 88. Merge Sorted Array

Difficulty: Easy

Approach 3: Merge Using Three Pointers (In-Place)

Time Complexity: O(m + n)

Space Complexity: O(1)

Pattern:

* Two Pointers
* In-Place Array Manipulation
* Merging Sorted Arrays
* Reverse Traversal

Approach:

* Initialize three pointers:

  * `i = m - 1`: Points to the last valid element in `nums1`.
  * `j = n - 1`: Points to the last element in `nums2`.
  * `k = m + n - 1`: Points to the last available position in `nums1`.
* Compare the elements at `nums1[i]` and `nums2[j]`.
* Place the larger element at `nums1[k]`.
* Move the corresponding pointer backward and decrement `k`.
* Continue until either array has no elements remaining.
* Copy any remaining elements from `nums2` into `nums1`.

Why it works:

* Both arrays are already sorted, so their largest elements are at the end.
* Comparing the largest remaining elements identifies which element belongs at the current last position.
* Filling from right to left prevents overwriting unprocessed elements in `nums1`.
* Any remaining elements in `nums1` are already in their correct positions.
* Each element is processed at most once, resulting in linear time complexity.

Best Approach:

* Approach 3 is optimal because it uses the existing sorted order of both arrays.
* It achieves O(m + n) time complexity and O(1) extra space.
"""
# Using 3 pointers to merge and sort 2 arrays in-place
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        i = m-1
        j = n-1
        k = m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        
