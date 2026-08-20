"""
Brute Force Approach:
List Traversal

Problem: 933. Number of Recent Calls

Difficulty: Easy

Time Complexity: O(n) per `ping()` call
Space Complexity: O(n)

Pattern:
Sliding Window

Approach:
- Store every request timestamp in the `requests` list.
- Whenever `ping(t)` is called:
    - Add the new timestamp `t` to the list.
    - Traverse through all previously stored requests.
    - Count the requests that fall within the required time range.
- Return the total count.

Time Window:
- A request is considered recent if:
    `t - 3000 <= request <= t`
- Since timestamps are added in increasing order, older requests will
  eventually fall outside this window.

Example:
ping(1)
requests = [1]
Recent requests = [1]
Answer = 1

ping(100)
requests = [1, 100]
Recent requests = [1, 100]
Answer = 2

ping(3001)
requests = [1, 100, 3001]
Recent requests = [1, 100, 3001]
Answer = 3

ping(3002)
requests = [1, 100, 3001, 3002]

Window:
[2, 3002]

Request `1` is outside the window.
Recent requests = [100, 3001, 3002]
Answer = 3

Key Insight:
- Every `ping()` scans the entire list, even though many old requests
  are already known to be outside the 3000ms window.
- Because timestamps arrive in increasing order, once a request becomes
  too old, it will never become relevant again.

Note:
- This solution is simple and easy to understand.
- However, repeatedly scanning all requests is inefficient.
- The time complexity can become O(n²) over many `ping()` calls.
- We can optimize this by removing expired requests as soon as they
  become irrelevant.
"""
class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        count = 0
        for request in self.requests:
            if t-3000<request<t:
                count+=1
        return count

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
Optimal Approach:
Sliding Window + Queue

Problem: 933. Number of Recent Calls

Difficulty: Easy

Time Complexity: O(1) amortized per `ping()` call
Space Complexity: O(n)

Pattern:
Sliding Window
Queue

Approach:
- Use a `deque` to store only the timestamps that are currently inside
  the 3000ms window.
- Add the new request `t` to the queue.
- Remove timestamps from the front while they are outside the window.
- Since timestamps arrive in increasing order, the oldest request is
  always at the front of the queue.
- After removing expired requests, the size of the queue is exactly the
  number of recent requests.

Time Window:
    `t - 3000 <= request <= t`

Example:
ping(1)

Queue:
[1]

Answer:
1

ping(100)

Queue:
[1, 100]

Answer:
2

ping(3001)

Queue:
[1, 100, 3001]

All requests are within:
[1, 3001]

Answer:
3

ping(3002)

Before removing:
[1, 100, 3001, 3002]

Window:
[2, 3002]

Remove `1` because:
1 < 3002 - 3000

Queue becomes:
[100, 3001, 3002]

Answer:
3

Why `deque`?
- We need to add new requests at the back.
- We need to remove expired requests from the front.
- `deque.append()` → O(1)
- `deque.popleft()` → O(1)
- A normal list's `pop(0)` would be O(n).

Key Insight:
- The timestamps are guaranteed to arrive in increasing order.
- Therefore, the queue is automatically sorted.
- Once a timestamp is older than `t - 3000`, it can be permanently removed.
- Each timestamp is:
    1. Added once.
    2. Removed at most once.
- Therefore, although the `while` loop may remove multiple elements in
  one call, each element is processed only a constant number of times.

Why the condition is:
    `self.requests[0] < t - 3000`

The boundary is included.

For example, if:
`t = 3001`

Then:
`t - 3000 = 1`

A request at `1` is valid because:
`1 <= 1`

So we remove only requests where:
`request < t - 3000`

Not:
`request <= t - 3000`

Note:
- The first solution stores every request and scans them repeatedly.
- The optimal solution keeps only the active sliding window.
- `deque` is ideal because we need FIFO behavior:
    - append at the back
    - popleft from the front
- This gives O(1) amortized time per `ping()` and is the optimal approach.
"""
from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0]<t-3000:
            self.requests.popleft()
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)