"""
Problem: 392. Is Subsequence

Approach:
- Use one pointer (j) to track the current character in string s.
- Traverse string t from left to right.
- Whenever the current character in t matches s[j],
  move j to the next character in s.
- If all characters of s are matched (j == len(s)),
  return True immediately.
- If the traversal finishes before matching all characters,
  return False.

Example:
s = "abc"
t = "ahbgdc"

t = a h b g d c
    ^
Match 'a' -> j = 1

t = a h b g d c
        ^
Match 'b' -> j = 2

t = a h b g d c
            ^
Match 'c' -> j = 3

j == len(s) -> True

Time Complexity:
- O(len(t))
  We scan string t only once.

Space Complexity:
- O(1)
  Only one pointer is used.

Key Insight:
- We never move backwards in either string.
- Characters only need to appear in the same order,
  not necessarily consecutively.
- The condition (j < len(s)) prevents accessing s out of bounds.
- Early return stops the traversal as soon as the entire subsequence is found.

Edge Cases:
- s = ""        -> True
- t = ""        -> False (unless s is also empty)
- s longer than t -> False
- Repeated characters are handled naturally.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for ch in t:
            if j<len(s) and ch == s[j]:
                j+=1
                if j==len(s):
                    return True
        return j == len(s)
        