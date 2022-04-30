class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[0 for _ in range(math.ceil((len(s)/4))*2)] for _ in range(numRows)]
        x = 0
        y = 0
        i = 0
        res = ""
        if numRows == 1:
            return s
        for _ in range(math.ceil((len(s)/4))*2):
            # while i < len(s):
            # 00 10 20 11   02 12 22 13
            for _ in range(numRows):
                if i >= len(s):
                    break
                matrix[x][y] = s[i]
                i += 1
                
                x += 1
                if x == numRows:
                    x = 0
            if i >= len(s):
                    break
            y += (numRows-1)
            for tmp in range(numRows-2,0,-1):
                if i >= len(s):
                    break
                matrix[x+tmp][y-tmp] = s[i]
                i += 1

        for j in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[j][k] != 0:
                    res += matrix[j][k]
        return res




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。