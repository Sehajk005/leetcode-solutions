"""
Problem: 345. Reverse Vowels of a String

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(n)

Pattern:
String Manipulation
Array Simulation
Two-Pass Traversal

Approach:
- Convert the string into a list since strings are immutable in Python.
- Traverse the string once and store all vowels in a separate list.
- Traverse the character list again:
    - Whenever a vowel is encountered, replace it with the last vowel from the stored list.
    - Using pop() reverses the vowel order naturally.
- Join the modified character list back into a string and return it.

Note:
- The string is traversed twice, but each traversal is linear, giving an overall time complexity of O(n).
- Extracting vowels requires scanning the entire string, even though only k vowels are stored.
- The extra vowel list requires O(k) space, where k is the number of vowels.
- Converting the string to a list requires O(n) space, making the overall auxiliary space O(n + k), which simplifies to O(n) since k ≤ n.
- This is a simple and readable solution, though it is not the most space-efficient.
- An optimal approach uses the Two Pointers technique to swap vowels in place while traversing from both ends, achieving O(n) time with O(n) total output storage and only O(1) auxiliary space.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = [ch for ch in s if ch in "aeiouAEIOU"]
        for i, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                s[i] = vowels.pop()
        return ''.join(s)
    

"""
Problem: 345. Reverse Vowels of a String

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(n)

Pattern:
Two Pointers
String Manipulation

Approach:
- Convert the string into a list since strings are immutable in Python.
- Initialize two pointers:
    - left at the beginning of the string.
    - right at the end of the string.
- While left < right:
    - Move the left pointer forward until it points to a vowel.
    - Move the right pointer backward until it points to a vowel.
    - Swap the vowels at the left and right pointers.
    - Move both pointers inward.
- Join the modified list back into a string and return it.

Note:
- Each pointer only moves toward the center and never revisits a character.
- Although there are nested while loops, each character is processed at most once by each pointer, so the overall time complexity remains O(n), not O(n²).
- Converting the string to a list requires O(n) space.
- Apart from the character list, only two pointers and a constant-sized vowel string are used, so the auxiliary space is O(1).
- This is the optimal Two Pointers approach for this problem, achieving O(n) time with O(1) auxiliary space.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        left = 0
        right = len(s)-1
        vowels = "aeiouAEIOU"
        while left<right:
            while left<right and s[left] not in vowels:
                left += 1
            while left<right and s[right] not in vowels:
                right-=1
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return ''.join(s)
