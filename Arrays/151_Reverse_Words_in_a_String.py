"""
Problem: 151. Reverse Words in a String

Difficulty: Medium

Time Complexity: O(n)

Space Complexity: O(n)

Pattern:
- String Manipulation
- Split and Join
- Reversal

Approach:
- Replace multiple consecutive spaces with a single space using regex.
- Remove leading and trailing spaces.
- Split the cleaned string into a list of words.
- Reverse the list.
- Join the words using a single space.

Why it works:
- `re.sub()` ensures every group of spaces becomes one space.
- `strip()` removes extra spaces at both ends.
- Splitting gives individual words.
- Reversing changes their order.
- Joining reconstructs the required string with exactly one space between words.
"""
import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(r'\s+', ' ', s).strip()
        s = s.split(' ')
        s = s[::-1]
        return ' '.join(s)
# OR
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
    
"""
Problem: 151. Reverse Words in a String

Difficulty: Medium

Time Complexity: O(n)

Space Complexity: O(1)   (Follow-up: assuming the string is mutable)

Pattern:
Two Pointers
String Manipulation
In-Place Reversal

Approach:
- Treat the input as a mutable character array.
- Step 1: Remove extra spaces using two pointers:
    - Use a read pointer to scan every character.
    - Use a write pointer to overwrite the array with:
        - No leading spaces.
        - Exactly one space between words.
        - No trailing spaces.
- Step 2: Reverse the entire cleaned string using two pointers
  (left and right). This places the words in reverse order,
  but each word itself becomes reversed.
- Step 3: Traverse the string to locate each word.
    - For every word, use two pointers (start and end)
      to reverse only that word.
- The final result has:
    - Words in reverse order.
    - Correct character order within each word.
    - Exactly one space separating consecutive words.

Note:
- The algorithm combines three different two-pointer techniques:
    1. Read/Write pointers for removing extra spaces.
    2. Left/Right pointers for reversing the entire string.
    3. Start/End pointers for reversing individual words.
- Every character is visited only a constant number of times,
  resulting in O(n) time complexity.
- This achieves O(1) extra space only when the string is mutable
  (e.g., C++, Java char[], C). In Python, strings are immutable,
  so an in-place solution is not possible.
"""