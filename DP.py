
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# 示例 1：

# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace" ，它的长度为 3 



# DP 递归

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(n - 1, m - 1)

# DP 递推
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                f[i + 1][j + 1] = f[i][j] + 1 if x == y else \
                                  max(f[i][j + 1], f[i + 1][j])
        return f[n][m]


# DP 递推-空间优化 1
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(2)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                f[(i + 1) % 2][j + 1] = f[i % 2][j] + 1 if x == y else \
                                        max(f[i % 2][j + 1], f[(i + 1) % 2][j])
        return f[n % 2][m]


# DP 递推-空间优化 2
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        f = [0] * (len(t) + 1)
        for x in s:
            pre = 0  # f[0]
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre + 1 if x == y else max(f[j + 1], f[j])
                pre = tmp
        return f[-1]

