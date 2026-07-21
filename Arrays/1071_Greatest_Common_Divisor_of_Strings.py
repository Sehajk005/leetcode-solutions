"""
Problem: 1071. Greatest Common Divisor of Strings

Difficulty: Easy

Time Complexity: O(min(n, m) × (n + m))
Worst Case: O(N²), where N is the length of the strings when n ≈ m.

Space Complexity: O(n + m)

Pattern:
Brute Force
String Manipulation
Prefix Checking

Approach:
- Iterate through every common prefix of both strings from shortest to longest.
- For each common prefix:
    - Treat it as a candidate divisor.
    - Repeat it enough times to reconstruct both strings.
    - If it exactly reconstructs both strings, update the answer.
- Return the last valid divisor found, which is the longest valid prefix.

Note:
- This solution checks every possible common prefix, making it a brute-force approach.
- String slicing and string multiplication create new strings, increasing the overall time complexity.
- Although correct, it is not the most optimal solution.
- An optimal approach first checks whether (str1 + str2) == (str2 + str1). If true, the answer is the prefix of length gcd(len(str1), len(str2)), achieving O(n + m) time complexity.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = min(len(str1), len(str2))
        ans = ''
        for i in range(n):
            if str2[:i+1] == str1[:i+1]:
                t=str2[:i+1]
                times2 = len(str2)//len(t)
                times1 = len(str1)//len(t)
                if t*times2 == str2 and t*times1 == str1:
                    ans = t
        return ans
    
    
"""
optimal Approach:
Problem: 1071. Greatest Common Divisor of Strings

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Pattern:
Math
String Manipulation
Greatest Common Divisor (GCD)

Approach:
- First, check whether both strings are composed of the same repeating pattern.
- If (str1 + str2) != (str2 + str1), no common divisor string exists, so return "".
- Otherwise, compute the GCD of the two string lengths.
- The answer is the prefix of str1 whose length is gcd(len(str1), len(str2)).

Key Insight:
- A divisor string must be able to generate both strings by repeated concatenation.
- Therefore, its length must divide both string lengths.
- The largest possible divisor length is gcd(len(str1), len(str2)).
- The concatenation check guarantees that both strings share the same repeating pattern, making the prefix of GCD length the greatest common divisor string.

Note:
- This is the optimal solution.
- The concatenation check eliminates all invalid cases in O(n + m) time.
- Computing the GCD of the lengths is very efficient (Euclidean Algorithm), and extracting the prefix takes O(gcd(n, m)).
"""

from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]