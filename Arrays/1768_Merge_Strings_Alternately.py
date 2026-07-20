"""
    Problem: 1768. Merge Strings Alternately

    Difficulty: Easy

    Time Complexity: O((n + m)²)
    Space Complexity: O(n + m)

    Pattern:
    Two Pointers
    String Manipulation

    Approach:
    - Traverse both strings up to the length of the shorter string.
    - Append characters alternately using string concatenation.
    - Append the remaining substring from the longer string.

    Note:
    - This solution is simple and readable, but repeated string concatenation
    ('+=') creates new strings on each iteration, making the worst-case
    time complexity O((n + m)²).
    - A more efficient approach is to append characters to a list and use
    ''.join() at the end, achieving O(n + m) time complexity.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n = len(word1)
        m = len(word2)
        min_len = min(n, m)
     
        for i in range(min_len):
            res += word1[i] + word2[i]
        if n>m:
            res += word1[min_len:]
        else:
            res += word2[min_len:]
        return res
    
"""
    More Efficient Approach:
    Problem: 1768. Merge Strings Alternately

    Difficulty: Easy

    Time Complexity: O(n + m)

    Space Complexity: O(n + m)

    Pattern:
    Two Pointers
    String Construction (List + Join)

    Key Idea:
    - Traverse both strings simultaneously using two pointers.
    - Append characters alternately to a list.
    - Append the remaining characters from the longer string.
    - Use ''.join() to build the final string efficiently, avoiding repeated string concatenation.
    
    Approach:
    1. Initialize two pointers for both strings.
    2. Append one character from each string alternately.
    3. After one string is exhausted, append the remaining characters
       from the other string.
    4. Convert the list into a string using ''.join().
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = b = 0
        res = []
        while a<len(word1) and b<len(word2):
            res.append(word1[a])
            res.append(word2[b])
            a+=1
            b+=1
        res.extend(word1[a:])
        res.extend(word2[b:])
        return ''.join(res)