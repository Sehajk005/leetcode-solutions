"""
Approach 1:
Manual Frequency Map + Character Set Comparison

Problem: 1657. Determine if Two Strings Are Close

Difficulty: Medium

Time Complexity:
- O(n)

Space Complexity:
- O(k)

Pattern:
Hash Map

Approach:
- If the lengths of the two strings are different, return False.
- Build a frequency map for each string using a dictionary and if-else statements.
- Compare the sets of keys (characters).
- If the character sets are different, return False.
- Extract the frequency values from both maps.
- Sort both frequency lists.
- Return True if the sorted frequency lists are equal.

Key Insight:
- Close strings must contain exactly the same unique characters.
- The actual characters can be transformed into each other by swapping frequencies.
- Therefore:
    1. Character sets must match.
    2. Frequency multisets must match.

Example:
word1 = "abbccc"
word2 = "cccbba"

Frequency Maps:
word1:
a → 1
b → 2
c → 3

word2:
a → 1
b → 2
c → 3

Character Sets:
{'a','b','c'}

Sorted Frequencies:
[1,2,3]

Output:
True

Note:
- Most beginner-friendly implementation.
- Explicitly shows how a frequency dictionary is built.
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}

        # Build frequency map for word1
        for ch in word1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1

        # Build frequency map for word2
        for ch in word2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        # Same set of characters?
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Same frequency multiset?
        freq_list1 = list(freq1.values())
        freq_list2 = list(freq2.values())

        freq_list1.sort()
        freq_list2.sort()

        return freq_list1 == freq_list2


"""
Approach 2:
Dictionary get() + Character Set Comparison

Problem: 1657. Determine if Two Strings Are Close

Difficulty: Medium

Time Complexity:
- O(n)

Space Complexity:
- O(k)

Pattern:
Hash Map

Approach:
- If the lengths differ, return False.
- Build frequency maps using dict.get().
- Compare the sets of characters.
- Compare the sorted frequency values.
- Return True only if both comparisons match.

Key Insight:
- dict.get(key, 0) returns 0 when the key is absent.
- This allows updating frequencies in a single line.
- The algorithm remains identical to the manual dictionary approach.

Example:
word1 = "abcabb"
word2 = "bacbab"

Frequency Maps:
a → 2
b → 3
c → 1

Character Sets:
{'a','b','c'}

Sorted Frequencies:
[1,2,3]

Output:
True

Note:
- Cleaner and more Pythonic than using if-else.
- Preferred when manually implementing frequency maps.
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        freq1 = {}
        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1
        freq2= {}
        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1
        return (
            set(freq1.keys()) == set(freq2.keys())
            and sorted(freq1.values()) == sorted(freq2.values())
        )
        

"""
Approach 3:
Counter + Character Set Comparison

Problem: 1657. Determine if Two Strings Are Close

Difficulty: Medium

Time Complexity:
- O(n)

Space Complexity:
- O(k)

Pattern:
Hash Map (Counter)

Approach:
- If the lengths differ, return False.
- Use Counter() to build the frequency map for each string.
- Compare the sets of characters.
- Compare the sorted frequency values.
- Return True if both conditions hold.

Key Insight:
- Counter automatically counts the occurrences of each character.
- It replaces manual frequency counting with a single function call.
- The underlying algorithm is exactly the same as the previous approaches.

Example:
word1 = "cabbba"
word2 = "abbcbc"

Counter(word1):
a → 2
b → 3
c → 1

Counter(word2):
a → 1
b → 3
c → 2

Character Sets:
{'a','b','c'}

Sorted Frequencies:
[1,2,3]

Output:
True

Note:
- Shortest and most readable solution.
- Commonly used in Python interviews and production code.
- Same time and space complexity as the other two approaches.
"""
from collections import Counter   
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return (
            set(freq1.keys()) == set(freq2.keys())
            and sorted(freq1.values()) == sorted(freq2.values())
        )