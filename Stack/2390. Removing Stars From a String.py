"""
Optimal Approach:
Stack

Problem: 2390. Removing Stars From a String

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
Stack

Approach:

- Maintain a stack using a list called output.
- Traverse the string character by character.
- If the current character is a normal character,
  add it to the stack using append().
- If the current character is '*',
  remove the most recently added character using pop().
- The most recently added character is exactly the
  closest non-star character to the left.
- At the end, join the stack to form the resulting string.

Key Insight:

- A '*' always removes the closest non-star character
  to its left.
- A stack follows Last In, First Out (LIFO).
- Therefore, the most recently added character is the
  correct character to remove.
- append() adds a character to the stack.
- pop() removes the most recently added character.
- Each character is processed only once, giving O(n)
  time complexity.

Example:
s = "leet**cod*e"

Process:

'l' → ['l']
'e' → ['l', 'e']
'e' → ['l', 'e', 'e']
't' → ['l', 'e', 'e', 't']

'*' → remove 't'
      ['l', 'e', 'e']

'*' → remove 'e'
      ['l', 'e']

'c' → ['l', 'e', 'c']
'o' → ['l', 'e', 'c', 'o']
'd' → ['l', 'e', 'c', 'o', 'd']

'*' → remove 'd'
      ['l', 'e', 'c', 'o']

'e' → ['l', 'e', 'c', 'o', 'e']

Final Result:
"lecoe"


Note:

- Use a list as a stack.
- append() → push element onto the stack.
- pop() → remove the most recently added element.
- The stack must be checked before pop() using
  "if output" to avoid popping from an empty list.
- Each character is pushed at most once and popped at most once.
- Therefore, the overall time complexity is O(n).
- The list can contain up to O(n) characters,
  so space complexity is O(n).

Important Pattern:

"Remove the most recent element"
        ↓
      STACK
        ↓
LIFO (Last In, First Out)
"""
class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for ch in s:
            if output and ch == '*':
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)