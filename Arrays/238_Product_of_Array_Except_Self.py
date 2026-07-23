"""
Problem: 238. Product of Array Except Self

Difficulty: Medium

Time Complexity: O(n)
- First pass: Build prefix array → O(n)
- Second pass: Build suffix array → O(n)
- Third pass: Multiply prefix and suffix → O(n)
- Total = O(n)

Space Complexity: O(n)
- Prefix array: O(n)
- Suffix array: O(n)
- Answer array is ignored when considering extra space only.

Pattern:
- Prefix Sum / Prefix Product
- Suffix Product
- Array Traversal

Approach:
- Create a prefix array where prefix[i] stores the product of all elements before index i.
- Create a suffix array where suffix[i] stores the product of all elements after index i.
- Reverse the suffix array since it is built from right to left.
- Multiply prefix[i] and suffix[i] to obtain the product of all elements except nums[i].

Why it works:
- Every element's answer equals:
      Product of elements on the left
      ×
      Product of elements on the right
- Prefix stores the left product.
- Suffix stores the right product.
- Their multiplication gives the required result.

Pros:
- Easy to understand.
- Straightforward implementation.
- Good stepping stone to the optimal solution.

Cons:
- Uses two additional arrays, increasing space complexity.
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        ans = []
        n = len(nums)
        pro_pre = 1
        pro_suff = 1
        for i in range(n):
            if i==0:
                prefix.append(pro_pre)
            else:
                pro_pre *= nums[i-1]
                prefix.append(pro_pre)
        for i in range(n-1, -1, -1):
            if i==n-1:
                suffix.append(pro_suff)
            else:
                pro_suff *= nums[i+1]
                suffix.append(pro_suff)
        suffix.reverse()
        for i in range(n):
            ans.append(prefix[i] * suffix[i])
        return ans

"""
Problem: 238. Product of Array Except Self

Difficulty: Medium

Time Complexity: O(n)
- First pass: Store prefix products in answer array → O(n)
- Second pass: Multiply running suffix product → O(n)
- Total = O(n)

Space Complexity: O(1)
- Uses only two variables (prefix and suffix).
- The answer array is required output and does not count as extra space.

Pattern:
- Prefix Product
- Running Suffix Product
- Space Optimization

Approach:
- Traverse from left to right while maintaining a running prefix product.
- Store the prefix product directly in the answer array.
- Traverse from right to left while maintaining a running suffix product.
- Multiply each answer element by the current suffix product.

Why it works:
- After the first pass:
      ans[i] = product of all elements before i
- During the second pass:
      suffix = product of all elements after i
- Multiplying them gives:
      left product × right product
      = product of every element except nums[i].

Pros:
- Optimal time complexity.
- Optimal extra space complexity.
- No division used.
- Correctly handles arrays containing zeros.

Cons:
- Slightly less intuitive than maintaining separate prefix and suffix arrays.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        pro_pre = 1
        pro_suff = 1
        for i in range(n):
            if i==0:
                ans.append(pro_pre)
            else:
                pro_pre *= nums[i-1]
                ans.append(pro_pre)
        for i in range(n-1, -1, -1):
            if i==n-1:
                ans[i] *= pro_suff
            else:
                pro_suff *= nums[i+1]
                ans[i] *= pro_suff
        return ans
