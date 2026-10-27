"""
Problem: 58. Length of Last Word
Difficulty: Easy
Approach 1: Using split() to Extract Words

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:

* String Manipulation
* Built-in String Methods

Approach:

* Use split() to divide the string into a list of words.
* split() automatically removes leading and trailing whitespace
  and handles multiple spaces between words.
* Access the last word using s[-1].
* Return the length of the last word using len().

Why it works:

* split() creates a list containing only non-empty words.
* The last element of the list is always the last word.
* len() calculates the number of characters in that word.

Advantages:

* Simple, readable, and easy to implement.
* No need to manually handle spaces.

Limitation:

* Creates a list of words, requiring O(n) extra space.
"""
# Using split() to extract words and return the length of the last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split() # or s = s.strip().split()
        return len(s[-1])
    
"""
Problem: 58. Length of Last Word
Difficulty: Easy
Approach 2: Manually Extracting Words Using a Single Loop

Time Complexity: O(n^2) in the worst case with immutable string concatenation
Space Complexity: O(n)

Pattern:

* String Traversal
* Manual Parsing
* String Manipulation

Approach:

* Initialize an empty list list_words to store extracted words.
* Set i = 0 to traverse the string.
* Initialize new_word = '' to build the current word.
* Traverse the string character by character.
* If the current character is alphabetic:
    * Append it to new_word.
* Otherwise:
    * If new_word is not empty, append it to list_words.
    * Reset new_word to an empty string.
* Increment i after processing each character.
* After the loop, check new_word again.
* If it contains a word, append it to list_words.
* Return the length of the last word.

Why it works:

* Alphabetic characters are collected into the current word.
* A non-alphabetic character marks the end of a word.
* The final check handles strings that end directly with a word
  rather than a separator.
* The last extracted word is stored at list_words[-1].

Limitation:

* Stores every extracted word, requiring O(n) extra space.
* String concatenation inside the loop can take O(n^2) time
  in the worst case.
* isalpha() recognizes alphabetic characters, not just English letters.
"""
# Manually extracting words using a single loop and returning the length of the last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_words = []
        i = 0
        new_word = ''
        while i<len(s):
            if s[i].isalpha():
                new_word += s[i]
            else:
                if new_word:
                    list_words.append(new_word)
                    new_word = ''
            i+=1
        if new_word:
            list_words.append(new_word)
        return len(list_words[-1])
    
"""
Problem: 58. Length of Last Word
Difficulty: Easy
Approach 3: Using Nested Loops to Extract Words

Time Complexity: O(n^2) in the worst case with immutable string concatenation
Space Complexity: O(n)

Pattern:

* String Traversal
* Nested Loops
* Manual Parsing

Approach:

* Initialize list_words to store extracted words.
* Set i = 0 to track the current position in the string.
* Start the outer while loop while i < len(s).
* Reset new_word = '' at the beginning of each iteration.
* Use the inner while loop to collect consecutive alphabetic
  characters into new_word.
* Increment i inside the inner loop as each character is processed.
* Once a word ends, append new_word to list_words if it is not empty.
* Increment i once more to skip the separator.
* After the outer loop finishes, return len(list_words[-1]).

Why it works:

* The inner loop processes an entire word at a time.
* The outer loop continues searching for the next word.
* Empty strings are not added to the list.
* The final list element contains the last extracted word.

Limitation:

* Requires O(n) extra space to store all words.
* String concatenation can result in O(n^2) worst-case time.
* The extra i += 1 assumes the character after a word is a
  single separator. It can skip a character when there are
  consecutive separators, although the next iteration may
  recover if that character is alphabetic.
* Like Approach 2, isalpha() treats only alphabetic characters
  as part of a word.
"""
# Using nested loops to extract words and return the length of the last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_words = []
        i = 0
        new_word = ''
        while i<len(s):
            new_word = ''
            while i<len(s) and s[i].isalpha():
                new_word += s[i]
                i+=1
            if new_word:
                list_words.append(new_word)
            i+=1
        return len(list_words[-1])
    
    
"""
Problem: 58. Length of Last Word
Difficulty: Easy
Approach 4: Reverse Traversal Without Storing Words

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Two-Pointer / Reverse Traversal
* String Manipulation
* Space Optimization

Approach:

* Initialize i at the last index of the string.
* Initialize length = 0.
* Skip trailing spaces by moving i backward.
* Traverse backward while characters are not spaces.
* Increment length for each character in the last word.
* Return length.

Why it works:

* Trailing spaces are skipped before counting begins.
* The first space encountered after counting starts marks
  the beginning of the last word.
* Only a counter is needed; no list or additional string is created.

Advantages:

* O(n) time complexity.
* O(1) extra space.
* Avoids storing or constructing words.
"""
# Reverse traversal without storing words and returning the length of the last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        length = 0
        while i>=0 and s[i] == ' ':
            i-=1
        while i>=0 and s[i] != ' ':
            length+=1
            i-=1
        return length
