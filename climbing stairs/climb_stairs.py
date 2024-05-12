class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(3, n + 1):
            dp[i - 1] = max(dp[i - 2] + 1, dp[i - 3] + 2)
        return dp[n - 1]


if __name__ == '__main__':
    print_hi('PyCharm')

