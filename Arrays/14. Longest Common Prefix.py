"""
Problem: 14. Longest Common Prefix
Difficulty: Easy

Approach 1: Comparing Adjacent Strings Character by Character

Time Complexity: O(n * m)
Space Complexity: O(m)

Where:
* n = Number of strings
* m = Length of the shortest string

Pattern:

* String Manipulation
* Nested Loops
* Character-by-Character Comparison
* Prefix Matching

Approach:

* Initialize `out = ''` to store the longest common prefix.
* Handle edge cases:
    * If `strs` is empty, return an empty string.
    * If there is only one string, return that string itself.
* Find the length of the shortest string using `min()` because the common prefix cannot be longer than the shortest string.
* Iterate through each character position using the outer loop.
* Use the inner loop to compare characters at the same index in adjacent strings.
* If two adjacent strings have different characters at the current index:
    * Return `out` because the common prefix ends at this position.
* If all adjacent strings have the same character:
    * Append that character to `out`.
* Return `out` after all character positions have been checked.

Why it works:

* A common prefix requires every string to have the same character at each position.
* Comparing adjacent strings ensures that all strings contain the same character at the current index.
* If any mismatch occurs, no further characters can be part of the common prefix.
* The shortest string determines the maximum possible prefix length.

Limitation:

* The algorithm performs adjacent comparisons instead of comparing every string directly with the first string.
* The special handling for a single string is unnecessary because the general algorithm can handle it.
* The `continue` statement is unnecessary because the loop naturally proceeds to the next iteration.
"""
# Compare adjacent strings character by character to build the longest common prefix.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        out = ''
        if not strs:
            return out
        if len(strs) == 1:
            out += strs[0]
            return out
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return out
                else:
                    continue
            out += strs[j][i]
        return out


"""
Problem: 14. Longest Common Prefix
Difficulty: Easy

Approach 2: Vertical Scanning (Comparing Characters with the First String)

Time Complexity: O(n * m)
Space Complexity: O(1) auxiliary space

Where:
* n = Number of strings
* m = Length of the first string

Pattern:

* String Manipulation
* Vertical Scanning
* Nested Loops
* Character-by-Character Comparison

Approach:

* Handle the edge case:
    * If `strs` is empty, return an empty string.
* Use the first string (`strs[0]`) as the reference string.
* Iterate through each character index of the first string using the outer loop.
* For every character position, iterate through the remaining strings using the inner loop.
* Check two conditions:
    * If `i == len(strs[j])`, the current string has ended before reaching this index.
    * If `strs[0][i] != strs[j][i]`, the characters do not match.
* If either condition is true:
    * Return `strs[0][:i]`, which contains all matching characters before the mismatch.
* If every character matches across all strings:
    * Return the entire first string.

Why it works:

* The first string acts as the reference for identifying the common prefix.
* At each index, every other string must contain the same character.
* The first mismatch or the end of any string determines where the common prefix stops.
* If no mismatch occurs, the entire first string is the common prefix.

Advantages:

* No additional data structure is required.
* Directly compares every string against one reference string.
* The slicing operation returns the prefix up to the first mismatch.

Limitation:

* The algorithm may perform unnecessary comparisons if the common prefix is very short and there are many strings.
* It depends on the first string as the reference, although this does not affect correctness.
"""
# Use the first string as a reference and compare characters vertically across all strings.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]



"""
Problem: 14. Longest Common Prefix
Difficulty: Easy

Approach 3: Horizontal Scanning (Progressively Shrinking the Prefix)

Time Complexity: O(n * m)
Space Complexity: O(m) due to string slicing

Where:
* n = Number of strings
* m = Length of the first string

Pattern:

* String Manipulation
* Prefix Matching
* Horizontal Scanning
* Two Pointers / Prefix Reduction

Approach:

* Handle the edge case:
    * If `strs` is empty, return an empty string.
* Initialize `prefix = strs[0]` by assuming the first string is the common prefix.
* Iterate through the remaining strings using `strs[1:]`.
* For every string `s`, check whether it starts with the current prefix using `startswith()`.
* While the current string does not start with `prefix`:
    * Remove the last character from `prefix` using `prefix = prefix[:-1]`.
    * Continue shrinking the prefix until a match is found.
* If `prefix` becomes empty:
    * Return an empty string because no common prefix exists.
* After processing all strings, return the remaining prefix.

Why it works:

* Initially, the first string is treated as the potential common prefix.
* Each subsequent string must start with the current prefix.
* If it does not, removing the last character progressively reduces the prefix.
* Once a string starts with the prefix, that prefix is valid for all strings processed so far.
* After all strings are processed, the remaining prefix is common to every string.

Advantages:

* Simple and readable implementation.
* Uses Python's built-in `startswith()` method.
* Avoids explicitly comparing individual characters using nested loops.

Limitation:

* String slicing creates new string objects because Python strings are immutable.
* Repeatedly shrinking the prefix can involve additional copying.
* The first string may be much longer than the actual common prefix.
"""
# Start with the first string as the prefix and shrink it until every string starts with it.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix
    
    
