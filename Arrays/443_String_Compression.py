"""
Approach:
Build Compressed String

Problem: 443. String Compression

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
String Building / Simulation

Approach:
- Initialize an empty string `s` and a counter `count = 1`.
- Traverse the array from left to right while comparing each character with the next one.
- If the current character is the same as the next:
    - Increment the count.
- Otherwise:
    - Append the current character to the string.
    - If count > 1, append its frequency as a string.
    - Reset count to 1.
- After the loop, process the last group of characters.
- Return the length of the compressed string.

Key Insight:
- Consecutive identical characters form one group.
- Each group is represented by:
    - Character only, if frequency = 1.
    - Character followed by its count, if frequency > 1.

Example:
chars = ["a","a","b","b","c","c","c"]

Groups:
aa → a2
bb → b2
ccc → c3

Compressed String:
"a2b2c3"

Length = 6

Note:
- Easy to understand and implement.
- Correctly handles multi-digit counts by converting the count to a string.
- Uses extra space to build a new compressed string.
- Does not compress the array in-place, so it does not satisfy the optimal space requirement.
"""
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        count = 1
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                count += 1
            elif chars[i] != chars[i+1] and count == 1:
                s += chars[i]
                count = 1
            elif chars[i] != chars[i+1] and count>1:
                s += chars[i]
                s += str(count)
                count = 1
        if count == 1:
            s += chars[-1]
        else:
            s += chars[-1]
            s += str(count)
        
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)
    

"""
Approach:
Two Pointers (In-Place Compression)

Problem: 443. String Compression

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Two Pointers / In-Place Array Modification

Approach:
- Maintain two pointers:
    - read → scans the original array.
    - write → writes the compressed result.
- For each group of consecutive identical characters:
    - Count how many times the character appears.
    - Write the character at the write pointer.
    - If the count is greater than 1:
        - Convert the count to a string.
        - Write each digit separately into the array.
- Continue until all characters are processed.
- Return the value of the write pointer as the new length.

Key Insight:
- The read pointer identifies one complete group at a time.
- The write pointer overwrites the array with the compressed representation.
- Each digit of the count is stored separately, allowing counts greater than 9.

Example:
chars = ["a","a","b","b","c","c","c"]

Read Groups:
aa  → count = 2
bb  → count = 2
ccc → count = 3

Writing Process:
a → 2
b → 2
c → 3

Modified Array:
["a","2","b","2","c","3", ...]

New Length = 6

Note:
- Compresses the array in-place without using extra storage.
- Supports counts with multiple digits (e.g., 12 → "1", "2").
- The remaining elements after the returned length are ignored.
- This is the optimal solution because it runs in O(n) time using O(1) extra space.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0 
        while read<len(chars):
            ch=chars[read]
            count=0
            while read<len(chars) and ch==chars[read]:
                count+=1
                read+=1
            chars[write]=str(ch)
            write+=1
            if count>1:
                for d in str(count):
                    chars[write]=d
                    write+=1
        return write 