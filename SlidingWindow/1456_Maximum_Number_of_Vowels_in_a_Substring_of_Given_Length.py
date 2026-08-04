"""
Approach 1:
Brute Force (Create Every Window + Count Vowels Again)

Problem: 1456. Maximum Number of Vowels in a Substring of Given Length

Difficulty: Medium

Time Complexity: O(n × k)
Space Complexity: O(k)

Pattern:
Brute Force / Sliding Window Simulation

Approach:
- Create the first substring (window) of size `k`.
- For every possible window:
    - Count the vowels in the current substring using `count()`.
    - Store the maximum vowel count.
    - Create the next substring using slicing.
- Count the vowels in the final window after the loop.

Key Insight:
- Every window is rebuilt from scratch.
- The vowel count is also recalculated from scratch for every window.
- Since both slicing and counting require scanning the substring, the same work is repeated many times.

Example:
s = "abciiidef"
k = 3

Windows:
"abc" → 1 vowel
"bci" → 1 vowel
"cii" → 2 vowels
"iii" → 3 vowels
"iid" → 2 vowels
"ide" → 2 vowels
"def" → 1 vowel

Maximum = 3

Note:
- Very easy to understand.
- Creates a new substring every iteration.
- Recounts all vowels every time.
- Not suitable for large inputs.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = s[:k]
        max_vowels = 0
        for i in range(1, len(s)-k+1):
            vowels = sum(start.count(vowels) for vowels in 'aeiouAEIOU')
            start = s[i:i+k]
            max_vowels = max(max_vowels, vowels)
        vowels = sum(start.count(vowels) for vowels in 'aeiouAEIOU')
        max_vowels = max(max_vowels, vowels)
        return max_vowels
    

"""
Approach 2:
Sliding Window using String Update

Problem: 1456. Maximum Number of Vowels in a Substring of Given Length

Difficulty: Medium

Time Complexity: O(n × k)
Space Complexity: O(k)

Pattern:
Sliding Window (String Manipulation)

Approach:
- Store the first window as a string.
- For every new character:
    - Count vowels in the current window.
    - Append the incoming character.
    - Remove the outgoing character using replace().
    - Update the maximum vowel count.
- Count the last window after the loop.

Key Insight:
- Instead of recreating the entire substring with slicing,
  the window string is updated by:
    - Adding one new character.
    - Removing one old character.
- However, vowel counting is still done from scratch for every window,
  so the overall complexity remains O(n × k).

Example:
s = "abciiidef"
k = 3

Initial Window:
"abc" → 1 vowel

Slide:
Add 'i'
Remove 'a'
Window = "bci" → 1 vowel

Slide:
Add 'i'
Remove 'b'
Window = "cii" → 2 vowels

Continue...

Maximum = 3

Note:
- Demonstrates how a sliding window can be maintained.
- String operations still create new strings.
- Counting vowels every iteration is still expensive.
- Better window management than Approach 1, but not yet optimal.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = s[:k]
        max_vowels = 0
        for i in range(k, len(s)):
            vowels = sum(start.count(vowels) for vowels in 'aeiouAEIOU')
            start += s[i]
            start = start.replace(s[i-k], '', 1)
            max_vowels = max(max_vowels, vowels)
        vowels = sum(start.count(vowels) for vowels in 'aeiouAEIOU')
        max_vowels = max(max_vowels, vowels)
        return max_vowels
   
   
"""
Approach 3:
Optimal Sliding Window (Maintain Running Vowel Count)

Problem: 1456. Maximum Number of Vowels in a Substring of Given Length

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(k)

Pattern:
Sliding Window

Approach:
- Create the first window using `s[:k]`.
- Count the vowels in this initial window.
- Store this as the current vowel count.
- Slide the window across the string:
    - If the incoming character is a vowel, increment the count.
    - If the outgoing character is a vowel, decrement the count.
    - Update the maximum vowel count.

Key Insight:
- Consecutive windows overlap by `k - 1` characters.
- Instead of recounting vowels for every window, only update the count using the incoming and outgoing characters.
- This reduces the time complexity from O(n × k) to O(n).

Example:
s = "abciiidef"
k = 3

Initial Window:
"abc"
Count = 1
Max = 1

Slide:
Add 'i'
Remove 'a'
Count = 1
Max = 1

Slide:
Add 'i'
Remove 'b'
Count = 2
Max = 2

Slide:
Add 'i'
Remove 'c'
Count = 3
Max = 3

Continue...

Answer = 3

Note:
- The initial substring `s[:k]` requires O(k) extra space.
- The window itself is not recreated while sliding.
- Each character is processed only once.
- This is time-optimal (O(n)), but not space-optimal because of the initial slice.
""" 
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        start = s[:k]
        count = 0
        max_count = 0
        for ch in start:
            if ch in vowels:
                count += 1
        max_count = max(max_count, count)
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            max_count = max(count, max_count)
        return max_count



"""
Approach 4:
Optimal Sliding Window (Without First Window Slice)

Problem: 1456. Maximum Number of Vowels in a Substring of Given Length

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Sliding Window

Approach:
- Build the first window directly using indices.
- Count its vowels.
- Slide the window:
    - Add the incoming vowel if present.
    - Remove the outgoing vowel if present.
    - Update the maximum count.

Key Insight:
- Same optimal sliding window idea as Approach 3.
- Avoids creating the initial substring (`s[:k]`).
- Works entirely with indices, making it slightly more memory-efficient.

Example:
s = "abciiidef"
k = 3

Initial Window:
Indices [0..2]
"abc"
Count = 1

Slide:
Incoming = 'i'
Outgoing = 'a'
Count = 1

Slide:
Incoming = 'i'
Outgoing = 'b'
Count = 2

Slide:
Incoming = 'i'
Outgoing = 'c'
Count = 3

Maximum = 3

Note:
- No substring creation anywhere.
- Every character is visited only once.
- Uses only variables and indices.
- This is the cleanest and most efficient implementation.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count = 0
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = max(max_count, count)
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            max_count = max(count, max_count)
        return max_count