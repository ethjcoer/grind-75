class Solution:
    def climbStairs(self, n: int) -> int:
        # This function calculates the number of distinct ways to climb `n` stairs.
        # You can climb 1 or 2 steps at a time. This is a classic Fibonacci problem.

        p, q = 0, 1  # Initialize variables: p (n-2), q (n-1).

        for i in range(n):
            # Update p and q for the next step.
            # p becomes the previous q, and q becomes the sum of p and q.
            p, q = q, p + q

        return q  # q represents the number of ways to climb `n` stairs.
