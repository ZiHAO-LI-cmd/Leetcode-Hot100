# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j]表示从s[i-j]是不是回文子串
        dp = [[False] * n for _ in range(n)]
        # 单独一个字符是回文子串
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1):
            # 左边界
            for left in range(n):
                # length = right - left + 1
                right = length + left - 1
                # 右边界越界
                if right >= n:
                    break

                if s[left] != s[right]:
                    dp[left][right] = False
                else:
                    if right - left <= 2:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left + 1][right - 1]

                # 只要 dp[left][right] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[left][right] == True and (right - left + 1) > max_len:
                    max_len = right - left + 1
                    begin = left
        
        return s[begin:begin + max_len]


# 中心扩展
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。