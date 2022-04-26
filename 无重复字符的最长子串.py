class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        right = -1 
        max_len = 0

        for left in range(len(s)):
            if left != 0:
                # 左指针向右移动一格，移除一个字符
                substr.remove(s[left - 1])

            #while s[right + 1] not in substr and right + 1 < len(s)  Wrong  out of index
            while right + 1 < len(s) and s[right + 1] not in substr:   
                substr.add(s[right + 1])
                right = right + 1

            cur_len = right - left + 1
            max_len = max(max_len,cur_len)
        return max_len