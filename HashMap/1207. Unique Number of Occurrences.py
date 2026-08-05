"""
Approach 1:
Frequency Map + List + Set Comparison

Problem: 1207. Unique Number of Occurrences

Difficulty: Easy

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Pattern:
Hash Map + Hash Set

Approach:
- Traverse the array and count the frequency of each number using a dictionary.
- Store all frequency values in a list.
- Convert the list into a set.
- Compare the lengths of the list and the set.
- If both lengths are equal, every frequency is unique.

Key Insight:
- A set automatically removes duplicate values.
- If two numbers have the same occurrence count, the set becomes smaller than the list.

Example:
arr = [1,2,2,1,1,3]

Frequency Map:
1 → 3
2 → 2
3 → 1

Occurrences List:
[3,2,1]

Set:
{1,2,3}

Lengths are equal.

Output:
True

Note:
- Easy to understand and implement.
- Uses an additional list to store frequencies before checking uniqueness.
"""
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        occurrences = []

        for num in freq:
            occurrences.append(freq[num])

        return len(occurrences) == len(set(occurrences))


"""
Approach 2:
Frequency Map + Seen Set (Early Exit)

Problem: 1207. Unique Number of Occurrences

Difficulty: Easy

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Pattern:
Hash Map + Hash Set

Approach:
- Count the frequency of every number using a dictionary.
- Create an empty set called 'seen'.
- Traverse all frequency values.
- If a frequency already exists in the set, return False immediately.
- Otherwise, add it to the set.
- Return True after checking all frequencies.

Key Insight:
- The set keeps track of frequencies that have already appeared.
- Detecting a duplicate frequency allows an early return without checking the remaining values.

Example:
arr = [1,2]

Frequency Map:
1 → 1
2 → 1

Seen:
{}

Check frequency 1:
Seen = {1}

Check frequency 1 again:
Already in seen.

Output:
False

Note:
- More memory-efficient than storing all frequencies in a list.
- Can terminate early when a duplicate occurrence is found.
- Preferred interview solution.
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        seen = set()

        for num in freq:
            if freq[num] in seen:
                return False
            seen.add(freq[num])

        return True
    

"""
Approach 3:
Frequency Map using get() + Set Comparison

Problem: 1207. Unique Number of Occurrences

Difficulty: Easy

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Pattern:
Hash Map + Hash Set

Approach:
- Count frequencies using dictionary.get().
- Obtain all frequency values using freq.values().
- Convert the values into a set.
- Compare the number of frequency values with the size of the set.

Key Insight:
- dict.get(key, default) simplifies frequency counting by eliminating explicit if-else conditions.
- dict.values() provides all occurrence counts directly without creating another list.

Example:
arr = [1,2,2,1,1,3]

Frequency Map:
{
    1:3,
    2:2,
    3:1
}

Values:
dict_values([3,2,1])

Set:
{1,2,3}

Output:
True

Note:
- Cleaner and shorter than manually checking dictionary keys.
- Avoids creating an extra list of occurrences.
- A common Pythonic solution.
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        return len(freq.values()) == len(set(freq.values()))


"""
Approach 4:
Counter + Set Comparison (Most Pythonic)

Problem: 1207. Unique Number of Occurrences

Difficulty: Easy

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Pattern:
Hash Map (Counter) + Hash Set

Approach:
- Use Counter() to count the occurrences of every element.
- Retrieve all occurrence counts using values().
- Convert the counts into a set.
- Compare the sizes of the values collection and the set.

Key Insight:
- Counter automatically builds the frequency map in one line.
- Combining Counter with a set produces the shortest and cleanest solution.

Example:
arr = [1,2,2,1,1,3]

Counter:
Counter({
    1:3,
    2:2,
    3:1
})

Values:
dict_values([3,2,1])

Set:
{1,2,3}

Output:
True

Note:
- Shortest implementation.
- Uses Python's collections.Counter.
- Ideal when built-in libraries are allowed.
"""
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))