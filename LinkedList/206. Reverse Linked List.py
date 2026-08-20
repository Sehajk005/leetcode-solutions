"""
Optimal Approach:
Iterative Pointer Reversal

Problem: 206. Reverse Linked List

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Linked List
Two Pointers
In-place Reversal

Approach:
- Use two pointers:
    `prev` → the already reversed part
    `curr` → the node currently being processed
- Initially:
    `prev = None`
    `curr = head`
- For every node:
    1. Save the next node before changing the pointer.
    2. Reverse the current node's `next` pointer.
    3. Move `prev` to the current node.
    4. Move `curr` to the saved next node.
- When `curr` becomes `None`, the entire list is reversed.
- `prev` is now the new head, so return `prev`.

Pointer Roles:

    `prev`
    → Head of the already reversed portion

    `curr`
    → Node currently being reversed

    `next_node`
    → Saved reference to the next node we still need to process

Why do we need `next_node`?

Before reversing:

    curr.next → next node

For example:

    1 → 2 → 3

If:

    curr = 1

and we directly do:

    curr.next = prev

then:

    1 → None

The connection to `2` would be lost.

So first save it:

    next_node = curr.next

Then reverse:

    curr.next = prev

Then we can safely move forward:

    curr = next_node


Initial State:

    prev = None
    curr = 1

    None    1 → 2 → 3 → 4 → 5 → None
     ↑      ↑
    prev   curr


Iteration 1:

    next_node = curr.next

    next_node = 2

    curr.next = prev

    1 → None

    prev = curr

    prev = 1

    curr = next_node

    curr = 2

State:

    prev    curr
     ↓       ↓
    1 → None 2 → 3 → 4 → 5 → None


Iteration 2:

    next_node = 3

    curr.next = prev

    2 → 1 → None

    prev = 2
    curr = 3

State:

    prev       curr
     ↓          ↓
    2 → 1 → None 3 → 4 → 5 → None


Iteration 3:

    next_node = 4

    curr.next = prev

    3 → 2 → 1 → None

    prev = 3
    curr = 4


Iteration 4:

    next_node = 5

    curr.next = prev

    4 → 3 → 2 → 1 → None

    prev = 4
    curr = 5


Iteration 5:

    next_node = None

    curr.next = prev

    5 → 4 → 3 → 2 → 1 → None

    prev = 5
    curr = None


Final State:

    prev
     ↓
    5 → 4 → 3 → 2 → 1 → None

    curr = None


Why return `prev`?

At the end of the loop:

    curr = None

because there are no more nodes to process.

But `prev` points to:

    5 → 4 → 3 → 2 → 1 → None

Therefore, `prev` is the new head of the reversed linked list.

    return prev


Key Insight:

The reversal happens through:

    curr.next = prev

The movement happens through:

    prev = curr
    curr = next_node

Think of each iteration as moving one node from the
unreversed portion to the reversed portion:

    Before:

    None    1 → 2 → 3 → 4 → 5
     ↑      ↑
    prev   curr

    After processing 1:

    1 → None    2 → 3 → 4 → 5
    ↑           ↑
    prev       curr

    After processing 2:

    2 → 1 → None    3 → 4 → 5
    ↑               ↑
    prev           curr

    After processing 3:

    3 → 2 → 1 → None    4 → 5
    ↑                   ↑
    prev               curr

    ...

    Final:

    5 → 4 → 3 → 2 → 1 → None
    ↑
    prev


Why `[::-1]` cannot be used:

- `[::-1]` reverses Python sequences such as lists and strings.
- A linked list is a collection of separate nodes connected by
  `next` pointers.
- To reverse a linked list, we must change those `next` pointers.
- The iterative solution does this in-place.
- No new linked-list nodes are required.

Space Complexity:

    O(1)

Only three references are used:

    prev
    curr
    next_node

We do not create another list or store all nodes.


Final Code:

    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


Core Formula to Remember:

    SAVE → REVERSE → MOVE PREV → MOVE CURR

    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev