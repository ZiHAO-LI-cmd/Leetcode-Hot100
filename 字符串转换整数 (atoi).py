class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1
        s = s.strip()
        if not s: return 0
        i, sign = 0, 1
        res = 0
        if s[0] in '+-':
            sign = 1 if s[0] == '+' else -1
            i += 1
        while i < len(s):
            if not s[i].isdigit(): break
            res = res * 10 + int(s[i])
            if not INT_MIN <= sign * res <= INT_MAX:
                return INT_MIN if sign * res < INT_MIN else INT_MAX
            i += 1
        return sign * res



        
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值


# ^：匹配字符串开头
# [\+\-]：代表一个+字符或-字符
# ?：前面一个字符可有可无
# \d：一个数字
# +：前面一个字符的一个或多个
# \D：一个非数字字符
# *：前面一个字符的0个或多个

