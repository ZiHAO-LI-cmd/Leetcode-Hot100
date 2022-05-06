# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs[0]) == 0:       # [""]
#             return ""
#         if len(strs) == 1:          # ["a"]
#             return strs[0]
#         index = 0
#         for index in range(len(strs[0])):
#             for s in strs:
#                 if s.startswith(strs[0][:index+1]):
#                     continue
#                 else:
#                     return strs[0][:index]  # 一般情况
#         return strs[0][:index + 1]  # ["flower", "flower", "flower"]
        

strs = ["flower","flow","flight"]
for tmp in zip(*strs):
    print(tmp)



# 纵向扫描
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        
        return strs[0]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。